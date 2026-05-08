from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .com import import_pywin32, int_byref, member_value, unpack_out_call
from .constants import (
    DocumentType,
    OpenDocOptions,
    PaperSize,
    UserPreferenceStringValue,
    document_type_from_path,
)
from .errors import SolidWorksError
from .assembly import AssemblyDoc
from .model import ModelDoc


class SolidWorks:
    def __init__(self, com: Any) -> None:
        self.com = com

    @classmethod
    def connect(
        cls,
        *,
        visible: bool | None = True,
        start: bool = True,
        new_instance: bool = False,
        prog_id: str = "SldWorks.Application",
    ) -> "SolidWorks":
        pythoncom, win32com_client = import_pywin32()
        pythoncom.CoInitialize()
        app = None
        if not new_instance:
            try:
                app = win32com_client.GetActiveObject(prog_id)
            except Exception:
                app = None
        if app is None:
            if not start:
                raise SolidWorksError("SOLIDWORKS is not running")
            dispatch = win32com_client.DispatchEx if new_instance else win32com_client.Dispatch
            app = dispatch(prog_id)
        if visible is not None:
            app.Visible = bool(visible)
        return cls(app)

    @property
    def revision_number(self) -> str:
        return str(member_value(self.com, "RevisionNumber"))

    def active_doc(self) -> ModelDoc:
        doc = member_value(self.com, "ActiveDoc", None) or member_value(self.com, "IActiveDoc2", None)
        if doc is None:
            raise SolidWorksError("No active SOLIDWORKS document")
        return ModelDoc(doc, self)

    def open(
        self,
        path: str | Path,
        *,
        doc_type: int | DocumentType | None = None,
        options: int | OpenDocOptions = OpenDocOptions.Silent,
        configuration: str = "",
        activate: bool = False,
    ) -> ModelDoc:
        path = Path(path)
        if doc_type is None:
            doc_type = document_type_from_path(path)
        errors = int_byref()
        warnings = int_byref()
        result = self.com.OpenDoc6(str(path), int(doc_type), int(options), configuration, errors, warnings)
        out = unpack_out_call(result, errors, warnings)
        if out.value is None:
            raise SolidWorksError(f"Failed to open SOLIDWORKS document: {path}", errors=out.errors, warnings=out.warnings)
        model = AssemblyDoc(out.value, self) if int(doc_type) == int(DocumentType.ASSEMBLY) else ModelDoc(out.value, self)
        if activate:
            model.activate()
        return model

    def new_document(
        self,
        template: str | Path,
        *,
        paper_size: int | PaperSize = PaperSize.UserDefined,
        width: float = 0.0,
        height: float = 0.0,
    ) -> ModelDoc:
        doc = self.com.NewDocument(str(template), int(paper_size), float(width), float(height))
        if doc is None:
            raise SolidWorksError(f"Failed to create SOLIDWORKS document from template: {template}")
        return ModelDoc(doc, self)

    def try_new_document(
        self,
        template: str | Path,
        *,
        paper_size: int | PaperSize = PaperSize.UserDefined,
        width: float = 0.0,
        height: float = 0.0,
    ) -> ModelDoc | None:
        if not template:
            return None
        doc = self.com.NewDocument(str(template), int(paper_size), float(width), float(height))
        return ModelDoc(doc, self) if doc is not None else None

    def default_template(
        self,
        kind: int | DocumentType,
        *,
        template_name: str = "",
        paper_size: int | PaperSize = PaperSize.UserDefined,
        width: float = 0.0,
        height: float = 0.0,
    ) -> str:
        value = self.com.GetDocumentTemplate(int(kind), template_name, int(paper_size), float(width), float(height))
        if not value:
            raise SolidWorksError(f"No SOLIDWORKS template is configured for document type {int(kind)}")
        return str(value)

    def new_part(self) -> ModelDoc:
        return self.new_document_from_candidates(DocumentType.PART)

    def new_assembly(self) -> AssemblyDoc:
        doc = self.new_document_from_candidates(DocumentType.ASSEMBLY)
        return AssemblyDoc(doc.com, self)

    def new_drawing(self, *, width: float = 0.0, height: float = 0.0) -> ModelDoc:
        return self.new_document_from_candidates(DocumentType.DRAWING, width=width, height=height)

    def new_document_from_candidates(
        self,
        kind: int | DocumentType,
        *,
        paper_size: int | PaperSize = PaperSize.UserDefined,
        width: float = 0.0,
        height: float = 0.0,
    ) -> ModelDoc:
        candidates = self.document_template_candidates(kind, paper_size=paper_size, width=width, height=height)
        tried: list[str] = []
        for template in candidates:
            tried.append(str(template))
            doc = self.try_new_document(template, paper_size=paper_size, width=width, height=height)
            if doc is not None:
                return doc
        detail = ", ".join(tried) if tried else "no template candidates"
        raise SolidWorksError(f"Failed to create SOLIDWORKS document for type {int(kind)}; tried: {detail}")

    def document_template_candidates(
        self,
        kind: int | DocumentType,
        *,
        paper_size: int | PaperSize = PaperSize.UserDefined,
        width: float = 0.0,
        height: float = 0.0,
    ) -> list[str]:
        kind = DocumentType(int(kind))
        suffix = {
            DocumentType.PART: ".prtdot",
            DocumentType.ASSEMBLY: ".asmdot",
            DocumentType.DRAWING: ".drwdot",
        }[kind]
        env_var = {
            DocumentType.PART: "SOLIDWORKS_PART_TEMPLATE",
            DocumentType.ASSEMBLY: "SOLIDWORKS_ASSEMBLY_TEMPLATE",
            DocumentType.DRAWING: "SOLIDWORKS_DRAWING_TEMPLATE",
        }[kind]
        pref = {
            DocumentType.PART: UserPreferenceStringValue.DefaultTemplatePart,
            DocumentType.ASSEMBLY: UserPreferenceStringValue.DefaultTemplateAssembly,
            DocumentType.DRAWING: UserPreferenceStringValue.DefaultTemplateDrawing,
        }[kind]

        candidates: list[str] = []
        candidates.extend(_split_paths(os.environ.get(env_var, "")))
        try:
            candidates.append(self.default_template(kind, paper_size=paper_size, width=width, height=height))
        except SolidWorksError:
            pass
        candidates.append(self.user_preference_string(pref))

        template_dirs = _split_paths(self.user_preference_string(UserPreferenceStringValue.FileLocationsDocumentTemplates))
        candidates.extend(_templates_in_dirs(template_dirs, suffix, preferred_tokens=_preferred_template_tokens(kind)))
        return _existing_or_named(candidates, suffix)

    def user_preference_string(self, preference: int | UserPreferenceStringValue) -> str:
        getter = getattr(self.com, "GetUserPreferenceStringValue", None)
        if not callable(getter):
            return ""
        try:
            return str(getter(int(preference)) or "")
        except Exception:
            return ""

    def close(self, title_or_path: str | Path) -> None:
        self.com.CloseDoc(str(title_or_path))

    def exit(self) -> None:
        self.com.ExitApp()


def connect(**kwargs: Any) -> SolidWorks:
    return SolidWorks.connect(**kwargs)


def _split_paths(value: str) -> list[str]:
    paths: list[str] = []
    for chunk in value.replace("\n", ";").split(";"):
        chunk = chunk.strip().strip('"')
        if chunk:
            paths.append(chunk)
    return paths


def _templates_in_dirs(directories: list[str], suffix: str, *, preferred_tokens: tuple[str, ...]) -> list[str]:
    matches: list[Path] = []
    for directory in directories:
        path = Path(directory)
        if not path.exists() or not path.is_dir():
            continue
        matches.extend(path.glob(f"*{suffix}"))
    preferred = [p for p in matches if any(token in p.name.lower() for token in preferred_tokens)]
    others = [p for p in matches if p not in preferred]
    return [str(p) for p in sorted(preferred) + sorted(others)]


def _preferred_template_tokens(kind: DocumentType) -> tuple[str, ...]:
    if kind == DocumentType.PART:
        return ("part", "gb_part", "零件")
    if kind == DocumentType.ASSEMBLY:
        return ("assembly", "assem", "gb_assembly", "装配")
    return ("drawing", "draw", "gb_a", "工程图")


def _existing_or_named(candidates: list[str], suffix: str) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        if not candidate or Path(candidate).suffix.lower() != suffix:
            continue
        key = str(Path(candidate)).lower()
        if key in seen:
            continue
        seen.add(key)
        if Path(candidate).exists():
            result.insert(0, candidate)
        else:
            result.append(candidate)
    return result

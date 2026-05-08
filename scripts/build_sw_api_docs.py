from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as md


DEFAULT_API_DIR = Path(r"D:\Program Files\SOLIDWORKS Corp\SOLIDWORKS (2)\api")

DOCSETS = {
    "sldworksapi": {
        "kind": "cab",
        "cab": DEFAULT_API_DIR / "HelpViewer" / "sldworksapi" / "apihelpviewer.cab",
        "description": "Core SOLIDWORKS COM API interfaces, methods, properties, and events.",
    },
    "swconst": {
        "kind": "cab",
        "cab": DEFAULT_API_DIR / "HelpViewer" / "swconst" / "apienumshelpviewer.cab",
        "description": "SOLIDWORKS API constants and enumerations.",
    },
    "swdocmgrapi": {
        "kind": "chm",
        "chm": DEFAULT_API_DIR / "swdocmgrapi.chm",
        "description": "SOLIDWORKS Document Manager API.",
    },
    "swcommands": {
        "kind": "chm",
        "chm": DEFAULT_API_DIR / "swcommands.chm",
        "description": "SOLIDWORKS command IDs.",
    },
    "sldworksapiprogguide": {
        "kind": "chm",
        "chm": DEFAULT_API_DIR / "sldworksapiprogguide.chm",
        "description": "SOLIDWORKS API programming guide.",
    },
}

REMOVE_SELECTORS = [
    "script",
    "style",
    "link",
    "meta",
    "object",
    "iframe",
    "#i-before-header-content",
    "#i-header-content",
    "#i-after-header-content",
    "#BeforeHeaderContent",
    "#HeaderContent",
    "#AfterHeaderContent",
    ".i-before-header-content",
    ".i-header-content",
    ".i-after-header-content",
    ".i-popup-content",
    ".PopupContent",
    ".i-section-heading-icon",
]


@dataclass(frozen=True)
class Page:
    source: Path
    source_root: Path
    docset: str
    help_id: str
    title: str
    description: str
    output: Path


def progress(prefix: str, current: int, total: int, width: int = 32) -> None:
    if total <= 0:
        sys.stdout.write(f"\r{prefix} {current}")
        sys.stdout.flush()
        return
    done = int(width * current / total)
    bar = "#" * done + "." * (width - done)
    pct = int(100 * current / total)
    sys.stdout.write(f"\r{prefix} [{bar}] {current}/{total} {pct:3d}%")
    sys.stdout.flush()
    if current >= total:
        sys.stdout.write("\n")


def run_expand(source_cab: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    before = {p.resolve() for p in out_dir.glob("*")}
    cmd = ["expand.exe", "-F:*", str(source_cab), str(out_dir)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    after = [p for p in out_dir.glob("*") if p.resolve() not in before]
    candidates = after or list(out_dir.glob("*"))
    zip_like = [p for p in candidates if p.is_file() and p.read_bytes()[:4] == b"PK\x03\x04"]
    if not zip_like:
        raise RuntimeError(f"No MSHC/ZIP payload found after expanding {source_cab}")
    return zip_like[0]


def command_path(*names: str) -> str | None:
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def find_7zip(explicit_path: Path | None = None) -> str | None:
    candidates: list[Path] = []
    if explicit_path:
        candidates.append(explicit_path)
    candidates.extend(
        [
            Path(r"C:\Program Files\7-Zip\7z.exe"),
            Path(r"C:\Program Files (x86)\7-Zip\7z.exe"),
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return command_path("7z.exe", "7za.exe", "7z", "7za")


def count_html_files(path: Path) -> int:
    return sum(1 for _ in path.rglob("*.htm*"))


def extract_chm_with_progress(chm_path: Path, out_dir: Path, label: str, sevenzip: Path | None) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    seven_zip = find_7zip(sevenzip)
    if seven_zip:
        print(f"extract chm with 7-Zip: {chm_path}")
        subprocess.run(
            [seven_zip, "x", "-y", f"-o{out_dir}", str(chm_path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        total = count_html_files(out_dir)
        progress(label, total, total)
        return

    hh = command_path("hh.exe", "hh")
    if hh:
        print(f"extract chm with hh.exe: {chm_path}")
        before = count_html_files(out_dir)
        subprocess.run(
            [hh, "-decompile", str(out_dir), str(chm_path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        after = count_html_files(out_dir)
        progress(label, after, max(after, 1))
        if after > before:
            return

    raise RuntimeError(
        "Could not extract CHM. Install 7-Zip and make 7z.exe available on PATH, "
        "or run on a Windows setup where hh.exe -decompile works."
    )


def extract_zip_with_progress(zip_path: Path, out_dir: Path, label: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        members = [m for m in zf.infolist() if not m.is_dir()]
        total = len(members)
        for index, member in enumerate(members, start=1):
            zf.extract(member, out_dir)
            if index == total or index % 100 == 0:
                progress(label, index, total)


def text_or_empty(node) -> str:
    if node is None:
        return ""
    return " ".join(node.get_text(" ", strip=True).split())


def meta_content(soup: BeautifulSoup, name: str) -> str:
    tag = soup.find("meta", attrs={"name": name})
    if not tag:
        return ""
    return str(tag.get("content", "")).strip()


def slug_filename(source: Path) -> str:
    name = source.stem
    name = re.sub(r"[^\w.\-~]+", "_", name, flags=re.ASCII)
    return f"{name}.md"


def read_soup(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_bytes(), "lxml")


def discover_pages(html_root: Path, output_root: Path) -> list[Page]:
    pages: list[Page] = []
    for docset_dir in sorted(p for p in html_root.iterdir() if p.is_dir()):
        html_files = sorted(docset_dir.rglob("*.html"))
        for index, source in enumerate(html_files, start=1):
            soup = read_soup(source)
            help_id = meta_content(soup, "Microsoft.Help.Id") or source.stem
            title = meta_content(soup, "Title") or text_or_empty(soup.find("title")) or source.stem
            description = meta_content(soup, "Description")
            output = output_root / docset_dir.name / slug_filename(source)
            pages.append(Page(source, docset_dir, docset_dir.name, help_id, title, description, output))
            if index == len(html_files) or index % 1000 == 0:
                progress(f"index {docset_dir.name}", index, len(html_files))
    return pages


def local_link_for_href(href: str, current: Page, by_help_id: dict[str, Page]) -> str:
    if href.startswith("ms-xhelp://"):
        target_id = (parse_qs(urlparse(href).query).get("id") or [""])[0]
        target = by_help_id.get(target_id)
        if target:
            return os.path.relpath(target.output, current.output.parent).replace("\\", "/")
        return ""

    parsed = urlparse(href)
    if parsed.scheme in {"http", "https", "mailto"}:
        return href
    if not parsed.path.lower().endswith(".html"):
        return href

    target_html = (current.source.parent / parsed.path).resolve()
    try:
        target_html.relative_to(current.source_root.resolve())
    except ValueError:
        return href
    target_output = current.output.parent / slug_filename(target_html)
    return os.path.relpath(target_output, current.output.parent).replace("\\", "/")


def markdown_for_page(page: Page, by_help_id: dict[str, Page]) -> str:
    soup = read_soup(page.source)
    for selector in REMOVE_SELECTORS:
        for tag in soup.select(selector):
            tag.decompose()

    body = (
        soup.select_one("#i-body-content")
        or soup.select_one("#BodyContent")
        or soup.select_one(".i-body-content")
        or soup.body
        or soup
    )

    for tag in body.find_all(True):
        for attr in list(tag.attrs):
            if attr not in {"href", "src", "alt", "title", "colspan", "rowspan"}:
                del tag.attrs[attr]

    for anchor in body.find_all("a"):
        href = anchor.get("href")
        if href:
            new_href = local_link_for_href(href, page, by_help_id)
            if new_href:
                anchor["href"] = new_href
            else:
                del anchor["href"]

    body_md = md(str(body), heading_style="ATX", bullets="-", strip=["span"])
    body_md = re.sub(r"\n{3,}", "\n\n", body_md).strip()
    header = [f"# {page.title}", ""]
    if page.help_id:
        header += [f"Help ID: `{page.help_id}`", ""]
    if page.description:
        header += [page.description, ""]
    return "\n".join(header) + body_md + "\n"


def write_index(pages: list[Page], output_root: Path) -> None:
    lines = [
        "# SOLIDWORKS API Markdown Docs",
        "",
        "Generated from local SOLIDWORKS HelpViewer packages.",
        "",
        "## Included Docsets",
        "",
    ]
    for docset in sorted({p.docset for p in pages}):
        count = sum(1 for p in pages if p.docset == docset)
        desc = DOCSETS.get(docset, {}).get("description", "")
        lines.append(f"- `{docset}`: {count} pages. {desc}".rstrip())

    lines += ["", "## Python Binding Entry Points", ""]
    entry_titles = {
        "ISldWorks Interface",
        "IModelDoc2 Interface",
        "IAssemblyDoc Interface",
        "IPartDoc Interface",
        "IDrawingDoc Interface",
        "swDocumentTypes_e Enumeration",
        "swFileSaveError_e Enumeration",
        "swOpenDocOptions_e Enumeration",
        "swSaveAsOptions_e Enumeration",
    }
    for page in sorted((p for p in pages if p.title in entry_titles), key=lambda p: p.title):
        rel = page.output.relative_to(output_root).as_posix()
        lines.append(f"- [{page.title}]({rel})")

    lines += ["", "## Full Index", ""]
    for docset in sorted({p.docset for p in pages}):
        lines += [f"### {docset}", ""]
        for page in sorted((p for p in pages if p.docset == docset), key=lambda p: p.title.lower()):
            rel = page.output.relative_to(output_root).as_posix()
            lines.append(f"- [{page.title}]({rel})")
        lines.append("")

    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    build_root = args.build_dir
    html_root = build_root / "html"
    payload_root = build_root / "payload"

    if args.clean:
        shutil.rmtree(html_root, ignore_errors=True)
        shutil.rmtree(payload_root, ignore_errors=True)
        shutil.rmtree(args.output, ignore_errors=True)

    for docset in args.docsets:
        doc_html_dir = html_root / docset
        print(f"\n== {docset} ==")
        config = DOCSETS[docset]
        if config["kind"] == "cab":
            source_cab = config["cab"]
            if not source_cab.exists():
                raise FileNotFoundError(source_cab)
            doc_payload_dir = payload_root / docset
            print(f"expand cab: {source_cab}")
            payload = run_expand(source_cab, doc_payload_dir)
            print(f"extract mshc: {payload}")
            extract_zip_with_progress(payload, doc_html_dir, f"extract {docset}")
        elif config["kind"] == "chm":
            source_chm = config["chm"]
            if not source_chm.exists():
                raise FileNotFoundError(source_chm)
            extract_chm_with_progress(source_chm, doc_html_dir, f"extract {docset}", args.sevenzip)
        else:
            raise ValueError(f"Unsupported docset kind: {config['kind']}")

    print("\n== markdown ==")
    pages = discover_pages(html_root, args.output)
    by_help_id = {p.help_id: p for p in pages if p.help_id}
    for index, page in enumerate(pages, start=1):
        page.output.parent.mkdir(parents=True, exist_ok=True)
        page.output.write_text(markdown_for_page(page, by_help_id), encoding="utf-8")
        if index == len(pages) or index % 500 == 0:
            progress("convert markdown", index, len(pages))
    write_index(pages, args.output)
    print(f"\ndone: {len(pages)} markdown files under {args.output}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Markdown docs from local SOLIDWORKS API HelpViewer packages.")
    parser.add_argument("--output", type=Path, default=Path("docs"))
    parser.add_argument("--build-dir", type=Path, default=Path("build") / "sw_api_docs")
    parser.add_argument("--sevenzip", type=Path, default=None, help="Path to 7z.exe for extracting CHM files.")
    parser.add_argument(
        "--docsets",
        nargs="+",
        choices=sorted(DOCSETS),
        default=["sldworksapi", "swconst", "swdocmgrapi", "swcommands", "sldworksapiprogguide"],
    )
    parser.add_argument("--clean", action="store_true", help="Remove previous extracted files and docs before building.")
    return parser.parse_args()


if __name__ == "__main__":
    build(parse_args())

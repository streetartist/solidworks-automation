from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, Callable, Iterator

from .com import (
    call_member,
    call_or_value,
    double_array,
    empty_dispatch,
    empty_variant,
    import_pywin32,
    int_byref,
    member_value,
    unpack_out_call,
    variant_array,
    variant_byref,
)
from .constants import ConstraintType, EndCondition, MoveRollbackBarTo, RefPlaneConstraint, SaveAsOptions, SaveAsVersion, SelectType
from .errors import SolidWorksError
from .geometry import Point, flatten_points
from .units import deg


FeaturePredicate = Callable[[Any], bool]
SegmentPredicate = Callable[["SketchSegment"], bool]
ContourPredicate = Callable[["SketchContour"], bool]


@dataclass(frozen=True)
class SketchSegment:
    model: "ModelDoc"
    com: Any

    @property
    def type(self) -> int | None:
        try:
            return int(member_value(self.com, "GetType"))
        except Exception:
            return None

    @property
    def curve(self) -> Any | None:
        return member_value(self.com, "GetCurve", None)

    def select(self, *, append: bool = False, mark: int = 0, require: bool = True) -> bool:
        return self.model.select_object(self.com, append=append, mark=mark, require=require)

    def delete(self) -> None:
        self.model.clear_selection()
        self.select()
        self.model.delete_selected()

    def curve_params(self) -> list[float]:
        curve = self.curve
        if curve is None:
            return []
        for name in ("CircleParams", "LineParams", "EllipseParams"):
            try:
                value = member_value(curve, name, None)
            except Exception:
                value = None
            if value is not None:
                return [float(item) for item in list(value)]
        return []


class ModelDoc:
    def __init__(self, com: Any, app: Any | None = None) -> None:
        self.com = com
        self.app = app

    @property
    def title(self) -> str:
        return str(member_value(self.com, "GetTitle"))

    @property
    def extension(self) -> Any:
        return self.com.Extension

    @property
    def features(self) -> "FeatureTools":
        return FeatureTools(self)

    @property
    def sketch_manager(self) -> Any:
        return self.com.SketchManager

    @property
    def selection_manager(self) -> Any:
        return self.com.SelectionManager

    def create_select_data(self, *, mark: int = 0) -> Any:
        data = member_value(self.selection_manager, "CreateSelectData")
        data.Mark = int(mark)
        return data

    def set_contour_selection(self, enabled: bool = True) -> None:
        self.selection_manager.EnableContourSelection = bool(enabled)

    def active_sketch(self, *, require: bool = True) -> Any:
        sketch = getattr(self.sketch_manager, "ActiveSketch", None)
        sketch = call_or_value(sketch) if sketch is not None else None
        if sketch is None:
            sketch = member_value(self.com, "GetActiveSketch2", None)
        if sketch is None and require:
            raise SolidWorksError("No active sketch")
        return sketch

    def active_sketch_contours(self, *, require: bool = True) -> list["SketchContour"]:
        sketch = self.active_sketch(require=require)
        if sketch is None:
            return []
        return SketchContour.from_sketch(self, sketch)

    def activate(self) -> "ModelDoc":
        if self.app is None:
            raise SolidWorksError("Cannot activate document without a SolidWorks application wrapper")
        errors = int_byref()
        try:
            result = self.app.com.ActivateDoc3(self.title, False, 0, errors)
        except TypeError:
            result = self.app.com.ActivateDoc3(self.title, False, 0, 0)
        err = int(result[1]) if isinstance(result, tuple) and len(result) > 1 else int(getattr(errors, "value", 0) or 0)
        if err:
            raise SolidWorksError(f"Failed to activate document: {self.title}", errors=err)
        return self

    def rebuild(self) -> None:
        ok = call_member(self.com, "EditRebuild3", default=None)
        if ok is False:
            raise SolidWorksError(f"Failed to rebuild document: {self.title}")

    def clear_selection(self, notify: bool = True) -> None:
        call_member(self.com, "ClearSelection2", bool(notify))

    def delete_selected(self) -> Any:
        return call_member(self.com, "EditDelete", default=None)

    def suppress_selected(self) -> Any:
        return call_member(self.com, "EditSuppress2", default=None)

    def unsuppress_selected(self) -> Any:
        return call_member(self.com, "EditUnsuppress2", default=None)

    def edit_selected_sketch(self) -> Any:
        return call_member(self.com, "EditSketch", default=None)

    def force_rebuild(self, top_only: bool = False) -> Any:
        return call_member(self.com, "ForceRebuild3", bool(top_only), default=None)

    def select_by_id(
        self,
        name: str,
        object_type: str,
        *,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
        append: bool = False,
        mark: int = 0,
        callout: Any = None,
        options: int = 0,
        require: bool = True,
    ) -> bool:
        if callout is None:
            callout = empty_dispatch()
        selected = bool(self.extension.SelectByID2(name, object_type, x, y, z, append, mark, callout, options))
        if require and not selected:
            raise SolidWorksError(f"Failed to select {object_type}: {name}")
        return selected

    def select_by_ray(
        self,
        origin: Point | tuple[float, float, float],
        direction: Point | tuple[float, float, float],
        *,
        radius: float,
        select_type: int | SelectType,
        append: bool = False,
        mark: int = 0,
        options: int = 0,
        require: bool = True,
    ) -> bool:
        ox, oy, oz = _xyz(origin)
        dx, dy, dz = _xyz(direction)
        selected = bool(
            self.extension.SelectByRay(
                ox,
                oy,
                oz,
                dx,
                dy,
                dz,
                float(radius),
                int(select_type),
                bool(append),
                int(mark),
                int(options),
            )
        )
        if require and not selected:
            raise SolidWorksError(f"Failed to select entity by ray: type {int(select_type)}")
        return selected

    def select_face_by_ray(
        self,
        origin: Point | tuple[float, float, float],
        direction: Point | tuple[float, float, float],
        *,
        radius: float,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> bool:
        return self.select_by_ray(origin, direction, radius=radius, select_type=SelectType.Faces, append=append, mark=mark, require=require)

    def select_edge_by_ray(
        self,
        origin: Point | tuple[float, float, float],
        direction: Point | tuple[float, float, float],
        *,
        radius: float,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> bool:
        return self.select_by_ray(origin, direction, radius=radius, select_type=SelectType.Edges, append=append, mark=mark, require=require)

    def selected_object(self, index: int = 1, mark: int = -1, *, require: bool = True) -> Any:
        getter = getattr(self.selection_manager, "GetSelectedObject6", None)
        if not callable(getter):
            raise SolidWorksError("SelectionManager does not support GetSelectedObject6")
        obj = getter(int(index), int(mark))
        if obj is None and require:
            raise SolidWorksError(f"No selected object at index {index} with mark {mark}")
        return obj

    def select_plane(self, name: str, *, append: bool = False) -> bool:
        aliases = {
            "Top Plane": ("Top Plane", "上视基准面", "上基准面"),
            "Front Plane": ("Front Plane", "前视基准面", "前基准面"),
            "Right Plane": ("Right Plane", "右视基准面", "右基准面"),
        }
        for candidate in aliases.get(name, (name,)):
            if self.select_by_id(candidate, "PLANE", append=append, require=False):
                return True
        raise SolidWorksError(f"Failed to select PLANE: {name}")

    def select_feature(self, name: str, *, append: bool = False, mark: int = 0) -> bool:
        return self.select_by_id(name, "BODYFEATURE", append=append, mark=mark)

    def select_axis(self, name: str, *, append: bool = False, mark: int = 0) -> bool:
        return self.select_by_id(name, "AXIS", append=append, mark=mark)

    def select_sketch(self, name: str, *, append: bool = False, mark: int = 0) -> bool:
        return self.select_by_id(name, "SKETCH", append=append, mark=mark)

    def select_object(self, obj: Any, *, append: bool = False, mark: int = 0, require: bool = True) -> bool:
        select4 = getattr(obj, "Select4", None)
        if callable(select4):
            try:
                selected = bool(select4(bool(append), self.create_select_data(mark=mark)))
            except TypeError:
                selected = bool(select4(bool(append), None, int(mark)))
            if require and not selected:
                name = getattr(obj, "Name", repr(obj))
                raise SolidWorksError(f"Failed to select object: {name}")
            return selected
        select2 = getattr(obj, "Select2", None)
        if not callable(select2):
            raise SolidWorksError(f"Object does not support Select2: {obj!r}")
        selected = bool(select2(bool(append), int(mark)))
        if require and not selected:
            name = getattr(obj, "Name", repr(obj))
            raise SolidWorksError(f"Failed to select object: {name}")
        return selected

    def insert_axis_from_planes(self, plane_a: str, plane_b: str, *, name: str = "Reference Axis", auto_size: bool = True) -> Any:
        self.clear_selection()
        self.select_plane(plane_a)
        self.select_plane(plane_b, append=True)
        ok = bool(self.com.InsertAxis2(bool(auto_size)))
        if not ok:
            raise SolidWorksError(f"Failed to create reference axis from planes: {plane_a}, {plane_b}")
        feature = self.last_feature()
        feature.Name = name
        return feature

    def select_sketch_contours(
        self,
        contours: list["SketchContour"] | tuple["SketchContour", ...],
        *,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> int:
        self.set_contour_selection(True)
        selected = 0
        for index, contour in enumerate(contours):
            if contour.select(append=append or index > 0, mark=mark, require=require):
                selected += 1
        return selected

    def select_closed_sketch_contours(
        self,
        *,
        append: bool = False,
        mark: int = 0,
        min_segments: int = 0,
        require: bool = True,
    ) -> list["SketchContour"]:
        contours = [contour for contour in self.active_sketch_contours() if contour.is_closed and contour.segment_count >= min_segments]
        if require and not contours:
            raise SolidWorksError("No closed sketch contours found")
        self.select_sketch_contours(contours, append=append, mark=mark, require=require)
        return contours

    def select_matching_sketch_contours(
        self,
        predicate: ContourPredicate,
        *,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> list["SketchContour"]:
        contours = [contour for contour in self.active_sketch_contours() if predicate(contour)]
        if require and not contours:
            raise SolidWorksError("No matching sketch contours found")
        self.select_sketch_contours(contours, append=append, mark=mark, require=require)
        return contours

    def last_feature(self) -> Any:
        feature = call_member(self.com, "FeatureByPositionReverse", 0, default=None)
        if feature is None:
            raise SolidWorksError("No feature exists in the current document")
        return feature

    def iter_features(self) -> Iterator[Any]:
        feature = member_value(self.com, "FirstFeature", None)
        while feature is not None:
            yield feature
            feature = member_value(feature, "GetNextFeature", None)

    def feature_name(self, feature: Any) -> str:
        return str(member_value(feature, "Name", ""))

    def feature_type(self, feature: Any) -> str:
        return str(member_value(feature, "GetTypeName2", ""))

    def find_feature(
        self,
        predicate: FeaturePredicate,
        *,
        after: Any | None = None,
        require: bool = True,
    ) -> Any | None:
        found_after = after is None
        for feature in self.iter_features():
            if not found_after:
                if _same_com_object(feature, after):
                    found_after = True
                continue
            if predicate(feature):
                return feature
        if require:
            raise SolidWorksError("No matching feature found")
        return None

    def find_features_by_name(
        self,
        name: str,
        *,
        type_name: str | None = None,
        contains: bool = False,
        case_sensitive: bool = True,
        after: Any | None = None,
    ) -> list[Any]:
        needle = str(name)
        if not case_sensitive:
            needle = needle.casefold()

        def matches(feature: Any) -> bool:
            if type_name is not None and self.feature_type(feature) != type_name:
                return False
            candidate = self.feature_name(feature)
            haystack = candidate if case_sensitive else candidate.casefold()
            return needle in haystack if contains else haystack == needle

        found_after = after is None
        matches_list: list[Any] = []
        for feature in self.iter_features():
            if not found_after:
                if _same_com_object(feature, after):
                    found_after = True
                continue
            if matches(feature):
                matches_list.append(feature)
        return matches_list

    def find_feature_by_name(
        self,
        name: str,
        *,
        type_name: str | None = None,
        contains: bool = False,
        case_sensitive: bool = True,
        after: Any | None = None,
        require: bool = True,
    ) -> Any | None:
        matches = self.find_features_by_name(
            name,
            type_name=type_name,
            contains=contains,
            case_sensitive=case_sensitive,
            after=after,
        )
        if matches:
            return matches[0]
        if require:
            raise SolidWorksError(f"No feature found matching name: {name!r}")
        return None

    def find_features_by_name_pattern(
        self,
        pattern: str,
        *,
        type_name: str | None = None,
        flags: int = 0,
        after: Any | None = None,
    ) -> list[Any]:
        regex = re.compile(pattern, flags)
        found_after = after is None
        matches: list[Any] = []
        for feature in self.iter_features():
            if not found_after:
                if _same_com_object(feature, after):
                    found_after = True
                continue
            if type_name is not None and self.feature_type(feature) != type_name:
                continue
            if regex.search(self.feature_name(feature)):
                matches.append(feature)
        return matches

    def select_feature_object(
        self,
        feature: Any,
        *,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> bool:
        return self.select_object(feature, append=append, mark=mark, require=require)

    def select_feature_by_name(
        self,
        name: str,
        *,
        type_name: str | None = None,
        contains: bool = False,
        case_sensitive: bool = True,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> bool:
        feature = self.find_feature_by_name(
            name,
            type_name=type_name,
            contains=contains,
            case_sensitive=case_sensitive,
            require=require,
        )
        if feature is None:
            return False
        return self.select_feature_object(feature, append=append, mark=mark, require=require)

    def next_feature(
        self,
        feature: Any,
        *,
        type_name: str | None = None,
        require: bool = True,
    ) -> Any | None:
        return self.find_feature(
            lambda candidate: type_name is None or self.feature_type(candidate) == type_name,
            after=feature,
            require=require,
        )

    def feature_error_code(self, feature: Any) -> int:
        try:
            return int(call_member(feature, "GetErrorCode", default=0) or 0)
        except Exception:
            return 0

    def feature_errors(self) -> list[tuple[Any, int]]:
        errors: list[tuple[Any, int]] = []
        for feature in self.iter_features():
            error = self.feature_error_code(feature)
            if error:
                errors.append((feature, error))
        return errors

    @property
    def feature_manager(self) -> Any:
        return self.com.FeatureManager

    def rollback(
        self,
        location: int | MoveRollbackBarTo,
        feature: Any | str = "",
        *,
        require: bool = True,
    ) -> bool:
        name = feature if isinstance(feature, str) else self.feature_name(feature)
        ok = bool(call_member(self.feature_manager, "EditRollback", int(location), str(name), default=False))
        if require and not ok:
            raise SolidWorksError(f"Failed to move rollback bar to {int(location)} for feature {name!r}")
        return ok

    def rollback_before(self, feature: Any | str, *, require: bool = True) -> bool:
        return self.rollback(MoveRollbackBarTo.BeforeFeature, feature, require=require)

    def rollback_after(self, feature: Any | str, *, require: bool = True) -> bool:
        return self.rollback(MoveRollbackBarTo.AfterFeature, feature, require=require)

    def rollback_to_end(self, *, require: bool = True) -> bool:
        return self.rollback(MoveRollbackBarTo.End, "", require=require)

    def suppress_feature(self, feature: Any) -> Any:
        self.clear_selection()
        self.select_object(feature)
        return self.suppress_selected()

    def unsuppress_feature(self, feature: Any) -> Any:
        self.clear_selection()
        self.select_object(feature)
        return self.unsuppress_selected()

    def delete_feature(self, feature: Any) -> Any:
        self.clear_selection()
        self.select_object(feature)
        return self.delete_selected()

    def part_box(self, *, exact: bool = True) -> tuple[float, float, float, float, float, float]:
        box = call_member(self.com, "GetPartBox", bool(exact), default=None)
        if box is None:
            raise SolidWorksError("Active document does not expose GetPartBox")
        values = tuple(float(value) for value in list(box)[:6])
        if len(values) != 6:
            raise SolidWorksError("GetPartBox returned an invalid bounding box")
        return values

    def size(self, *, exact: bool = True) -> tuple[float, float, float]:
        xmin, ymin, zmin, xmax, ymax, zmax = self.part_box(exact=exact)
        return xmax - xmin, ymax - ymin, zmax - zmin

    def rename_last_feature(self, name: str) -> Any:
        feature = self.last_feature()
        feature.Name = name
        return feature

    @contextmanager
    def sketch(self) -> Iterator["SketchBuilder"]:
        self.sketch_manager.InsertSketch(True)
        try:
            yield SketchBuilder(self)
        finally:
            self.sketch_manager.InsertSketch(True)

    @contextmanager
    def sketch3d(self) -> Iterator["SketchBuilder"]:
        self.sketch_manager.Insert3DSketch(True)
        try:
            yield SketchBuilder(self)
        finally:
            self.sketch_manager.Insert3DSketch(True)

    @contextmanager
    def edit_sketch_feature(self, feature: Any) -> Iterator["SketchEditor"]:
        self.clear_selection()
        self.select_object(feature)
        self.edit_selected_sketch()
        try:
            yield SketchEditor(self, feature)
        finally:
            self.clear_selection()
            self.edit_selected_sketch()

    @contextmanager
    def replace_feature_at_history(
        self,
        old_feature: Any,
        *,
        delete_old_on_success: bool = False,
        rebuild: bool = True,
    ) -> Iterator[Any]:
        self.suppress_feature(old_feature)
        if rebuild:
            self.rebuild()
        self.rollback_before(old_feature)
        try:
            yield old_feature
            self.rollback_to_end()
            self.force_rebuild(False)
            self.rebuild()
            errors = self.feature_errors()
            if errors:
                details = ", ".join(f"{self.feature_name(feature)}={error}" for feature, error in errors)
                raise SolidWorksError(f"Feature replacement left rebuild errors: {details}")
            if delete_old_on_success:
                self.delete_feature(old_feature)
                self.force_rebuild(False)
                self.rebuild()
        except Exception:
            self.rollback_to_end(require=False)
            raise

    def save(self) -> None:
        errors = int_byref()
        warnings = int_byref()
        result = self.com.Save3(int(SaveAsOptions.Silent), errors, warnings)
        out = unpack_out_call(result, errors, warnings)
        if not bool(out.value):
            raise SolidWorksError(f"Failed to save document: {self.title}", errors=out.errors, warnings=out.warnings)

    def save_as(
        self,
        path: str | Path,
        *,
        version: int | SaveAsVersion = SaveAsVersion.CurrentVersion,
        options: int | SaveAsOptions = SaveAsOptions.Silent,
        export_data: Any = None,
        advanced_options: Any = None,
    ) -> None:
        path = Path(path).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        errors = int_byref()
        warnings = int_byref()
        if export_data is None:
            export_data = empty_dispatch()
        if advanced_options is None:
            advanced_options = empty_dispatch()
        if hasattr(self.extension, "SaveAs3"):
            result = self.extension.SaveAs3(str(path), int(version), int(options), export_data, advanced_options, errors, warnings)
        else:
            result = self.extension.SaveAs(str(path), int(version), int(options), export_data, errors, warnings)
        out = unpack_out_call(result, errors, warnings)
        if not bool(out.value):
            raise SolidWorksError(f"Failed to save document as: {path}", errors=out.errors, warnings=out.warnings)

    def export(self, path: str | Path, *, options: int | SaveAsOptions = SaveAsOptions.Silent) -> None:
        self.activate()
        self.clear_selection()
        self.save_as(path, options=options)

    def builder(self) -> Any:
        from .builders import PartBuilder

        return PartBuilder(self)


class SketchBuilder:
    def __init__(self, model: ModelDoc) -> None:
        self.model = model

    @property
    def com(self) -> Any:
        return self.model.sketch_manager

    def line(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> Any:
        return self.com.CreateLine(x1, y1, z1, x2, y2, z2)

    def centerline(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> Any:
        return self.com.CreateCenterLine(x1, y1, z1, x2, y2, z2)

    def corner_rectangle(self, x1: float, y1: float, x2: float, y2: float, *, z: float = 0.0) -> Any:
        return self.com.CreateCornerRectangle(x1, y1, z, x2, y2, z)

    def center_rectangle(self, cx: float, cy: float, corner_x: float, corner_y: float, *, z: float = 0.0) -> Any:
        return self.com.CreateCenterRectangle(cx, cy, z, corner_x, corner_y, z)

    def circle(self, cx: float, cy: float, radius: float, *, z: float = 0.0) -> Any:
        return self.com.CreateCircleByRadius(cx, cy, z, radius)

    def arc(self, cx: float, cy: float, sx: float, sy: float, ex: float, ey: float, *, z: float = 0.0, direction: int = 1) -> Any:
        return self.com.CreateArc(cx, cy, z, sx, sy, z, ex, ey, z, direction)

    def three_point_arc(self, sx: float, sy: float, ex: float, ey: float, mx: float, my: float, *, z: float = 0.0) -> Any:
        return self.com.Create3PointArc(sx, sy, z, ex, ey, z, mx, my, z)

    def ellipse(
        self,
        cx: float,
        cy: float,
        major_x: float,
        major_y: float,
        minor_x: float,
        minor_y: float,
        *,
        z: float = 0.0,
    ) -> Any:
        return self.com.CreateEllipse(cx, cy, z, major_x, major_y, z, minor_x, minor_y, z)

    def polygon(
        self,
        cx: float,
        cy: float,
        vertex_x: float,
        vertex_y: float,
        *,
        sides: int,
        inscribed: bool = True,
        z: float = 0.0,
    ) -> Any:
        return self.com.CreatePolygon(cx, cy, z, vertex_x, vertex_y, z, int(sides), bool(inscribed))

    def spline(self, points: list[Point | tuple[float, float] | tuple[float, float, float]], *, closed: bool = False) -> Any:
        data = double_array(flatten_points(points))
        create_spline3 = getattr(self.com, "CreateSpline3", None)
        if callable(create_spline3):
            status = variant_byref()
            segment = create_spline3(data, empty_variant(), empty_variant(), bool(closed), status)
            if segment is not None:
                return segment
        create_spline2 = getattr(self.com, "CreateSpline2", None)
        if callable(create_spline2):
            segment = create_spline2(data, bool(closed))
            if segment is not None:
                return segment
        create_spline = getattr(self.com, "CreateSpline", None)
        if callable(create_spline):
            segment = create_spline(data)
            if segment is not None:
                return segment
        raise SolidWorksError("Failed to create sketch spline")

    def equation_spline(
        self,
        x_expression: str,
        y_expression: str,
        *,
        z_expression: str = "",
        range_start: str,
        range_end: str,
        is_angle_range: bool = False,
        rotation_angle: float = 0.0,
        x_offset: float = 0.0,
        y_offset: float = 0.0,
        lock_start: bool = True,
        lock_end: bool = True,
    ) -> Any:
        create_equation_spline2 = getattr(self.com, "CreateEquationSpline2", None)
        if callable(create_equation_spline2):
            segment = create_equation_spline2(
                str(x_expression),
                str(y_expression),
                str(z_expression),
                str(range_start),
                str(range_end),
                bool(is_angle_range),
                float(rotation_angle),
                float(x_offset),
                float(y_offset),
                bool(lock_start),
                bool(lock_end),
            )
            if segment is not None:
                return segment
        create_equation_spline = getattr(self.com, "CreateEquationSpline", None)
        if callable(create_equation_spline) and not x_expression and not z_expression:
            segment = create_equation_spline(
                str(y_expression),
                str(range_start),
                str(range_end),
                bool(is_angle_range),
                float(rotation_angle),
                float(x_offset),
                float(y_offset),
                bool(lock_start),
                bool(lock_end),
            )
            if segment is not None:
                return segment
        raise SolidWorksError("Failed to create equation-driven sketch spline")

    def polyline(self, points: list[Point | tuple[float, float] | tuple[float, float, float]], *, close: bool = True) -> list[Any]:
        if len(points) < 2:
            raise ValueError("polyline requires at least two points")
        normalized = [p if isinstance(p, Point) else Point(float(p[0]), float(p[1]), float(p[2]) if len(p) > 2 else 0.0) for p in points]
        if close and normalized[0] != normalized[-1]:
            normalized.append(normalized[0])
        return [
            self.line(a.x, a.y, a.z, b.x, b.y, b.z)
            for a, b in zip(normalized, normalized[1:])
        ]

    @property
    def active_sketch(self) -> Any:
        return self.model.active_sketch()

    @property
    def relation_manager(self) -> Any:
        sketch = self.active_sketch
        manager = getattr(sketch, "RelationManager", None)
        if manager is None:
            raise SolidWorksError("Active sketch does not expose RelationManager")
        return manager

    def add_relation(self, entities: list[Any] | tuple[Any, ...], relation_type: int | ConstraintType) -> Any:
        if not entities:
            raise ValueError("add_relation requires at least one entity")
        constraint = ConstraintType(int(relation_type)) if int(relation_type) in _SKETCH_CONSTRAINT_NAMES else relation_type
        if constraint in _SKETCH_CONSTRAINT_NAMES:
            return self.add_constraint_to_selected_entities(entities, constraint)
        relation = self.relation_manager.AddRelation(variant_array(tuple(entities)), int(relation_type))
        if relation is None:
            raise SolidWorksError(f"Failed to add sketch relation: {int(relation_type)}")
        return relation

    def add_constraint_to_selected_entities(self, entities: list[Any] | tuple[Any, ...], relation_type: int | ConstraintType) -> None:
        constraint_name = _SKETCH_CONSTRAINT_NAMES.get(ConstraintType(int(relation_type)))
        if constraint_name is None:
            raise SolidWorksError(f"SketchAddConstraints does not support relation: {int(relation_type)}")
        self.model.clear_selection()
        for index, entity in enumerate(entities):
            self.model.select_object(entity, append=index > 0)
        self.model.com.SketchAddConstraints(constraint_name)
        self.model.clear_selection()

    def coincident(self, entity_a: Any, entity_b: Any) -> Any:
        return self.add_relation((entity_a, entity_b), ConstraintType.Coincident)

    def tangent(self, entity_a: Any, entity_b: Any) -> Any:
        return self.add_relation((entity_a, entity_b), ConstraintType.Tangent)

    def merge_points(self, point_a: Any, point_b: Any) -> Any:
        return self.add_relation((point_a, point_b), ConstraintType.MergePoints)

    def start_point(self, segment: Any) -> Any:
        return sketch_segment_endpoint(segment, start=True)

    def end_point(self, segment: Any) -> Any:
        return sketch_segment_endpoint(segment, start=False)

    def coincident_endpoints(self, segment_a: Any, segment_b: Any, *, a_start: bool = False, b_start: bool = True) -> Any:
        point_a = sketch_segment_endpoint(segment_a, start=a_start)
        point_b = sketch_segment_endpoint(segment_b, start=b_start)
        return self.coincident(point_a, point_b)

    def contours(self, *, require: bool = True) -> list["SketchContour"]:
        return self.model.active_sketch_contours(require=require)

    def select_closed_contours(self, *, append: bool = False, mark: int = 0, min_segments: int = 0) -> list["SketchContour"]:
        return self.model.select_closed_sketch_contours(append=append, mark=mark, min_segments=min_segments)


class SketchEditor:
    def __init__(self, model: ModelDoc, feature: Any) -> None:
        self.model = model
        self.feature = feature

    @property
    def com(self) -> Any:
        return self.model.active_sketch()

    def segments(self) -> list[SketchSegment]:
        return [
            SketchSegment(self.model, segment)
            for segment in _as_list(member_value(self.com, "GetSketchSegments", []))
        ]

    def matching_segments(self, predicate: SegmentPredicate) -> list[SketchSegment]:
        return [segment for segment in self.segments() if predicate(segment)]

    def delete_segments(self, predicate: SegmentPredicate) -> int:
        deleted = 0
        while True:
            matches = self.matching_segments(predicate)
            if not matches:
                return deleted
            matches[0].delete()
            deleted += 1

    def contours(self) -> list["SketchContour"]:
        return SketchContour.from_sketch(self.model, self.com)

    def matching_contours(self, predicate: ContourPredicate) -> list["SketchContour"]:
        return [contour for contour in self.contours() if predicate(contour)]

    def select_contours(
        self,
        contours: list["SketchContour"] | tuple["SketchContour", ...],
        *,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> int:
        return self.model.select_sketch_contours(contours, append=append, mark=mark, require=require)


class SketchContour:
    def __init__(self, model: ModelDoc, com: Any) -> None:
        self.model = model
        self.com = com

    @staticmethod
    def from_sketch(model: ModelDoc, sketch: Any) -> list["SketchContour"]:
        contours = _as_list(member_value(sketch, "GetSketchContours"))
        return [SketchContour(model, contour) for contour in contours if contour is not None]

    @property
    def is_closed(self) -> bool:
        return bool(member_value(self.com, "IsClosed"))

    @property
    def segment_count(self) -> int:
        get_count = getattr(self.com, "GetSketchSegmentsCount", None)
        if get_count is not None:
            return int(call_or_value(get_count))
        return len(self.segments)

    @property
    def segments(self) -> list[Any]:
        return _as_list(member_value(self.com, "GetSketchSegments"))

    @property
    def sketch_segments(self) -> list[SketchSegment]:
        return [SketchSegment(self.model, segment) for segment in self.segments]

    @property
    def edge_count(self) -> int:
        get_count = getattr(self.com, "GetEdgesCount", None)
        if get_count is not None:
            return int(call_or_value(get_count))
        return len(self.edges)

    @property
    def edges(self) -> list[Any]:
        get_edges = getattr(self.com, "GetEdges", None)
        return _as_list(call_or_value(get_edges)) if get_edges is not None else []

    def select(self, *, append: bool = False, mark: int = 0, require: bool = True) -> bool:
        self.model.set_contour_selection(True)
        try:
            selected = bool(call_member(self.com, "Select2", bool(append), self.model.create_select_data(mark=mark)))
        except TypeError:
            selected = bool(call_member(self.com, "Select2", bool(append), int(mark)))
        if require and not selected:
            raise SolidWorksError("Failed to select sketch contour")
        return selected

    def deselect(self) -> None:
        call_member(self.com, "DeSelect", default=None)


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    try:
        return list(value)
    except TypeError:
        return [value]


def _xyz(value: Point | tuple[float, float, float]) -> tuple[float, float, float]:
    if isinstance(value, Point):
        return value.x, value.y, value.z
    return float(value[0]), float(value[1]), float(value[2])


def _same_com_object(left: Any, right: Any) -> bool:
    if left is right:
        return True
    try:
        return bool(left == right)
    except Exception:
        return False


_SKETCH_CONSTRAINT_NAMES = {
    ConstraintType.Horizontal: "sgHORIZONTAL2D",
    ConstraintType.Vertical: "sgVERTICAL2D",
    ConstraintType.Tangent: "sgTANGENT",
    ConstraintType.Parallel: "sgPARALLEL",
    ConstraintType.Perpendicular: "sgPERPENDICULAR",
    ConstraintType.Coincident: "sgCOINCIDENT",
    ConstraintType.Concentric: "sgCONCENTRIC",
    ConstraintType.Symmetric: "sgSYMMETRIC",
    ConstraintType.AtMiddle: "sgATMIDDLE",
    ConstraintType.AtIntersect: "sgATINTERSECT",
    ConstraintType.SameLength: "sgSAMELENGTH",
    ConstraintType.Fixed: "sgFIXED",
    ConstraintType.Colinear: "sgCOLINEAR",
    ConstraintType.Coradial: "sgCORADIAL",
    ConstraintType.MergePoints: "sgMERGEPOINTS",
}


def sketch_segment_endpoint(segment: Any, *, start: bool) -> Any:
    segment = _specific_sketch_segment(segment)
    method_name = "GetStartPoint2" if start else "GetEndPoint2"
    getter = getattr(segment, method_name, None)
    if getter is not None:
        try:
            point = call_or_value(getter)
            if point is not None:
                return point
        except Exception:
            pass
    get_points = getattr(segment, "GetPoints2", None)
    if get_points is not None:
        try:
            points = _as_list(call_or_value(get_points))
            if points:
                return points[0] if start else points[-1]
        except Exception:
            pass
    raise SolidWorksError(f"Sketch segment does not expose {'start' if start else 'end'} point")


def _specific_sketch_segment(segment: Any) -> Any:
    _, win32com_client = import_pywin32()
    for interface_name in ("SketchLine", "SketchArc", "SketchSpline"):
        try:
            return win32com_client.CastTo(segment, interface_name)
        except Exception:
            continue
    return segment


class FeatureTools:
    def __init__(self, model: ModelDoc) -> None:
        self.model = model

    @property
    def com(self) -> Any:
        return self.model.com.FeatureManager

    def extrude_blind(
        self,
        depth: float,
        *,
        reverse: bool = False,
        merge: bool = True,
        thin_feature: bool = False,
        flip: bool = False,
    ) -> Any:
        feature = self.com.FeatureExtrusion3(
            bool(thin_feature),
            bool(flip),
            bool(reverse),
            int(EndCondition.Blind),
            int(EndCondition.Blind),
            float(depth),
            0.0,
            False,
            False,
            False,
            False,
            0.0,
            0.0,
            False,
            False,
            False,
            False,
            bool(merge),
            True,
            True,
            int(EndCondition.Blind),
            0.0,
            False,
        )
        if feature is None:
            raise SolidWorksError("Failed to create blind extrusion")
        return feature

    def extrude_midplane(self, depth: float, *, merge: bool = True, thin_feature: bool = False) -> Any:
        feature = self.com.FeatureExtrusion3(
            bool(thin_feature),
            False,
            False,
            int(EndCondition.MidPlane),
            int(EndCondition.Blind),
            float(depth),
            0.0,
            False,
            False,
            False,
            False,
            0.0,
            0.0,
            False,
            False,
            False,
            False,
            bool(merge),
            True,
            True,
            int(EndCondition.Blind),
            0.0,
            False,
        )
        if feature is None:
            raise SolidWorksError("Failed to create mid-plane extrusion")
        return feature

    def cut_blind(self, depth: float, *, reverse: bool = False, normal_cut: bool = False) -> Any:
        feature = self.com.FeatureCut4(
            False,
            False,
            bool(reverse),
            int(EndCondition.Blind),
            int(EndCondition.Blind),
            float(depth),
            0.0,
            False,
            False,
            False,
            False,
            0.0,
            0.0,
            False,
            False,
            False,
            False,
            bool(normal_cut),
            True,
            True,
            False,
            True,
            False,
            int(EndCondition.Blind),
            0.0,
            False,
            True,
        )
        if feature is None:
            raise SolidWorksError("Failed to create blind cut")
        return feature

    def cut_midplane(self, depth: float, *, normal_cut: bool = False) -> Any:
        feature = self.com.FeatureCut4(
            False,
            False,
            False,
            int(EndCondition.MidPlane),
            int(EndCondition.Blind),
            float(depth),
            0.0,
            False,
            False,
            False,
            False,
            0.0,
            0.0,
            False,
            False,
            False,
            False,
            bool(normal_cut),
            True,
            True,
            False,
            True,
            False,
            int(EndCondition.Blind),
            0.0,
            False,
            True,
        )
        if feature is None:
            raise SolidWorksError("Failed to create mid-plane cut")
        return feature

    def revolve(self, *, angle: float | None = None, cut: bool = False, reverse: bool = False, merge: bool = True) -> Any:
        feature = self.com.FeatureRevolve2(
            True,
            True,
            False,
            bool(cut),
            bool(reverse),
            False,
            int(EndCondition.Blind),
            int(EndCondition.Blind),
            float(angle if angle is not None else deg(360)),
            0.0,
            False,
            False,
            0.0,
            0.0,
            0,
            0.0,
            0.0,
            bool(merge),
            True,
            True,
        )
        if feature is None:
            raise SolidWorksError("Failed to create revolve feature")
        return feature

    def fillet_selected(self, radius: float, *, options: int = 0) -> Any:
        feature = self.com.FeatureFillet3(int(options), float(radius), 0.0, 0.0, 0, 0, 0, None, None, None, None, None, None, None)
        if feature is None:
            raise SolidWorksError("Failed to create fillet from selected entities")
        return feature

    def circular_pattern_selected(
        self,
        instances: int,
        angle: float = deg(360),
        *,
        flip_direction: bool = False,
        direction_dimension_name: str = "",
        geometry_pattern: bool = True,
        equal_spacing: bool = True,
        vary_instance: bool = False,
    ) -> Any:
        """Create a circular pattern from the current ordered selection.

        SOLIDWORKS expects the rotation axis selected with mark 1 and seed
        features selected with mark 4 before this call.
        """
        feature = self.com.FeatureCircularPattern4(
            int(instances),
            float(angle),
            bool(flip_direction),
            str(direction_dimension_name),
            bool(geometry_pattern),
            bool(equal_spacing),
            bool(vary_instance),
        )
        if feature is None:
            raise SolidWorksError("Failed to create circular pattern from selected entities")
        return feature

    def loft_boss(
        self,
        *,
        closed: bool = False,
        keep_tangency: bool = True,
        force_non_rational: bool = False,
        tess_tolerance_factor: float = 1.0,
        start_matching_type: int = 0,
        end_matching_type: int = 0,
        start_tangent_length: float = 0.0,
        end_tangent_length: float = 0.0,
        start_tangent_dir: bool = False,
        end_tangent_dir: bool = False,
        merge: bool = True,
        guide_curve_influence: int = 0,
    ) -> Any:
        feature = self.com.InsertProtrusionBlend2(
            bool(closed),
            bool(keep_tangency),
            bool(force_non_rational),
            float(tess_tolerance_factor),
            int(start_matching_type),
            int(end_matching_type),
            float(start_tangent_length),
            float(end_tangent_length),
            bool(start_tangent_dir),
            bool(end_tangent_dir),
            False,
            0.0,
            0.0,
            0,
            bool(merge),
            True,
            True,
            int(guide_curve_influence),
        )
        if feature is None:
            raise SolidWorksError("Failed to create loft boss")
        return feature

    def loft_surface(
        self,
        *,
        closed: bool = False,
        keep_tangency: bool = True,
        force_non_rational: bool = False,
        tess_tolerance_factor: float = 1.0,
        start_matching_type: int = 0,
        end_matching_type: int = 0,
    ) -> Any:
        self.model.com.InsertLoftRefSurface2(
            bool(closed),
            bool(keep_tangency),
            bool(force_non_rational),
            float(tess_tolerance_factor),
            int(start_matching_type),
            int(end_matching_type),
        )
        return self.model.last_feature()

    def thicken_selected(self, thickness: float, *, direction: int = 0, fill_volume: bool = False, merge: bool = True) -> Any:
        feature = self.com.FeatureBossThicken(float(thickness), int(direction), 0, bool(fill_volume), bool(merge), True, True)
        if feature is None:
            raise SolidWorksError("Failed to thicken selected surface")
        return feature

    def fill_surface_selected(self, *, resolution: int = 3) -> Any:
        feature = self.com.InsertFillSurface(int(resolution))
        if feature is None:
            raise SolidWorksError("Failed to create fill surface from selected boundary")
        return feature

    def knit_selected(
        self,
        *,
        try_to_form_solid: bool = True,
        merge_entities: bool = True,
        knit_tolerance: float = 0.00001,
        use_gap_filters: bool = False,
        max_gap: float = 0.0001,
    ) -> Any:
        feature = self.com.InsertSewRefSurface(
            bool(use_gap_filters),
            bool(try_to_form_solid),
            bool(merge_entities),
            float(knit_tolerance),
            float(max_gap),
        )
        if feature is None:
            raise SolidWorksError("Failed to knit selected surfaces")
        return feature

    def offset_plane(self, distance: float, *, flip: bool = False) -> Any:
        constraint = RefPlaneConstraint.Distance | (RefPlaneConstraint.OptionFlip if flip else RefPlaneConstraint.NONE)
        plane = self.com.InsertRefPlane(int(constraint), float(distance), 0, 0.0, 0, 0.0)
        if plane is None:
            raise SolidWorksError("Failed to create offset reference plane")
        return plane

    def call(self, name: str, *args: Any, require: bool = True) -> Any:
        result = getattr(self.com, name)(*args)
        if require and result is None:
            raise SolidWorksError(f"FeatureManager.{name} returned None")
        return result

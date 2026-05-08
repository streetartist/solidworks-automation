"""Ergonomic Python wrappers for the SOLIDWORKS COM API."""

from .app import SolidWorks, connect
from .builders import PartBuilder
from .constants import (
    AddComponentConfigOptions,
    AddMateError,
    ConstraintType,
    DocumentType,
    EndCondition,
    MateAlign,
    MateType,
    MoveRollbackBarTo,
    OpenDocOptions,
    PaperSize,
    RefPlaneConstraint,
    SaveAsOptions,
    SaveAsVersion,
    SelectType,
    SketchSegmentType,
    UserPreferenceStringValue,
    bitmask,
    document_type_from_path,
)
from .errors import SolidWorksError
from .geometry import Point, Vector
from .model import SketchContour, SketchEditor, SketchSegment
from .units import cm, deg, inch, mm

__all__ = [
    "SolidWorks",
    "SolidWorksError",
    "PartBuilder",
    "connect",
    "AddComponentConfigOptions",
    "AddMateError",
    "ConstraintType",
    "DocumentType",
    "EndCondition",
    "MateAlign",
    "MateType",
    "MoveRollbackBarTo",
    "OpenDocOptions",
    "PaperSize",
    "RefPlaneConstraint",
    "SaveAsOptions",
    "SaveAsVersion",
    "SelectType",
    "SketchSegmentType",
    "UserPreferenceStringValue",
    "bitmask",
    "document_type_from_path",
    "Point",
    "Vector",
    "SketchContour",
    "SketchEditor",
    "SketchSegment",
    "mm",
    "cm",
    "inch",
    "deg",
]

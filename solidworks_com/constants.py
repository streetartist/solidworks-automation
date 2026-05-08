from __future__ import annotations

from enum import IntEnum, IntFlag
from pathlib import Path


class DocumentType(IntEnum):
    NONE = 0
    PART = 1
    ASSEMBLY = 2
    DRAWING = 3
    SDM = 4
    LAYOUT = 5
    IMPORTED_PART = 6
    IMPORTED_ASSEMBLY = 7


class OpenDocOptions(IntFlag):
    NONE = 0
    Silent = 1
    ReadOnly = 2
    ViewOnly = 4
    RapidDraft = 8
    LoadModel = 16
    AutoMissingConfig = 32
    OverrideDefaultLoadLightweight = 64
    LoadLightweight = 128
    DontLoadHiddenComponents = 256
    LoadExternalReferencesInMemory = 512
    OpenDetailingMode = 1024
    LDR_EditAssembly = 2048
    SpeedPak = 4096
    AdvancedConfig = 8192


class SaveAsOptions(IntFlag):
    NONE = 0
    Silent = 1
    Copy = 2
    SaveReferenced = 4
    AvoidRebuildOnSave = 8
    UpdateInactiveViews = 16
    OverrideSaveEmodel = 32
    IgnoreBiography = 256
    CopyAndOpen = 512
    IncludeVirtualSubAsmComps = 1024
    ExportTo2DPdfFromInspection = 2048


class SaveAsVersion(IntEnum):
    CurrentVersion = 0
    StandardDrawing = 1
    DetachedDrawing = 3


class AddComponentConfigOptions(IntEnum):
    CurrentSelectedConfig = 0
    NewConfigWithAllReferenceModels = 1
    NewConfigWithAsmStructure = 2


class MateType(IntEnum):
    Coincident = 0
    Concentric = 1
    Perpendicular = 2
    Parallel = 3
    Tangent = 4
    Distance = 5
    Angle = 6
    Symmetric = 8
    Gear = 10
    Width = 11
    RackPinion = 13
    Lock = 16
    Screw = 17


class MateAlign(IntEnum):
    Aligned = 0
    AntiAligned = 1
    Closest = 2


class AddMateError(IntEnum):
    Unknown = 0
    NoError = 1
    IncorrectMateType = 2
    IncorrectAlignment = 3
    IncorrectSelections = 4
    OverDefinedAssembly = 5
    IncorrectGearRatios = 6


class EndCondition(IntEnum):
    Blind = 0
    ThroughAll = 1
    ThroughNext = 2
    UpToVertex = 3
    UpToSurface = 4
    OffsetFromSurface = 5
    MidPlane = 6
    UpToBody = 7


class ConstraintType(IntEnum):
    Distance = 1
    Angle = 2
    Radius = 3
    Horizontal = 4
    Vertical = 5
    Tangent = 6
    Parallel = 7
    Perpendicular = 8
    Coincident = 9
    Concentric = 10
    Symmetric = 11
    AtMiddle = 12
    AtIntersect = 13
    SameLength = 14
    Diameter = 15
    OffsetEdge = 16
    Fixed = 17
    Colinear = 27
    Coradial = 28
    MergePoints = 42
    EqualCurvature = 61
    EqualTangent = 62


class SketchSegmentType(IntEnum):
    Line = 0
    Arc = 1
    Ellipse = 2
    Spline = 3
    Text = 4
    Parabola = 5


class SelectType(IntEnum):
    Edges = 1
    Faces = 2
    DatumPlanes = 4
    DatumAxes = 5
    DatumPoints = 6
    Components = 20
    Mates = 21
    BodyFeatures = 22
    SketchSegments = 24
    SketchPoints = 25
    Everything = -3


class PaperSize(IntEnum):
    UserDefined = 12


class UserPreferenceStringValue(IntEnum):
    FileLocationsDocumentTemplates = 6
    DefaultTemplatePart = 8
    DefaultTemplateAssembly = 9
    DefaultTemplateDrawing = 10


class RefPlaneConstraint(IntFlag):
    NONE = 0
    Parallel = 1
    Perpendicular = 2
    Coincident = 4
    Distance = 8
    Angle = 16
    Tangent = 32
    Project = 64
    MidPlane = 128
    OptionFlip = 256
    OptionOriginOnCurve = 512
    OptionProjectToNearestLocation = 1028
    OptionProjectAlongSketchNormal = 2056
    ParallelToScreen = 4096
    OptionReferenceFlip = 8192


class MoveRollbackBarTo(IntEnum):
    End = 1
    PreviousPosition = 2
    BeforeFeature = 3
    AfterFeature = 4


_DOC_TYPES_BY_SUFFIX = {
    ".sldprt": DocumentType.PART,
    ".sldasm": DocumentType.ASSEMBLY,
    ".slddrw": DocumentType.DRAWING,
    ".sldlfp": DocumentType.PART,
    ".prt": DocumentType.PART,
    ".asm": DocumentType.ASSEMBLY,
    ".drw": DocumentType.DRAWING,
}


def bitmask(*flags: int | IntEnum | IntFlag) -> int:
    value = 0
    for flag in flags:
        value |= int(flag)
    return value


def document_type_from_path(path: str | Path) -> DocumentType:
    suffix = Path(path).suffix.lower()
    try:
        return _DOC_TYPES_BY_SUFFIX[suffix]
    except KeyError as exc:
        raise ValueError(f"Cannot infer SOLIDWORKS document type from extension: {suffix!r}") from exc

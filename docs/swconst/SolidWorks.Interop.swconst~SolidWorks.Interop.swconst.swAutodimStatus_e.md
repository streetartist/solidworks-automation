# swAutodimStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimStatus_e`

Statuses returned by ISketch::AutoDimension2 and IDrawingDoc::AutoDimension.
Statuses returned by [ISketch::AutoDimension2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("3670C9B8-86D0-4B6A-9417-DE7C88A4907E")>
Public Enum swAutodimStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAutodimStatus_e
```

```

[System.Runtime.InteropServices.Guid("3670C9B8-86D0-4B6A-9417-DE7C88A4907E")]
public enum swAutodimStatus_e : System.Enum 
```

```

public enum swAutodimStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3670C9B8-86D0-4B6A-9417-DE7C88A4907E")
public enum swAutodimStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3670C9B8-86D0-4B6A-9417-DE7C88A4907E")]
__value public enum swAutodimStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3670C9B8-86D0-4B6A-9417-DE7C88A4907E")]
public enum class swAutodimStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAutodimStatus3DSketchNotSupported** | 5 = Cannot autodimension a 3D sketch |
| **swAutodimStatusAlgorithmFailed** | 17 = Unspecified algorithm failure |
| **swAutodimStatusBadOptionValue** | 1 = An option value for an argument is out of range |
| **swAutodimStatusCenterlineNotAllowed** | 10 = The centerline scheme is not valid for sketches that cannot be revolved to create valid features |
| **swAutodimStatusDatumLineNotCenterline** | 14 = The datum must be a centerline for the centerline scheme |
| **swAutodimStatusDatumLineNotHorizontal** | 16 = If the sketch line is a datum, it must be horizontal for horizontal dimensions |
| **swAutodimStatusDatumLineNotVertical** | 15 = If the sketch line is a datum, it must be vertical for vertical dimension |
| **swAutodimStatusDatumNotSupplied** | 11 = No datum was selected for either the horizontal or vertical dimensioning schemes |
| **swAutodimStatusDatumNotUnique** | 12 = More than one datum was selected for either the horizontal or vertical dimensioning schemes |
| **swAutodimStatusDatumNotValidType** | 13 = One of the selected datums is not valid. Valid types are sketch points and sketch lines |
| **swAutodimStatusDocTypeNotSupported** | 3 = Only part and assemblies documents are supported |
| **swAutodimStatusEntitiesNotValid** | 9 = The entitiesToDimension argument has the value of [swAutodimEntitiesSelected](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimEntities_e.md), but the marked entities are not valid |
| **swAutodimStatusNoActiveDoc** | 2 = No active document |
| **swAutodimStatusNoActiveSketch** | 4 = Can only autodimension an active sketch |
| **swAutodimStatusNoEntities** | 8 = The entitiesToDimension argument has the value of [swAutodimEntitiesSelected](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimEntities_e.md), but no entities were selected and marked with the value [swAutodimMarkEntities](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimMark_e.md) |
| **swAutodimStatusSketchIsEmpty** | 6 = Cannot autodimension an empty sketch |
| **swAutodimStatusSketchIsOverDefined** | 7 = Cannot autodimension an over defined sketch |
| **swAutodimStatusSketchNoSolutionFound** | 18 = Cannot autodimension a sketch for which there is no solution |
| **swAutodimStatusSuccess** | 0 = Sketch successfully dimensioned |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAutodimStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

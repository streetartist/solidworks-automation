# swAutodimMark_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimMark_e`

Selection mark values. Bitmask.
Selection mark values. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("AE2040E4-E895-43CB-9C4C-C680B68C4E35")>
Public Enum swAutodimMark_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAutodimMark_e
```

```

[System.Runtime.InteropServices.Guid("AE2040E4-E895-43CB-9C4C-C680B68C4E35")]
public enum swAutodimMark_e : System.Enum 
```

```

public enum swAutodimMark_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("AE2040E4-E895-43CB-9C4C-C680B68C4E35")
public enum swAutodimMark_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("AE2040E4-E895-43CB-9C4C-C680B68C4E35")]
__value public enum swAutodimMark_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("AE2040E4-E895-43CB-9C4C-C680B68C4E35")]
public enum class swAutodimMark_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAutodimMarkEntities** | 1 or 0x1; Sketch entities to autodimension when [swAutodimEntitiesSelected](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimEntities_e.md) is passed as the entitiesToDimension argument to [ISketch::AutoDimension2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) |
| **swAutodimMarkHorizontalDatum** | 2 or 0x2; Sketch entities to autodimension when [swAutodimEntitiesSelected](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimEntities_e.md) is passed as the entitiesToDimension argument to [ISketch::AutoDimension2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) |
| **swAutodimMarkOriginDatum** | 8 or 0x8; Unique datum for the origin dimension scheme. Datum must be either a sketch point or a vertical sketch line. |
| **swAutodimMarkVerticalDatum** | 4 or 0x4; Unique datum for the horizontal dimension scheme; datum must be either a sketch point or a vertical sketch line |

Remarks

These values are passed by [IModelDocExtension::SelectByID2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/Solidworks.Interop.sldworks~Solidworks.Interop.sldworks.IModelDocExtension~SelectByID2.html).

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAutodimMark\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

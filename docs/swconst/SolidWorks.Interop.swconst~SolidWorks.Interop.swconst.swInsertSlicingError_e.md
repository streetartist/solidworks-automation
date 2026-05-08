# swInsertSlicingError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertSlicingError_e`

Error codes for slicing insertion. Bitmask.
Error codes for slicing insertion. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("6C734AE8-3F3B-44D5-BD92-B144B0A215F7")>
Public Enum swInsertSlicingError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInsertSlicingError_e
```

```

[System.Runtime.InteropServices.Guid("6C734AE8-3F3B-44D5-BD92-B144B0A215F7")]
public enum swInsertSlicingError_e : System.Enum 
```

```

public enum swInsertSlicingError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6C734AE8-3F3B-44D5-BD92-B144B0A215F7")
public enum swInsertSlicingError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6C734AE8-3F3B-44D5-BD92-B144B0A215F7")]
__value public enum swInsertSlicingError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6C734AE8-3F3B-44D5-BD92-B144B0A215F7")]
public enum class swInsertSlicingError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swInsertSlicingError\_EntitiesCannotFormPlane** | 0x10 = Point and provided line overlap |
| **swInsertSlicingError\_GenericError** | 0x1 = Slicing inserted successfully |
| **swInsertSlicingError\_InvalidNumberOfPlanes** | 0x80 = Number of planes must be <= 100 |
| **swInsertSlicingError\_InvalidSlicesToGenerateOption** | 0x4 = Slicing method specified in [ISlicingData::SlicesToGenerate](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SlicesToGenerate.html) is not valid |
| **swInsertSlicingError\_InvalidSlicingData** | 0x40 = Null or invalid slicing data |
| **swInsertSlicingError\_InvalidSlicingPlaneEntities** | 0x8 = None or invalid type of entities specified |
| **swInsertSlicingError\_InvalidTotalAngle** | 0x2 = ([ISlicingData::NumberOfPlanes](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~NumberOfPlanes.html) \* [ISlicingData::Offset](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~Offset.html)) is invalid |
| **swInsertSlicingError\_NoBodiesInsideBox** | 0x20 = No bodies are inside the bounding box |
| **swInsertSlicingError\_NoError** | 0x0 = Slicing inserted successfully |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInsertSlicingError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

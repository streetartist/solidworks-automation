# swSurfaceFinishSymbolOrientation_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSurfaceFinishSymbolOrientation_e`

Surface finish symbol orientations.
Surface finish symbol orientations.

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

<System.Runtime.InteropServices.GuidAttribute("37BA1C7B-248F-4789-A9C5-73FEAD5FDF3F")>
Public Enum swSurfaceFinishSymbolOrientation_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSurfaceFinishSymbolOrientation_e
```

```

[System.Runtime.InteropServices.Guid("37BA1C7B-248F-4789-A9C5-73FEAD5FDF3F")]
public enum swSurfaceFinishSymbolOrientation_e : System.Enum 
```

```

public enum swSurfaceFinishSymbolOrientation_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("37BA1C7B-248F-4789-A9C5-73FEAD5FDF3F")
public enum swSurfaceFinishSymbolOrientation_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("37BA1C7B-248F-4789-A9C5-73FEAD5FDF3F")]
__value public enum swSurfaceFinishSymbolOrientation_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("37BA1C7B-248F-4789-A9C5-73FEAD5FDF3F")]
public enum class swSurfaceFinishSymbolOrientation_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSFOrientation\_Perpendicular** | 3 = Symbol is displayed at the same angle as the attached entity |
| **swSFOrientation\_PerpendicularFlipped** | 4 = Symbol is displayed at the same angle as the attached entity, but the symbol is flipped to the other side of the entity |
| **swSFOrientation\_Rotated90** | 2 = Symbol is displayed vertical (rotated 90 clockwise) |
| **swSFOrientation\_Upright** | 1 = Symbol is displayed horizontal |
| **swSFOrientation\_UserDefined** | 5 = Symbol is displayed at a user-specified angle |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSurfaceFinishSymbolOrientation\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

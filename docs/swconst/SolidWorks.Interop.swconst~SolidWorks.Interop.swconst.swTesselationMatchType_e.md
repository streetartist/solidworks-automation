# swTesselationMatchType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTesselationMatchType_e`

Tessellation match types.
Tessellation match types.

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

<System.Runtime.InteropServices.GuidAttribute("5AC149B6-2515-4895-9421-1CE2C25E04C3")>
Public Enum swTesselationMatchType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTesselationMatchType_e
```

```

[System.Runtime.InteropServices.Guid("5AC149B6-2515-4895-9421-1CE2C25E04C3")]
public enum swTesselationMatchType_e : System.Enum 
```

```

public enum swTesselationMatchType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("5AC149B6-2515-4895-9421-1CE2C25E04C3")
public enum swTesselationMatchType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("5AC149B6-2515-4895-9421-1CE2C25E04C3")]
__value public enum swTesselationMatchType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("5AC149B6-2515-4895-9421-1CE2C25E04C3")]
public enum class swTesselationMatchType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swTesselationMatchEdgeCurve** | 2 = Clipping facet boundaries to model edge curves |
| **swTesselationMatchFacetGeometry** | 1 = Clipping facet boundaries to a common edge |
| **swTesselationMatchFacetTopology** | 0 = Matching facet vertices across a common edge |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTesselationMatchType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

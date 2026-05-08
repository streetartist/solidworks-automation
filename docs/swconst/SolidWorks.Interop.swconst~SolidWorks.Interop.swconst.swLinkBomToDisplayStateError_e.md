# swLinkBomToDisplayStateError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLinkBomToDisplayStateError_e`

Errors when linking a BOM to a Display State.
Errors when linking a BOM to a Display State.

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

<System.Runtime.InteropServices.GuidAttribute("D99B9117-AB9E-404E-A0AB-661417EDEB07")>
Public Enum swLinkBomToDisplayStateError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLinkBomToDisplayStateError_e
```

```

[System.Runtime.InteropServices.Guid("D99B9117-AB9E-404E-A0AB-661417EDEB07")]
public enum swLinkBomToDisplayStateError_e : System.Enum 
```

```

public enum swLinkBomToDisplayStateError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D99B9117-AB9E-404E-A0AB-661417EDEB07")
public enum swLinkBomToDisplayStateError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D99B9117-AB9E-404E-A0AB-661417EDEB07")]
__value public enum swLinkBomToDisplayStateError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D99B9117-AB9E-404E-A0AB-661417EDEB07")]
public enum class swLinkBomToDisplayStateError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swLinkBomToDisplayState\_InvalidDisplayState** | 1 |
| **swLinkBomToDisplayState\_MultipleConfigurations** | 2 |
| **swLinkBomToDisplayState\_Success** | 0 |

Remarks

This enumeration is used in IBomFeature::GetLinkToDisplayState and IBomFeature::SetLinkToDisplayState.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLinkBomToDisplayStateError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

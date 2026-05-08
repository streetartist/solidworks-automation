# swCreateOrdDimError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateOrdDimError_e`

Errors when inserting an ordinate dimension.
Errors when inserting an ordinate dimension.

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

<System.Runtime.InteropServices.GuidAttribute("C5167D55-425F-4099-89BF-A5F5405E3D51")>
Public Enum swCreateOrdDimError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCreateOrdDimError_e
```

```

[System.Runtime.InteropServices.Guid("C5167D55-425F-4099-89BF-A5F5405E3D51")]
public enum swCreateOrdDimError_e : System.Enum 
```

```

public enum swCreateOrdDimError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C5167D55-425F-4099-89BF-A5F5405E3D51")
public enum swCreateOrdDimError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C5167D55-425F-4099-89BF-A5F5405E3D51")]
__value public enum swCreateOrdDimError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C5167D55-425F-4099-89BF-A5F5405E3D51")]
public enum class swCreateOrdDimError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCreateOrdDimErr\_GenBadSel** | 3 |
| **swCreateOrdDimErr\_GenExtraSelection** | 6 |
| **swCreateOrdDimErr\_GenFailure** | 7 |
| **swCreateOrdDimErr\_GenNeedModelLoaded** | 4 |
| **swCreateOrdDimErr\_GenNoInternalDims** | 2 |
| **swCreateOrdDimErr\_GenSamePartOnly** | 5 |
| **swCreateOrdDimErr\_OrdBadDir** | 9 |
| **swCreateOrdDimErr\_OrdDupInGroup** | 8 |
| **swCreateOrdDimErr\_OrdFailure** | 1 |
| **swCreateOrdDimErr\_Success** | 0 |
| **swCreateOrdDimErr\_Undefined** | -1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCreateOrdDimError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

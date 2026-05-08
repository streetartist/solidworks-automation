# swChamferType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChamferType_e`

Chamfer types.
Chamfer types.

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

<System.Runtime.InteropServices.GuidAttribute("6C0DC3EE-D080-42AC-896F-E497C7E1E825")>
Public Enum swChamferType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swChamferType_e
```

```

[System.Runtime.InteropServices.Guid("6C0DC3EE-D080-42AC-896F-E497C7E1E825")]
public enum swChamferType_e : System.Enum 
```

```

public enum swChamferType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6C0DC3EE-D080-42AC-896F-E497C7E1E825")
public enum swChamferType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6C0DC3EE-D080-42AC-896F-E497C7E1E825")]
__value public enum swChamferType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6C0DC3EE-D080-42AC-896F-E497C7E1E825")]
public enum class swChamferType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swChamferAngleDistance** | 1 |
| **swChamferDistanceDistance** | 2 |
| **swChamferEqualDistance** | 16 |
| **swChamferVertex** | 3 |

Remarks

These values can be bitwise OR'd to get the desired chamfer type.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swChamferType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

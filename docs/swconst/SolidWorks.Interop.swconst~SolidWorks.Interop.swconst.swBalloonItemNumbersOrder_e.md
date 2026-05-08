# swBalloonItemNumbersOrder_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBalloonItemNumbersOrder_e`

Balloon item ordering options. Bitmask.
Balloon item ordering options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("C621FA4E-D7E8-4F55-9E88-7C9F3451405B")>
Public Enum swBalloonItemNumbersOrder_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBalloonItemNumbersOrder_e
```

```

[System.Runtime.InteropServices.Guid("C621FA4E-D7E8-4F55-9E88-7C9F3451405B")]
public enum swBalloonItemNumbersOrder_e : System.Enum 
```

```

public enum swBalloonItemNumbersOrder_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C621FA4E-D7E8-4F55-9E88-7C9F3451405B")
public enum swBalloonItemNumbersOrder_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C621FA4E-D7E8-4F55-9E88-7C9F3451405B")]
__value public enum swBalloonItemNumbersOrder_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C621FA4E-D7E8-4F55-9E88-7C9F3451405B")]
public enum class swBalloonItemNumbersOrder_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBalloonItemNumbers\_DoNotChangeItemNumbers** | 0x1 or 1 |
| **swBalloonItemNumbers\_FollowAssemblyOrder** | 0x2 or 2 |
| **swBalloonItemNumbers\_NotApplicable** | -1 |
| **swBalloonItemNumbers\_OrderSequentially** | 0x4 or 4 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBalloonItemNumbersOrder\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

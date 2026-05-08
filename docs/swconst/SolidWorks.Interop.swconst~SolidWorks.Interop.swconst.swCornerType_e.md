# swCornerType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerType_e`

Structure system corner types.
Structure system corner types.

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

<System.Runtime.InteropServices.GuidAttribute("0CC09EF4-646F-4F49-9117-10AB76C3C06D")>
Public Enum swCornerType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCornerType_e
```

```

[System.Runtime.InteropServices.Guid("0CC09EF4-646F-4F49-9117-10AB76C3C06D")]
public enum swCornerType_e : System.Enum 
```

```

public enum swCornerType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0CC09EF4-646F-4F49-9117-10AB76C3C06D")
public enum swCornerType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0CC09EF4-646F-4F49-9117-10AB76C3C06D")]
__value public enum swCornerType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0CC09EF4-646F-4F49-9117-10AB76C3C06D")]
public enum class swCornerType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCorner\_Complex** | 2 = Three or more members intersect with several trim options |
| **swCorner\_Simple** | 0 = Two members intersect with two trim options |
| **swCorner\_TwoMember** | 1 = Two members intersect with three trim options |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCornerType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

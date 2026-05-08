# swReplaceComponentError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReplaceComponentError_e`

Replace component errors.
Replace component errors.

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

<System.Runtime.InteropServices.GuidAttribute("8DDA70EC-D3FD-43C8-9B94-CB844BC0A0F6")>
Public Enum swReplaceComponentError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swReplaceComponentError_e
```

```

[System.Runtime.InteropServices.Guid("8DDA70EC-D3FD-43C8-9B94-CB844BC0A0F6")]
public enum swReplaceComponentError_e : System.Enum 
```

```

public enum swReplaceComponentError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8DDA70EC-D3FD-43C8-9B94-CB844BC0A0F6")
public enum swReplaceComponentError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8DDA70EC-D3FD-43C8-9B94-CB844BC0A0F6")]
__value public enum swReplaceComponentError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8DDA70EC-D3FD-43C8-9B94-CB844BC0A0F6")]
public enum class swReplaceComponentError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swReplaceComponent\_EmptyName** | 2 |
| **swReplaceComponent\_InvalidFileName** | 3 |
| **swReplaceComponent\_NotTopLevelComponent** | 6 |
| **swReplaceComponent\_SameFile** | 5 |
| **swReplaceComponent\_SameModelDifferentPath** | 4 |
| **swReplaceComponent\_Success** | 1 |
| **swReplaceComponent\_Undefined** | 0 |
| **swReplaceComponent\_UnknownError** | 7 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swReplaceComponentError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

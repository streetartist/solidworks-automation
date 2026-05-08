# swCreateAngRunDimError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateAngRunDimError_e`

Statuses when inserting an angular running dimension.
Statuses when inserting an angular running dimension.

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

<System.Runtime.InteropServices.GuidAttribute("2C17418D-6EF7-4FD1-AAD0-54EF39261356")>
Public Enum swCreateAngRunDimError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCreateAngRunDimError_e
```

```

[System.Runtime.InteropServices.Guid("2C17418D-6EF7-4FD1-AAD0-54EF39261356")]
public enum swCreateAngRunDimError_e : System.Enum 
```

```

public enum swCreateAngRunDimError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2C17418D-6EF7-4FD1-AAD0-54EF39261356")
public enum swCreateAngRunDimError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2C17418D-6EF7-4FD1-AAD0-54EF39261356")]
__value public enum swCreateAngRunDimError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2C17418D-6EF7-4FD1-AAD0-54EF39261356")]
public enum class swCreateAngRunDimError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCreateAngRunDimError\_GenFailure** | 0 = Cannot create this angular running dimension |
| **swCreateAngRunDimError\_IdenticalDimension** | 2 = Identical dimensions cannot be created in the same angular running dimension |
| **swCreateAngRunDimError\_SelectAnotherEntity** | 3 = Cannot use the selected entity to create this angular running dimension; select another entity |
| **swCreateAngRunDimError\_Success** | 1 |
| **swCreateAngRunDimError\_Undefined** | -1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCreateAngRunDimError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

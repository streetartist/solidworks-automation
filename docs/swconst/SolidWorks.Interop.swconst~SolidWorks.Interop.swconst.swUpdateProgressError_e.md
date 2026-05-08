# swUpdateProgressError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUpdateProgressError_e`

User progress errors.
User progress errors.

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

<System.Runtime.InteropServices.GuidAttribute("70C4B9B6-BD6E-4A5E-AA2B-A6FCE499F58A")>
Public Enum swUpdateProgressError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swUpdateProgressError_e
```

```

[System.Runtime.InteropServices.Guid("70C4B9B6-BD6E-4A5E-AA2B-A6FCE499F58A")]
public enum swUpdateProgressError_e : System.Enum 
```

```

public enum swUpdateProgressError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("70C4B9B6-BD6E-4A5E-AA2B-A6FCE499F58A")
public enum swUpdateProgressError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("70C4B9B6-BD6E-4A5E-AA2B-A6FCE499F58A")]
__value public enum swUpdateProgressError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("70C4B9B6-BD6E-4A5E-AA2B-A6FCE499F58A")]
public enum class swUpdateProgressError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swUpdateProgressError\_NotInitialized** | 4 |
| **swUpdateProgressError\_OutOfBounds** | 3 |
| **swUpdateProgressError\_Success** | 1 |
| **swUpdateProgressError\_UnknownError** | 0 |
| **swUpdateProgressError\_UserCancel** | 2 = User pressed the Esc key to cancel the progress indicator |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swUpdateProgressError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

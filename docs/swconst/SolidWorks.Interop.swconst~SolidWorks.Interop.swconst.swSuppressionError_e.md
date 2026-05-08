# swSuppressionError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSuppressionError_e`

Suppression errors.
Suppression errors.

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

<System.Runtime.InteropServices.GuidAttribute("237D715A-D4FE-4438-80AA-A6B937BA5D23")>
Public Enum swSuppressionError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSuppressionError_e
```

```

[System.Runtime.InteropServices.Guid("237D715A-D4FE-4438-80AA-A6B937BA5D23")]
public enum swSuppressionError_e : System.Enum 
```

```

public enum swSuppressionError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("237D715A-D4FE-4438-80AA-A6B937BA5D23")
public enum swSuppressionError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("237D715A-D4FE-4438-80AA-A6B937BA5D23")]
__value public enum swSuppressionError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("237D715A-D4FE-4438-80AA-A6B937BA5D23")]
public enum class swSuppressionError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSuppressionBadComponent** | 0 = Component object is no longer valid; for example, if a configuration changed |
| **swSuppressionBadState** | 1 = Invalid state was specified |
| **swSuppressionChangeFailed** | 3 = Change failed, even though the arguments were okay |
| **swSuppressionChangeOk** | 2 = State was changed |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSuppressionError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

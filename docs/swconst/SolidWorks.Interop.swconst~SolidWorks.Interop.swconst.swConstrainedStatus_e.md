# swConstrainedStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConstrainedStatus_e`

Status of sketch constraints.
Status of sketch constraints.

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

<System.Runtime.InteropServices.GuidAttribute("CCB930F4-D194-4C29-BD6A-E2FCE43DFF8A")>
Public Enum swConstrainedStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConstrainedStatus_e
```

```

[System.Runtime.InteropServices.Guid("CCB930F4-D194-4C29-BD6A-E2FCE43DFF8A")]
public enum swConstrainedStatus_e : System.Enum 
```

```

public enum swConstrainedStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CCB930F4-D194-4C29-BD6A-E2FCE43DFF8A")
public enum swConstrainedStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CCB930F4-D194-4C29-BD6A-E2FCE43DFF8A")]
__value public enum swConstrainedStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CCB930F4-D194-4C29-BD6A-E2FCE43DFF8A")]
public enum class swConstrainedStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAutosolveOff** | 7 |
| **swFullyConstrained** | 3 |
| **swInvalidSolution** | 6 |
| **swNoSolution** | 5 |
| **swOverConstrained** | 4 |
| **swUnderConstrained** | 2 |
| **swUnknownConstraint** | 1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConstrainedStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

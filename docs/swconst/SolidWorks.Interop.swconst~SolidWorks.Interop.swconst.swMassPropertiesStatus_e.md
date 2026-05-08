# swMassPropertiesStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMassPropertiesStatus_e`

Mass property result codes.
Mass property result codes.

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

<System.Runtime.InteropServices.GuidAttribute("69F2494B-5A65-4B83-8B5C-2DAD99A14578")>
Public Enum swMassPropertiesStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMassPropertiesStatus_e
```

```

[System.Runtime.InteropServices.Guid("69F2494B-5A65-4B83-8B5C-2DAD99A14578")]
public enum swMassPropertiesStatus_e : System.Enum 
```

```

public enum swMassPropertiesStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("69F2494B-5A65-4B83-8B5C-2DAD99A14578")
public enum swMassPropertiesStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("69F2494B-5A65-4B83-8B5C-2DAD99A14578")]
__value public enum swMassPropertiesStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("69F2494B-5A65-4B83-8B5C-2DAD99A14578")]
public enum class swMassPropertiesStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMassPropertiesStatus\_NoBody** | 2 = Mass properties calculation failed because there is no body in the model |
| **swMassPropertiesStatus\_OK** | 0 = Mass properties calculation successful |
| **swMassPropertiesStatus\_UnknownError** | 1 = Mass properties calculation failed for an unknown reason |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMassPropertiesStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

# swCheckOutOfDate_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckOutOfDate_e`

Check for out-of-date lightweight components options.
Check for out-of-date lightweight components options.

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

<System.Runtime.InteropServices.GuidAttribute("CFFD955A-B5C3-4629-B954-993D8A5913AF")>
Public Enum swCheckOutOfDate_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCheckOutOfDate_e
```

```

[System.Runtime.InteropServices.Guid("CFFD955A-B5C3-4629-B954-993D8A5913AF")]
public enum swCheckOutOfDate_e : System.Enum 
```

```

public enum swCheckOutOfDate_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CFFD955A-B5C3-4629-B954-993D8A5913AF")
public enum swCheckOutOfDate_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CFFD955A-B5C3-4629-B954-993D8A5913AF")]
__value public enum swCheckOutOfDate_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CFFD955A-B5C3-4629-B954-993D8A5913AF")]
public enum class swCheckOutOfDate_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCheckOutOfDate\_AlwaysResolve** | Resolve out-of-date components; other lightweight components are not resolved |
| **swCheckOutOfDate\_DoNotCheck** | Do not check |
| **swCheckOutOfDate\_Indicate** | Mark out-of-date components with a broken feather; good lightweight models are not marked with the broken feather; instead, they are marked with the regular feather |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCheckOutOfDate\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

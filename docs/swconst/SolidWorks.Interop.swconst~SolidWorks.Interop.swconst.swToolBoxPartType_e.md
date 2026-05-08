# swToolBoxPartType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swToolBoxPartType_e`

Toolbox part types. Bitmask.
Toolbox part types. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("8895AE39-207E-4677-B51D-C2EBCFF44D67")>
Public Enum swToolBoxPartType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swToolBoxPartType_e
```

```

[System.Runtime.InteropServices.Guid("8895AE39-207E-4677-B51D-C2EBCFF44D67")]
public enum swToolBoxPartType_e : System.Enum 
```

```

public enum swToolBoxPartType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8895AE39-207E-4677-B51D-C2EBCFF44D67")
public enum swToolBoxPartType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8895AE39-207E-4677-B51D-C2EBCFF44D67")]
__value public enum swToolBoxPartType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8895AE39-207E-4677-B51D-C2EBCFF44D67")]
public enum class swToolBoxPartType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swNotAToolboxPart** | 0x0 = Not a Toolbox part |
| **swToolboxCopiedPart** | 0x2 = Copied part |
| **swToolboxStandardPart** | 0x1 = Standard part |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swToolBoxPartType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

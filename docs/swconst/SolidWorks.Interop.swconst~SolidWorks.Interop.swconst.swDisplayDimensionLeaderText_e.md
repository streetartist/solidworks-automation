# swDisplayDimensionLeaderText_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayDimensionLeaderText_e`

Display dimension leaders and text placement.
Display dimension leaders and text placement.

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

<System.Runtime.InteropServices.GuidAttribute("2E496EF8-E31D-49EB-BEDD-36998316865C")>
Public Enum swDisplayDimensionLeaderText_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDisplayDimensionLeaderText_e
```

```

[System.Runtime.InteropServices.Guid("2E496EF8-E31D-49EB-BEDD-36998316865C")]
public enum swDisplayDimensionLeaderText_e : System.Enum 
```

```

public enum swDisplayDimensionLeaderText_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2E496EF8-E31D-49EB-BEDD-36998316865C")
public enum swDisplayDimensionLeaderText_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2E496EF8-E31D-49EB-BEDD-36998316865C")]
__value public enum swDisplayDimensionLeaderText_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2E496EF8-E31D-49EB-BEDD-36998316865C")]
public enum class swDisplayDimensionLeaderText_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBrokenLeaderAlignedText** | 3 = Leader is broken and the text is aligned with the leader |
| **swBrokenLeaderHorizontalText** | 2 = Leader is broken and the text is horizontal |
| **swSolidLeaderAlignedText** | 1 = Leader is solid (not broken) and the text is aligned with the leader |
| **swSolidLeaderHorizontalText** | 4 = The leader is solid and the text is horizontal; although this value can be applied to any type of dimension where the dimension text is not between the extension lines, it is currently only implemented by SOLIDWORKS for chamfer dimensions |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDisplayDimensionLeaderText\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

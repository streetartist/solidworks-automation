# swSketchFullyDefineRelationType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchFullyDefineRelationType_e`

Fully defined sketch relations. Bitmask.
Fully defined sketch relations. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("FC7F5EE0-9CC1-4261-9FE6-8F4703C00F0B")>
Public Enum swSketchFullyDefineRelationType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSketchFullyDefineRelationType_e
```

```

[System.Runtime.InteropServices.Guid("FC7F5EE0-9CC1-4261-9FE6-8F4703C00F0B")]
public enum swSketchFullyDefineRelationType_e : System.Enum 
```

```

public enum swSketchFullyDefineRelationType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("FC7F5EE0-9CC1-4261-9FE6-8F4703C00F0B")
public enum swSketchFullyDefineRelationType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("FC7F5EE0-9CC1-4261-9FE6-8F4703C00F0B")]
__value public enum swSketchFullyDefineRelationType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("FC7F5EE0-9CC1-4261-9FE6-8F4703C00F0B")]
public enum class swSketchFullyDefineRelationType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSketchFullyDefineRelationType\_Coincident** | 512 or 0x200 |
| **swSketchFullyDefineRelationType\_Colinear** | 32 or 0x20 |
| **swSketchFullyDefineRelationType\_Concentric** | 64 or 0x40 |
| **swSketchFullyDefineRelationType\_Equal** | 1 or 0x1 |
| **swSketchFullyDefineRelationType\_Horizontal** | 2 or 0x2 |
| **swSketchFullyDefineRelationType\_Midpoint** | 256 or 0x100 |
| **swSketchFullyDefineRelationType\_Parallel** | 128 or 0x80 |
| **swSketchFullyDefineRelationType\_Perpendicular** | 16 or 0x10 |
| **swSketchFullyDefineRelationType\_Tangent** | 8 or 0x8 |
| **swSketchFullyDefineRelationType\_Vertical** | 4 or 0x4 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSketchFullyDefineRelationType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

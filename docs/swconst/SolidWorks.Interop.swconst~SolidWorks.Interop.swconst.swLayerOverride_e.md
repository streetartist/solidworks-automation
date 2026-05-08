# swLayerOverride_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLayerOverride_e`

Layer override types. Bitmask.
Layer override types. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("6A55A95E-775B-4B23-98A4-43906AD43B37")>
Public Enum swLayerOverride_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLayerOverride_e
```

```

[System.Runtime.InteropServices.Guid("6A55A95E-775B-4B23-98A4-43906AD43B37")]
public enum swLayerOverride_e : System.Enum 
```

```

public enum swLayerOverride_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6A55A95E-775B-4B23-98A4-43906AD43B37")
public enum swLayerOverride_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6A55A95E-775B-4B23-98A4-43906AD43B37")]
__value public enum swLayerOverride_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6A55A95E-775B-4B23-98A4-43906AD43B37")]
public enum class swLayerOverride_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swLayerOverrideColor** | 1 or 0x1 |
| **swLayerOverrideNone** | 0 or 0x0 |
| **swLayerOverrideStyle** | 2 or 0x2 |
| **swLayerOverrideWidth** | 4 or 0x4 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLayerOverride\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

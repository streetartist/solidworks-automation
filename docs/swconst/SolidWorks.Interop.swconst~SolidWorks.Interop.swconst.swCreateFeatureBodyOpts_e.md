# swCreateFeatureBodyOpts_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateFeatureBodyOpts_e`

Options for creating bodies. Bitmask.
Options for creating bodies. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("21D9896E-EDE1-4DBC-B52D-7D846B659202")>
Public Enum swCreateFeatureBodyOpts_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCreateFeatureBodyOpts_e
```

```

[System.Runtime.InteropServices.Guid("21D9896E-EDE1-4DBC-B52D-7D846B659202")]
public enum swCreateFeatureBodyOpts_e : System.Enum 
```

```

public enum swCreateFeatureBodyOpts_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("21D9896E-EDE1-4DBC-B52D-7D846B659202")
public enum swCreateFeatureBodyOpts_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("21D9896E-EDE1-4DBC-B52D-7D846B659202")]
__value public enum swCreateFeatureBodyOpts_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("21D9896E-EDE1-4DBC-B52D-7D846B659202")]
public enum class swCreateFeatureBodyOpts_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCreateFeatureBodyCheck** | 1 or 0x1; Check body |
| **swCreateFeatureBodySimplify** | 2 or 0x2; Simplify body |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCreateFeatureBodyOpts\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

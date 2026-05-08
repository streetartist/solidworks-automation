# swRoutingComponentGroupingOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRoutingComponentGroupingOption_e`

Routing components grouping options. Bitmask.
Routing components grouping options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("A6F66AF2-2E08-406A-8588-90281257E9F4")>
Public Enum swRoutingComponentGroupingOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRoutingComponentGroupingOption_e
```

```

[System.Runtime.InteropServices.Guid("A6F66AF2-2E08-406A-8588-90281257E9F4")]
public enum swRoutingComponentGroupingOption_e : System.Enum 
```

```

public enum swRoutingComponentGroupingOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A6F66AF2-2E08-406A-8588-90281257E9F4")
public enum swRoutingComponentGroupingOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A6F66AF2-2E08-406A-8588-90281257E9F4")]
__value public enum swRoutingComponentGroupingOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A6F66AF2-2E08-406A-8588-90281257E9F4")]
public enum class swRoutingComponentGroupingOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDisplayUnitsInBOM** | 4 or 0x4 |
| **swGroupPipesOrTubesWithTheSameDiameterAndSchedule** | 2 or 0x2 |
| **swRoutingGroupSpoolComponents** | 8 or 0x8 |
| **swShowOnlyRoutingComponentsInBOM** | 1 or 0x1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRoutingComponentGroupingOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

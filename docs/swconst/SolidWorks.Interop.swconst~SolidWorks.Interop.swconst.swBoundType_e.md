# swBoundType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundType_e`

Boundary behaviors at the start and end of UV parameter ranges.
Boundary behaviors at the start and end of UV parameter ranges.

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

<System.Runtime.InteropServices.GuidAttribute("8D005900-E3AD-40E8-98B6-8B29DE939952")>
Public Enum swBoundType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBoundType_e
```

```

[System.Runtime.InteropServices.Guid("8D005900-E3AD-40E8-98B6-8B29DE939952")]
public enum swBoundType_e : System.Enum 
```

```

public enum swBoundType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8D005900-E3AD-40E8-98B6-8B29DE939952")
public enum swBoundType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8D005900-E3AD-40E8-98B6-8B29DE939952")]
__value public enum swBoundType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8D005900-E3AD-40E8-98B6-8B29DE939952")]
public enum class swBoundType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBoundType\_Degenerate** | 13741 (**see Remarks**) |
| **swBoundType\_Extendable** | 13734 |
| **swBoundType\_Infinite** | 13733 |
| **swBoundType\_NotExtendable** | 13735 |
| **swBoundType\_Periodic** | 13701 |
| **swBoundType\_PeriodicNotDifferentiable** | 13736 = Not continuously differentiable across the boundary. |

Remarks

If the behavior at the start of the U range is Degenerate', then the V parameter is degenerate when U = urange[0]'. The derivative of the parameterization function with respect to v is 0 whenever u = urange[0]', for all values of v, and the parameter curve corresponding to u = urange[0]' degenerates to a single point. A parameterization can only degenerate at the end of its range, unless the surface is a B-spline surface.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBoundType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

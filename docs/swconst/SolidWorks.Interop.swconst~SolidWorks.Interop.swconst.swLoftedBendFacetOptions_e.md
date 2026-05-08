# swLoftedBendFacetOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoftedBendFacetOptions_e`

Faceting options for lofted bend facet features.
Faceting options for lofted bend facet features.

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

<System.Runtime.InteropServices.GuidAttribute("A1D37B79-CF02-484B-8D04-4827DE1A1647")>
Public Enum swLoftedBendFacetOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLoftedBendFacetOptions_e
```

```

[System.Runtime.InteropServices.Guid("A1D37B79-CF02-484B-8D04-4827DE1A1647")]
public enum swLoftedBendFacetOptions_e : System.Enum 
```

```

public enum swLoftedBendFacetOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A1D37B79-CF02-484B-8D04-4827DE1A1647")
public enum swLoftedBendFacetOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A1D37B79-CF02-484B-8D04-4827DE1A1647")]
__value public enum swLoftedBendFacetOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A1D37B79-CF02-484B-8D04-4827DE1A1647")]
public enum class swLoftedBendFacetOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAngleBetweenSegments** | 3 = Facet by maximum angle between adjacent linear segments |
| **swBendsPerTransitionSegment** | 1 = Facet by maximum number of bends per transition segment |
| **swChordTolerance** | 0 = Facet by maximum distance between the arc and linear segment of a chord on the lofted bend |
| **swMaxSegmentLength** | 2 = Facet by maximum length of a linear segment |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLoftedBendFacetOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

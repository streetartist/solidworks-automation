# swRefPlaneReferenceConstraints_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRefPlaneReferenceConstraints_e`

Reference plane constraints. Bitmask.
Reference plane constraints. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("2A006D5A-8953-4DB0-AEC5-CF76E08E1604")>
Public Enum swRefPlaneReferenceConstraints_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRefPlaneReferenceConstraints_e
```

```

[System.Runtime.InteropServices.Guid("2A006D5A-8953-4DB0-AEC5-CF76E08E1604")]
public enum swRefPlaneReferenceConstraints_e : System.Enum 
```

```

public enum swRefPlaneReferenceConstraints_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2A006D5A-8953-4DB0-AEC5-CF76E08E1604")
public enum swRefPlaneReferenceConstraints_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2A006D5A-8953-4DB0-AEC5-CF76E08E1604")]
__value public enum swRefPlaneReferenceConstraints_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2A006D5A-8953-4DB0-AEC5-CF76E08E1604")]
public enum class swRefPlaneReferenceConstraints_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRefPlaneReferenceConstraint\_Angle** | 16 or 0x10 |
| **swRefPlaneReferenceConstraint\_Coincident** | 4 or 0x4 |
| **swRefPlaneReferenceConstraint\_Distance** | 8 or 0x8 |
| **swRefPlaneReferenceConstraint\_MidPlane** | 128 or 0x80 |
| **swRefPlaneReferenceConstraint\_OptionFlip** | 256 or 0x100 |
| **swRefPlaneReferenceConstraint\_OptionOriginOnCurve** | 512 or 0x200 |
| **swRefPlaneReferenceConstraint\_OptionProjectAlongSketchNormal** | 2056 or 0x800 |
| **swRefPlaneReferenceConstraint\_OptionProjectToNearestLocation** | 1028 or 0x400 |
| **swRefPlaneReferenceConstraint\_OptionReferenceFlip** | 8192 or 0x2000 |
| **swRefPlaneReferenceConstraint\_Parallel** | 1 or 0x1 |
| **swRefPlaneReferenceConstraint\_ParallelToScreen** | 4096 or 0x1000 |
| **swRefPlaneReferenceConstraint\_Perpendicular** | 2 or 0x2 |
| **swRefPlaneReferenceConstraint\_Project** | 64 or 0x40 |
| **swRefPlaneReferenceConstraint\_Tangent** | 32 or 0x20 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRefPlaneReferenceConstraints\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

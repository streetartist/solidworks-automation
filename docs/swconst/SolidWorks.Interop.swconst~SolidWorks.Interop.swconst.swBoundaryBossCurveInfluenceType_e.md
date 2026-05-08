# swBoundaryBossCurveInfluenceType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossCurveInfluenceType_e`

Boundary feature curve influence types. Bitmask.
Boundary feature curve influence types. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("6226AE1F-F5AD-4E2C-8A9B-112C298F4F13")>
Public Enum swBoundaryBossCurveInfluenceType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBoundaryBossCurveInfluenceType_e
```

```

[System.Runtime.InteropServices.Guid("6226AE1F-F5AD-4E2C-8A9B-112C298F4F13")]
public enum swBoundaryBossCurveInfluenceType_e : System.Enum 
```

```

public enum swBoundaryBossCurveInfluenceType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6226AE1F-F5AD-4E2C-8A9B-112C298F4F13")
public enum swBoundaryBossCurveInfluenceType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6226AE1F-F5AD-4E2C-8A9B-112C298F4F13")]
__value public enum swBoundaryBossCurveInfluenceType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6226AE1F-F5AD-4E2C-8A9B-112C298F4F13")]
public enum class swBoundaryBossCurveInfluenceType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBoundaryBossCurve\_GlobalInfluence** | 32 or 0x20 |
| **swBoundaryBossCurve\_LinearInfluence** | 144 or 0x90 |
| **swBoundaryBossCurve\_ToEdgeInfluence** | 64 or 0x40 |
| **swBoundaryBossCurve\_ToNextCurveInfluence** | 0 or 0x0 |
| **swBoundaryBossCurve\_ToNextSharpInfluence** | 16 or 0x10 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBoundaryBossCurveInfluenceType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

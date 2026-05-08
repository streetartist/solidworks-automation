# swDraftAnalysisShow_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDraftAnalysisShow_e`

Show draft analsyis options. Bitmask.
Show draft analsyis options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("F21E9F2C-18C2-4E6B-AF79-3E24D0E331A8")>
Public Enum swDraftAnalysisShow_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDraftAnalysisShow_e
```

```

[System.Runtime.InteropServices.Guid("F21E9F2C-18C2-4E6B-AF79-3E24D0E331A8")]
public enum swDraftAnalysisShow_e : System.Enum 
```

```

public enum swDraftAnalysisShow_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F21E9F2C-18C2-4E6B-AF79-3E24D0E331A8")
public enum swDraftAnalysisShow_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F21E9F2C-18C2-4E6B-AF79-3E24D0E331A8")]
__value public enum swDraftAnalysisShow_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F21E9F2C-18C2-4E6B-AF79-3E24D0E331A8")]
public enum class swDraftAnalysisShow_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDraftAnalysisShowDraftRequired** | 4 or 0x4 |
| **swDraftAnalysisShowNegative** | 2 or 0x2 |
| **swDraftAnalysisShowNegativeSteep** | 32 or 0x20 |
| **swDraftAnalysisShowPositive** | 1 or 0x1 |
| **swDraftAnalysisShowPositiveSteep** | 16 or 0x10 |
| **swDraftAnalysisShowStraddle** | 8 or 0x8 |
| **swDraftAnalysisShowSurface** | 64 or 0x40 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDraftAnalysisShow\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

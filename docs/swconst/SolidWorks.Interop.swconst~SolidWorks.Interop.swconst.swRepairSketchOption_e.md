# swRepairSketchOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRepairSketchOption_e`

Options for repairing sketches. Bitmask.
Options for repairing sketches. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("C88127C7-4DAA-45B5-BDE2-528BCE8D778E")>
Public Enum swRepairSketchOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRepairSketchOption_e
```

```

[System.Runtime.InteropServices.Guid("C88127C7-4DAA-45B5-BDE2-528BCE8D778E")]
public enum swRepairSketchOption_e : System.Enum 
```

```

public enum swRepairSketchOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("C88127C7-4DAA-45B5-BDE2-528BCE8D778E")
public enum swRepairSketchOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("C88127C7-4DAA-45B5-BDE2-528BCE8D778E")]
__value public enum swRepairSketchOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("C88127C7-4DAA-45B5-BDE2-528BCE8D778E")]
public enum class swRepairSketchOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRepairSketchBreakIntersection** | 8 = Break intersection |
| **swRepairSketchCleanup** | 0 = Clean up |
| **swRepairSketchCloseGaps** | 4 = Close gaps |
| **swRepairSketchMergeSegment** | 2 = Merge segment |
| **swRepairSketchZeroSegment** | 1 = Zero segment |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRepairSketchOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

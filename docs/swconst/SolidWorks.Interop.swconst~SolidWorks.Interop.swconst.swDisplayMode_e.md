# swDisplayMode_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayMode_e`

Display modes of drawing views.
Display modes of drawing views.

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

<System.Runtime.InteropServices.GuidAttribute("CD17A96F-EED6-4A76-8875-65DA058B7D20")>
Public Enum swDisplayMode_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDisplayMode_e
```

```

[System.Runtime.InteropServices.Guid("CD17A96F-EED6-4A76-8875-65DA058B7D20")]
public enum swDisplayMode_e : System.Enum 
```

```

public enum swDisplayMode_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CD17A96F-EED6-4A76-8875-65DA058B7D20")
public enum swDisplayMode_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CD17A96F-EED6-4A76-8875-65DA058B7D20")]
__value public enum swDisplayMode_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CD17A96F-EED6-4A76-8875-65DA058B7D20")]
public enum class swDisplayMode_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDisplayModeDEFAULT** | 8 |
| **swDisplayModeUNKNOWN** | -1 |
| **swFACETED\_HIDDEN** | 6 |
| **swFACETED\_HIDDEN\_GREYED** | 5 |
| **swFACETED\_WIREFRAME** | 4 |
| **swHIDDEN** | 2; Hidden Lines Removed (HLR) |
| **swHIDDEN\_GREYED** | 1; Hidden Lines Visible (HLV) |
| **swSHADED** | 3 |
| **swSHADED\_EDGES** | 7 |
| **swWIREFRAME** | 0 |

Remarks

A faceted display mode is draft quality.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDisplayMode\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

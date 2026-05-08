# swCloseReopenOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCloseReopenOption_e`

File close and reopen options. Bitmask.
File close and reopen options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("025E2010-9D00-417F-8232-9B32FE1BDB2E")>
Public Enum swCloseReopenOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCloseReopenOption_e
```

```

[System.Runtime.InteropServices.Guid("025E2010-9D00-417F-8232-9B32FE1BDB2E")]
public enum swCloseReopenOption_e : System.Enum 
```

```

public enum swCloseReopenOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("025E2010-9D00-417F-8232-9B32FE1BDB2E")
public enum swCloseReopenOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("025E2010-9D00-417F-8232-9B32FE1BDB2E")]
__value public enum swCloseReopenOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("025E2010-9D00-417F-8232-9B32FE1BDB2E")]
public enum class swCloseReopenOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCloseReopenOption\_DiscardChanges** | 2 or 0x2; include this option to discard any changes to the document before reopening it; if you exclude this option and there are changes, [ISldWorks::CloseAndReopen](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CloseAndReopen.html) fails and returns [swCloseReopenError\_e.swCloseReopenModifiedError](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCloseReopenError_e.md) |
| **swCloseReopenOption\_ExitDetailingMode** | 8 or 0x8; include this option to reopen model drawings as resolved; if excluded by ISldWorks::CloseAndReopen2, keeps a model drawing in detailing mode on reopen |
| **swCloseReopenOption\_MatchSheet** | 4 or 0x4; include this option to open the same sheet that was active during closing |
| **swCloseReopenOption\_ReadOnly** | 1 or 0x1; include this option to open the drawing document in read-only mode |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCloseReopenOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

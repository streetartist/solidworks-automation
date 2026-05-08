# swPrintSelectionScaleFactor_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrintSelectionScaleFactor_e`

Drawing print selection scale options.
Drawing print selection scale options.

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

<System.Runtime.InteropServices.GuidAttribute("0D6738AA-18DE-4858-B84B-BABDB0BBC950")>
Public Enum swPrintSelectionScaleFactor_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPrintSelectionScaleFactor_e
```

```

[System.Runtime.InteropServices.Guid("0D6738AA-18DE-4858-B84B-BABDB0BBC950")]
public enum swPrintSelectionScaleFactor_e : System.Enum 
```

```

public enum swPrintSelectionScaleFactor_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0D6738AA-18DE-4858-B84B-BABDB0BBC950")
public enum swPrintSelectionScaleFactor_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0D6738AA-18DE-4858-B84B-BABDB0BBC950")]
__value public enum swPrintSelectionScaleFactor_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0D6738AA-18DE-4858-B84B-BABDB0BBC950")]
public enum class swPrintSelectionScaleFactor_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPrintAll** | 0 |
| **swPrintCurrentSheet** | 1; Print the current drawing sheet with a 1:1 scale |
| **swPrintScreenImage** | 2 |
| **swPrintSelection** | 3; Specify custom scale factors for the current drawing sheet |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPrintSelectionScaleFactor\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

# swBalloonFit_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBalloonFit_e`

Types of balloon and label location fits.
Types of balloon and label location fits.

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

<System.Runtime.InteropServices.GuidAttribute("1D47F505-0A54-421D-818C-D607DC1D9B11")>
Public Enum swBalloonFit_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBalloonFit_e
```

```

[System.Runtime.InteropServices.Guid("1D47F505-0A54-421D-818C-D607DC1D9B11")]
public enum swBalloonFit_e : System.Enum 
```

```

public enum swBalloonFit_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1D47F505-0A54-421D-818C-D607DC1D9B11")
public enum swBalloonFit_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1D47F505-0A54-421D-818C-D607DC1D9B11")]
__value public enum swBalloonFit_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1D47F505-0A54-421D-818C-D607DC1D9B11")]
public enum class swBalloonFit_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBF\_1Char** | 1 |
| **swBF\_2Chars** | 2 |
| **swBF\_3Chars** | 3 |
| **swBF\_4Chars** | 4 |
| **swBF\_5Chars** | 5 |
| **swBF\_Tightest** | 0; Not available for a label location |
| **swBF\_UserDef** | 6; Can use for label location selection **Custom Size** |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBalloonFit\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

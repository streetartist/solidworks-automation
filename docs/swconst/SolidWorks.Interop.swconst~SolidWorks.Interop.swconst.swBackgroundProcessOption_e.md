# swBackgroundProcessOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBackgroundProcessOption_e`

Background processing options.
Background processing options.

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

<System.Runtime.InteropServices.GuidAttribute("CAB36875-5B3B-493C-8604-159B67A6D0C0")>
Public Enum swBackgroundProcessOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBackgroundProcessOption_e
```

```

[System.Runtime.InteropServices.Guid("CAB36875-5B3B-493C-8604-159B67A6D0C0")]
public enum swBackgroundProcessOption_e : System.Enum 
```

```

public enum swBackgroundProcessOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CAB36875-5B3B-493C-8604-159B67A6D0C0")
public enum swBackgroundProcessOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CAB36875-5B3B-493C-8604-159B67A6D0C0")]
__value public enum swBackgroundProcessOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CAB36875-5B3B-493C-8604-159B67A6D0C0")]
public enum class swBackgroundProcessOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBackgroundProcessing\_DeferToApplication** | 2 = Defer to [ISldWorks::EnableBackgroundProcessing](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.html) setting |
| **swBackgroundProcessing\_Disabled** | 0 |
| **swBackgroundProcessing\_Enabled** | 1 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBackgroundProcessOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

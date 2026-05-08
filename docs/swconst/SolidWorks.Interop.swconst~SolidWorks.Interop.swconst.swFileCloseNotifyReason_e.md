# swFileCloseNotifyReason_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileCloseNotifyReason_e`

Reasons for the FileCloseNotify event.
Reasons for the [FileCloseNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler.html) event.

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

<System.Runtime.InteropServices.GuidAttribute("80BE9AE1-6FF4-4883-9261-44587162432A")>
Public Enum swFileCloseNotifyReason_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFileCloseNotifyReason_e
```

```

[System.Runtime.InteropServices.Guid("80BE9AE1-6FF4-4883-9261-44587162432A")]
public enum swFileCloseNotifyReason_e : System.Enum 
```

```

public enum swFileCloseNotifyReason_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("80BE9AE1-6FF4-4883-9261-44587162432A")
public enum swFileCloseNotifyReason_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("80BE9AE1-6FF4-4883-9261-44587162432A")]
__value public enum swFileCloseNotifyReason_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("80BE9AE1-6FF4-4883-9261-44587162432A")]
public enum class swFileCloseNotifyReason_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFileCloseNotifyReason\_CloseForReload** | 1 = [ISldWorks::CloseAndReopen](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CloseAndReopen.html) was called |
| **swFileCloseNotifyReason\_Unknown** | 0 = unknown reason |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFileCloseNotifyReason\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

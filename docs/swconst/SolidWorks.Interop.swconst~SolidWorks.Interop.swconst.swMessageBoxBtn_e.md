# swMessageBoxBtn_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMessageBoxBtn_e`

Message box control buttons.
Message box control buttons.

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

<System.Runtime.InteropServices.GuidAttribute("75A20839-2665-40FD-82B7-E6C11A5D97EB")>
Public Enum swMessageBoxBtn_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMessageBoxBtn_e
```

```

[System.Runtime.InteropServices.Guid("75A20839-2665-40FD-82B7-E6C11A5D97EB")]
public enum swMessageBoxBtn_e : System.Enum 
```

```

public enum swMessageBoxBtn_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("75A20839-2665-40FD-82B7-E6C11A5D97EB")
public enum swMessageBoxBtn_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("75A20839-2665-40FD-82B7-E6C11A5D97EB")]
__value public enum swMessageBoxBtn_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("75A20839-2665-40FD-82B7-E6C11A5D97EB")]
public enum class swMessageBoxBtn_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMbAbortRetryIgnore** | 1 = The message box contains three push buttons: Abort, Retry, and Ignore |
| **swMbOk** | 2 = The message box contains one button, OK |
| **swMbOkCancel** | 3 = The message box contains two push buttons: OK and Cancel |
| **swMbRetryCancel** | 4 = The message box contains two push buttons: Retry and Cancel |
| **swMbYesNo** | 5 = The message box contains two push buttons: Yes and No |
| **swMbYesNoCancel** | 6 = The message box contains three push buttons: Yes, No, and Cancel |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMessageBoxBtn\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

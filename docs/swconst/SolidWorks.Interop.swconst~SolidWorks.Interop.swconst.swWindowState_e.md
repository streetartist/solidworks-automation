# swWindowState_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWindowState_e`

Window states.
Window states.

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

<System.Runtime.InteropServices.GuidAttribute("A5FA80AD-2096-41A2-B9C6-6AC5D7BB7C18")>
Public Enum swWindowState_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swWindowState_e
```

```

[System.Runtime.InteropServices.Guid("A5FA80AD-2096-41A2-B9C6-6AC5D7BB7C18")]
public enum swWindowState_e : System.Enum 
```

```

public enum swWindowState_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A5FA80AD-2096-41A2-B9C6-6AC5D7BB7C18")
public enum swWindowState_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A5FA80AD-2096-41A2-B9C6-6AC5D7BB7C18")]
__value public enum swWindowState_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A5FA80AD-2096-41A2-B9C6-6AC5D7BB7C18")]
public enum class swWindowState_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swWindowMaximized** | 1 = The window fills the whole client area |
| **swWindowMinimized** | 2 = The window is represented by an icon only |
| **swWindowNormal** | 0 = The window is displayed in its normal state |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swWindowState\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

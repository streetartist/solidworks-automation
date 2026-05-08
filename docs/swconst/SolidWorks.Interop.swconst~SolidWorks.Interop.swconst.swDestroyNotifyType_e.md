# swDestroyNotifyType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDestroyNotifyType_e`

Options for when destroying model views.
Options for when destroying model views.

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

<System.Runtime.InteropServices.GuidAttribute("D2DDA52F-5472-41A6-9EFD-88BD5A1DC337")>
Public Enum swDestroyNotifyType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDestroyNotifyType_e
```

```

[System.Runtime.InteropServices.Guid("D2DDA52F-5472-41A6-9EFD-88BD5A1DC337")]
public enum swDestroyNotifyType_e : System.Enum 
```

```

public enum swDestroyNotifyType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D2DDA52F-5472-41A6-9EFD-88BD5A1DC337")
public enum swDestroyNotifyType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D2DDA52F-5472-41A6-9EFD-88BD5A1DC337")]
__value public enum swDestroyNotifyType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D2DDA52F-5472-41A6-9EFD-88BD5A1DC337")]
public enum class swDestroyNotifyType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDestroyNotifyDestroy** | 0 = View is being destroyed |
| **swDestroyNotifyHidden** | 1 = View is being hidden, not destroyed |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDestroyNotifyType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

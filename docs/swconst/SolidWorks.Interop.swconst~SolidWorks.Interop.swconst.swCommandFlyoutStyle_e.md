# swCommandFlyoutStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCommandFlyoutStyle_e`

Types of FlyoutGroup.
Types of FlyoutGroup.

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

<System.Runtime.InteropServices.GuidAttribute("B33A8523-7EFD-4B8C-AD0D-4BA9EB8B9F21")>
Public Enum swCommandFlyoutStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCommandFlyoutStyle_e
```

```

[System.Runtime.InteropServices.Guid("B33A8523-7EFD-4B8C-AD0D-4BA9EB8B9F21")]
public enum swCommandFlyoutStyle_e : System.Enum 
```

```

public enum swCommandFlyoutStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B33A8523-7EFD-4B8C-AD0D-4BA9EB8B9F21")
public enum swCommandFlyoutStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B33A8523-7EFD-4B8C-AD0D-4BA9EB8B9F21")]
__value public enum swCommandFlyoutStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B33A8523-7EFD-4B8C-AD0D-4BA9EB8B9F21")]
public enum class swCommandFlyoutStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCommandFlyoutStyle\_Favorite** | 1 = the first command in the menu list is the immediate action for the main button |
| **swCommandFlyoutStyle\_LastUsed** | 2 = the last used command in the menu list is the immediate action for the main button |
| **swCommandFlyoutStyle\_Simple** | 0 = no immediate action is available for the main button |

Remarks

Context-sensitive menus support only the swCommandFlyoutStyle\_Simple flyout style.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCommandFlyoutStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

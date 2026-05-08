# swMenuItemType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMenuItemType_e`

Menu item types.
Menu item types.

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

<System.Runtime.InteropServices.GuidAttribute("5B98E547-90C8-4EB8-9898-4BB94779F441")>
Public Enum swMenuItemType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMenuItemType_e
```

```

[System.Runtime.InteropServices.Guid("5B98E547-90C8-4EB8-9898-4BB94779F441")]
public enum swMenuItemType_e : System.Enum 
```

```

public enum swMenuItemType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("5B98E547-90C8-4EB8-9898-4BB94779F441")
public enum swMenuItemType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("5B98E547-90C8-4EB8-9898-4BB94779F441")]
__value public enum swMenuItemType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("5B98E547-90C8-4EB8-9898-4BB94779F441")]
public enum class swMenuItemType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMenuItemType\_Break** | 1 = Add titles to sections of third-party pop-up menus |
| **swMenuItemType\_Default** | 0 = Add actionable menu items to third-party pop-up menus |
| **swMenuItemType\_Separator** | 2 = Add separator bars to third-party pop-up menus |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMenuItemType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)  
[ISldWorks::AddItemToThirdPartyPopupMenu](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.html)  
[ISldWorks::AddItemToThirdPartyPopupMenu2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.html)

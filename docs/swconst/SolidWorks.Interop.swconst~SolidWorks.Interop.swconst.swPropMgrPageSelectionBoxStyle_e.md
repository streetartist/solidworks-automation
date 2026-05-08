# swPropMgrPageSelectionBoxStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageSelectionBoxStyle_e`

PropertyManager page selection box styles. Bitmask.
PropertyManager page selection box styles. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("CE0DA579-62EA-4A56-A6DE-4B4202775420")>
Public Enum swPropMgrPageSelectionBoxStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropMgrPageSelectionBoxStyle_e
```

```

[System.Runtime.InteropServices.Guid("CE0DA579-62EA-4A56-A6DE-4B4202775420")]
public enum swPropMgrPageSelectionBoxStyle_e : System.Enum 
```

```

public enum swPropMgrPageSelectionBoxStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CE0DA579-62EA-4A56-A6DE-4B4202775420")
public enum swPropMgrPageSelectionBoxStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CE0DA579-62EA-4A56-A6DE-4B4202775420")]
__value public enum swPropMgrPageSelectionBoxStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CE0DA579-62EA-4A56-A6DE-4B4202775420")]
public enum class swPropMgrPageSelectionBoxStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropMgrPageSelectionBoxStyle\_HScroll** | 1 or 0x1; Specifies that the selection box has a scroll bar so that interactive users can scroll through the list of items |
| **swPropMgrPageSelectionBoxStyle\_MultipleItemSelect** | 4 or 0x4; Specifies that you can select multiple items in the selection box |
| **swPropMgrPageSelectionBoxStyle\_UpAndDownButtons** | 2 or 0x2; Specifies that selection listbox has up and down arrows so that interactive users can move items in the list up or down |
| **swPropMgrPageSelectionBoxStyle\_WantListboxSelectionChanged** | 8 or 0x8; Specifies that you want a notification sent when a user changes the selected item in a listbox or selection listbox |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropMgrPageSelectionBoxStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

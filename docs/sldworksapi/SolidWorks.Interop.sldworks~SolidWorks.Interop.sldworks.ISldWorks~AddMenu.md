# AddMenu Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu`

Adds a menu item to a SOLIDWORKS menu for DLL applications.
Adds a menu item to a SOLIDWORKS menu for DLL applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenu( _
   ByVal DocType As System.Integer, _
   ByVal Menu As System.String, _
   ByVal Position As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim DocType As System.Integer
Dim Menu As System.String
Dim Position As System.Integer
Dim value As System.Integer
 
value = instance.AddMenu(DocType, Menu, Position)
```

```

System.int AddMenu( 
   System.int DocType,
   System.string Menu,
   System.int Position
)
```

```

System.int AddMenu( 
   System.int DocType,
   System.String^ Menu,
   System.int Position
) 
```

#### Parameters

*DocType*
:   Document type to add the menu item as defined by [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*Menu*
:   Name of menu item to add, including any parent menu names, e.g., subMenuString@menuString

*Position*
:   Specifies the position where to add the new menu item; 0 = first position and 1 = end of the parent menu (see **Remarks**)

#### Return Value

1 if menu item is added successfully added or 0 if adding the menu item failed

Remarks

If the name of a parent menu is not specified in Menu, then:

- the menu item appears on the **Tools** menu below the **XPress products** menu item.
- Position is ignored.

Menus items are automatically created at the end of the parent menu when using [ISldWorks::AddMenuItem5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem5.md). Therefore, if your menu structure is created using sequential calls to SldWorks::AddMenuItem5, then all the menu items are positioned based on their order of creation.

This method is only required when a menu needs to be placed into an existing menu at a specific position.

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

Example

[Add Menu and Menu Item (C#)](Add_Menu_and_Menu_Item_Example_CSharp.htm)  
[Add Menu and Menu Item (VB.NET)](Add_Menu_and_Menu_Item_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.md)  
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.md)  
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.md)  
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.md)  
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.md)  
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md)  
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.md)  
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.md)  
[ISldWorks::GetLocalizedMenuName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.md)

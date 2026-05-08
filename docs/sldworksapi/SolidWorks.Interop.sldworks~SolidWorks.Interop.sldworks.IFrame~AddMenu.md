# AddMenu Method (IFrame)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu`

Adds a menu item.
Adds a menu item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenu( _
   ByVal Menu As System.String, _
   ByVal Position As System.Integer _
) As System.Boolean
```

```

Dim instance As IFrame
Dim Menu As System.String
Dim Position As System.Integer
Dim value As System.Boolean
 
value = instance.AddMenu(Menu, Position)
```

```

System.bool AddMenu( 
   System.string Menu,
   System.int Position
)
```

```

System.bool AddMenu( 
   System.String^ Menu,
   System.int Position
) 
```

#### Parameters

*Menu*
:   Name of the menu item to add; including parent menu names, e.g., subMenuString@menuString (see **Remarks**)

*Position*
:   Position of the existing menu item before which to insert the new menu item; the first menu item is at position 0; if Position is 1, the new menu item is appended to the end of the menu (see **Remarks**)

#### Return Value

True if menu item was successfully added, false if not

Remarks

If the name of a parent menu name is not specified in Menu, then:

- the menu item appears on the Tools menu below the **XPress products** menu item.
- Position is ignored.

This method is only valid when the application is implemented as a DLL, not as an EXE.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)  
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.md)  
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)  
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.md)  
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md)  
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md)  
[ISldWorks::GetLocalizedMenuName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.md)  
[IFrame::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2.md)  
[IFrame::RemoveMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.md)

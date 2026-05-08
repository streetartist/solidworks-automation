# RemoveMenu Method (IFrame)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu`

Removes a menu item.
Removes a menu item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveMenu( _
   ByVal MenuItemString As System.String _
) 
```

```

Dim instance As IFrame
Dim MenuItemString As System.String
 
instance.RemoveMenu(MenuItemString)
```

```

void RemoveMenu( 
   System.string MenuItemString
)
```

```

void RemoveMenu( 
   System.String^ MenuItemString
) 
```

#### Parameters

*MenuItemString*
:   Name of menu item (see **Remarks**)

Remarks

Use [ISldWorks::GetMenuStrings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.md) to get MenuItemString.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md)  
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)  
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.md)  
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)  
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.md)  
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md)  
[ISldWorks::GetMenuStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.md)

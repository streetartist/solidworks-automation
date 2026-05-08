# RenameMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu`

Renames a menu item.
Renames a menu item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RenameMenu( _
   ByVal MenuItemString As System.String, _
   ByVal NewName As System.String _
) 
```

```

Dim instance As IFrame
Dim MenuItemString As System.String
Dim NewName As System.String
 
instance.RenameMenu(MenuItemString, NewName)
```

```

void RenameMenu( 
   System.string MenuItemString,
   System.string NewName
)
```

```

void RenameMenu( 
   System.String^ MenuItemString,
   System.String^ NewName
) 
```

#### Parameters

*MenuItemString*
:   Name of the menu item

*NewName*
:   New name of this menu item

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
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)  
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.md)  
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md)  
[ISldWorks::GetMenuStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.md)

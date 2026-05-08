# RemoveFromMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu`

Removes:
Removes:

- the specified command from all main frame menus or a toolbar or both
- the specified command's parent menus

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveFromMenu( _
   ByVal CommandID As System.Integer, _
   ByVal DocumentType As System.Integer, _
   ByVal Option As System.Integer, _
   ByVal RemoveParentMenu As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim DocumentType As System.Integer
Dim Option As System.Integer
Dim RemoveParentMenu As System.Boolean
Dim value As System.Boolean
 
value = instance.RemoveFromMenu(CommandID, DocumentType, Option, RemoveParentMenu)
```

```

System.bool RemoveFromMenu( 
   System.int CommandID,
   System.int DocumentType,
   System.int Option,
   System.bool RemoveParentMenu
)
```

```

System.bool RemoveFromMenu( 
   System.int CommandID,
   System.int DocumentType,
   System.int Option,
   System.bool RemoveParentMenu
) 
```

#### Parameters

*CommandID*
:   Command ID of the command to remove as defined by [swCommands\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.md)

*DocumentType*
:   Document types in which to remove the command as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*Option*
:   - 1 = Menu
    - 2 = Toolbar
    - 3 = Both menu and toolbar

*RemoveParentMenu*
:   True to remove the specified command's parent menu, false to not

    NOTE: This parameter is specific to menus only; it does not affect toolbars.

#### Return Value

True if the specified items are removed, false if not

Remarks

This method does not affect context-sensitive menus (also called shortcut menus and pop-up menus); this command only affects main frame menus and toolbars. To remove commands and parent menus from context-sensitive menus, use [ISldWorks::RemoveFromPopupMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.md).

The specified items are removed after this method executes, and their removal can be seen immediately.

This method is not persistent across SOLIDWORKS sessions.

Example

[Remove Menu Commands, Menus, and Toolbar Buttons (VBA)](Remove_Menu_Commands_Menus_and_Toolbar_Buttons_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md)  
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.md)  
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.md)  
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.md)  
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.md)  
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.md)  
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)  
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md)  
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.md)  
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.md)

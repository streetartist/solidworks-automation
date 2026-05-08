# RemoveFromPopupMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu`

Removes the specified menu item from one or all specified context-sensitive menus (also called shortcut menus and pop-up menus) for the specified document types.
Removes the specified menu item from one or all specified context-sensitive menus (also called shortcut menus and pop-up menus) for the specified document types.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveFromPopupMenu( _
   ByVal CommandID As System.Integer, _
   ByVal DocumentType As System.Integer, _
   ByVal SelectionType As System.Integer, _
   ByVal RemoveParentMenu As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim DocumentType As System.Integer
Dim SelectionType As System.Integer
Dim RemoveParentMenu As System.Boolean
Dim value As System.Boolean
 
value = instance.RemoveFromPopupMenu(CommandID, DocumentType, SelectionType, RemoveParentMenu)
```

```

System.bool RemoveFromPopupMenu( 
   System.int CommandID,
   System.int DocumentType,
   System.int SelectionType,
   System.bool RemoveParentMenu
)
```

```

System.bool RemoveFromPopupMenu( 
   System.int CommandID,
   System.int DocumentType,
   System.int SelectionType,
   System.bool RemoveParentMenu
) 
```

#### Parameters

*CommandID*
:   Command ID of the command to remove as defined by [swCommands\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.md)

*DocumentType*
:   Document types in which to remove the command as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*SelectionType*
:   Context-sensitive menu from which to remove the command as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

    NOTE: Specifying swSelEVERYTHING will remove the command from all context-sensitive menus

*RemoveParentMenu*
:   True to remove the specified command's any parent menus, false to not

Remarks

The removal of the specified menu item takes affect the next time the context-sensitive menu is displayed.

To remove main frame menu commands and menus, use [ISldWorks::RemoveFromMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.md).

This method is not persistent across SOLIDWORKS sessions.

Example

[Remove Menu commands, Menus, and Toolbar Buttons (VBA)](Remove_Menu_Commands_Menus_and_Toolbar_Buttons_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md)  
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.md)  
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.md)  
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md)  
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.md)

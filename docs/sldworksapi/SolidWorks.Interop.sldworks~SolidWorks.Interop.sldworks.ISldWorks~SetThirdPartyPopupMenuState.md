# SetThirdPartyPopupMenuState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetThirdPartyPopupMenuState`

Sets whether to show or hide a third-party popup (shortcut) menu.
Sets whether to show or hide a third-party popup (shortcut) menu.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetThirdPartyPopupMenuState( _
   ByVal RegisterId As System.Integer, _
   ByVal IsActive As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim IsActive As System.Boolean
Dim value As System.Boolean
 
value = instance.SetThirdPartyPopupMenuState(RegisterId, IsActive)
```

```

System.bool SetThirdPartyPopupMenuState( 
   System.int RegisterId,
   System.bool IsActive
)
```

```

System.bool SetThirdPartyPopupMenuState( 
   System.int RegisterId,
   System.bool IsActive
) 
```

#### Parameters

*RegisterId*
:   ID of shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.md)

*IsActive*
:   True to show the shortcut menu, false to hide it

#### Return Value

True if shortcut menu is shown, false if it is hidden

Remarks

This method is supported in C++ applications only.

Typical steps in creating and displaying your shortcut menu:

1. [Add menu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md) and [add menu items](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem4.md) to the SOLIDWORKS main menu bar for your shortcut menu, or [add an icon to a context-sensitive menu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.md) that displays your shortcut menu, or both.
2. [Register](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.md) your shortcut menu.
3. [Add](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.md) your shortcut menu items.
4. [Show](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.md) your shortcut menu at a specific location in the SOLIDWORKS graphics area, typically from a mouse event handler.
5. [Remove](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveItemFromThirdPartyPopupMenu.md) a menu item from your shortcut menu, if desired.
6. Toggle the visibility of your shortcut menu.
7. [Remove the shortcut menu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md) from the SOLIDWORKS main menu bar and [remove the icon from the context-sensitive menu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.md), if  added.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)

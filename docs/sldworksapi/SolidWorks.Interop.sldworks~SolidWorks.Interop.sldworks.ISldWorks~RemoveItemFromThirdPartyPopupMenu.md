# RemoveItemFromThirdPartyPopupMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveItemFromThirdPartyPopupMenu`

Removes a menu item and icon from a third-party pop-up (shortcut) menu.
Removes a menu item and icon from a third-party pop-up (shortcut) menu.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveItemFromThirdPartyPopupMenu( _
   ByVal RegisterId As System.Integer, _
   ByVal DocType As System.Integer, _
   ByVal Item As System.String, _
   ByVal IconIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim DocType As System.Integer
Dim Item As System.String
Dim IconIndex As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveItemFromThirdPartyPopupMenu(RegisterId, DocType, Item, IconIndex)
```

```

System.bool RemoveItemFromThirdPartyPopupMenu( 
   System.int RegisterId,
   System.int DocType,
   System.string Item,
   System.int IconIndex
)
```

```

System.bool RemoveItemFromThirdPartyPopupMenu( 
   System.int RegisterId,
   System.int DocType,
   System.String^ Item,
   System.int IconIndex
) 
```

#### Parameters

*RegisterId*
:   :   ID of the shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.md)

*DocType*
:   :   Document type where to display the shortcut menu, as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*Item*
:   Name of the shortcut menu item

*IconIndex*
:   1-based index of the icon (see **Remarks**)

#### Return Value

True if the shortcut menu item or icon is removed, false if not

Remarks

To remove:

- a menu item, specify a valid name for Item only. If you specify both Item and IconIndex, only Item is evaluated; IconIndex is ignored.
- a menu bar icon, specify an empty string for Item and pass the 1-based index value of the icon for IconIndex.

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

Example

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)  
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddItemToThirdPartyPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.md)  
[ISldWorks::SetThirdPartyPopupMenuState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetThirdPartyPopupMenuState.md)  
[ISldWorks::ShowThirdPartyPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.md)  
[ISldWorks::AddItemToThirdPartyPopupMenu2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.md)

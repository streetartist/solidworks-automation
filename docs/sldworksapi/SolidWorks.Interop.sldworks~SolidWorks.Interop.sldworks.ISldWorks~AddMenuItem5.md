# AddMenuItem5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem5`

Adds a menu item and image to the SOLIDWORKS user interface.
Adds a menu item and image to the SOLIDWORKS user interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuItem5( _
   ByVal DocumentType As System.Integer, _
   ByVal Cookie As System.Integer, _
   ByVal MenuItem As System.String, _
   ByVal Position As System.Integer, _
   ByVal MenuCallback As System.String, _
   ByVal MenuEnableMethod As System.String, _
   ByVal HintString As System.String, _
   ByVal ImageList As System.Object _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim DocumentType As System.Integer
Dim Cookie As System.Integer
Dim MenuItem As System.String
Dim Position As System.Integer
Dim MenuCallback As System.String
Dim MenuEnableMethod As System.String
Dim HintString As System.String
Dim ImageList As System.Object
Dim value As System.Integer
 
value = instance.AddMenuItem5(DocumentType, Cookie, MenuItem, Position, MenuCallback, MenuEnableMethod, HintString, ImageList)
```

```

System.int AddMenuItem5( 
   System.int DocumentType,
   System.int Cookie,
   System.string MenuItem,
   System.int Position,
   System.string MenuCallback,
   System.string MenuEnableMethod,
   System.string HintString,
   System.object ImageList
)
```

```

System.int AddMenuItem5( 
   System.int DocumentType,
   System.int Cookie,
   System.String^ MenuItem,
   System.int Position,
   System.String^ MenuCallback,
   System.String^ MenuEnableMethod,
   System.String^ HintString,
   System.Object^ ImageList
) 
```

#### Parameters

*DocumentType*
:   Document type to which to add the menu item as defined by [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*Cookie*
:   Cookie as defined in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*MenuItem*
:   Menu item string ( e.g., "menuItem@menuString"); SOLIDWORKS creates menu items only if they do not already exist

    NOTES:

    - Specify the name of the menu for menuString (e.g., File, View, etc.) where you want your menu item to appear. If you do not specify menu string, then the menu item appears on the **Tools** menu below the **Xpress Products** menu item.
    - To add your own menu to which to add this menu item, call [ISldWorks::AddMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md) and substitute the name of your menu for menuString.
    - Use the & symbol to include an accelerator key, e.g., MyItem@, adds MyItem to the File menu with an accelerator key. To display the accelerator key, press the Alt key. The accelerator key is underlined.

*Position*
:   Position where to add the new menu item; the first item is position 0; if -1 is specified for Position, then the new menu item is added to the bottom of the list; this argument specifies the position of the menu item in relation to its immediate parent menu

*MenuCallback*
:   Function to call when this menu item is selected (see **Remarks**)

*MenuEnableMethod*
:   Optional function that controls the state of the menu item (See **Remarks**)

    If specified:

    - SOLIDWORKS calls this function before displaying the menu item
    - display of the menu item is controlled by the return value of MenuEnableMethod

    | If MenuEnableMethod returns... | **Then SOLIDWORKS...** |
    | --- | --- |
    | 0 | Deselects and disables the menu item |
    | 1 | Deselects and enables the menu item; this is the default menu state if no update function is specified |
    | 2 | Selects and disables the menu item |
    | 3 | Selects and enables the menu item |

*HintString*
:   Text to show in the SOLIDWORKS status bar when the user moves the pointer over this menu item; if you specify HintString, then it must be preceded by a comma

*ImageList*
:   Array of strings for the paths for the image files for the menu item (see **Remarks**)

#### Return Value

SOLIDWORKS runtime command ID if successful or -1 if unsuccessful

Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify MenuCallback and MenuEnableMethod.

For information about using this method with the [ISwAddin](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin.md) object, see [Using ISwAddin to Create a SOLIDWORKS Add-in](sldworksAPIProgGuide.chm::/OVERVIEW/Using_SwAddin_to_Create_a_SOLIDWORKS_Addin.htm).

You can add a new menu item to any one of the four SOLIDWORKS frames (main, part, assembly, or drawing). To do this, call this method with the appropriate argument in the swDocumentTypes\_e.DocumentType parameter. For example, if you want your menu item to be available when a part document is active, then call this method and pass swDocumentTypes\_e.swDocPART as the first argument. After you adding your menu item to the part frame, you do not need to do it again during the current SOLIDWORKS session. Once a part document is activated by the user, SOLIDWORKS automatically displays your menu item.

This method supports scaling for high resolution screens with high resolution operating system scaling options.

ImageList images can be:

- 20 x 20 pixels
- 32 x 32 pixels
- 40 x 40 pixels
- 64 x 64 pixels
- 96 x 96 pixels
- 128 x128 pixels

Images should use 256-color palette.

To add a menu item separator:

- leave the text for the menu item blank, so that the menu string for the MenuItem argument starts with the at-sign symbol (@):   
    
  "@subMenuString@menuString"
- specify an existing method for the MenuCallback argument. This method is never called, so its implementation can be empty.
- specify empty strings for MenuEnableMethod and HintString.
- specify Nothing or null for ImageList.

Read [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm) for more information.

Example

[Add Menu and Menu Item (C#)](Add_Menu_and_Menu_Item_Example_CSharp.htm)  
[Add Menu and Menu Item (VB.NET)](Add_Menu_and_Menu_Item_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddMenuPopupItem4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem4.md)  
[ISldWorks::AddToolbar5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.md)  
[ISldWorks::GetLocalizedMenuName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.md)  
[ISldWorks::RemoveFromMenu Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.md)  
[ISldWorks::RemoveFromPopupMenu Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.md)  
[ISldWorks::RemoveItemFromThirdPartyPopupMenu Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveItemFromThirdPartyPopupMenu.md)  
[ISldWorks::RemoveMenu Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md)  
[ISldWorks::RemoveMenuPopupItem2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.md)  
[ISldWorks::RemoveToolbar2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.md)  
[ISldWorks::GetImageSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.md)

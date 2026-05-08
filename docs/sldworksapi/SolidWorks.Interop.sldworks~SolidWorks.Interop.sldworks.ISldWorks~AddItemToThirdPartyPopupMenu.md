# AddItemToThirdPartyPopupMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu`

Adds menu items to a pop-up (shortcut) menu in a C++ SOLIDWORKS add-in.
Adds menu items to a pop-up (shortcut) menu in a C++ SOLIDWORKS add-in.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddItemToThirdPartyPopupMenu( _
   ByVal RegisterId As System.Integer, _
   ByVal DocType As System.Integer, _
   ByVal Item As System.String, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal CustomName As System.String, _
   ByVal HintString As System.String, _
   ByVal BitmapFileName As System.String, _
   ByVal MenuItemTypeOption As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim DocType As System.Integer
Dim Item As System.String
Dim CallbackFcnAndModule As System.String
Dim CustomName As System.String
Dim HintString As System.String
Dim BitmapFileName As System.String
Dim MenuItemTypeOption As System.Integer
Dim value As System.Boolean
 
value = instance.AddItemToThirdPartyPopupMenu(RegisterId, DocType, Item, CallbackFcnAndModule, CustomName, HintString, BitmapFileName, MenuItemTypeOption)
```

```

System.bool AddItemToThirdPartyPopupMenu( 
   System.int RegisterId,
   System.int DocType,
   System.string Item,
   System.string CallbackFcnAndModule,
   System.string CustomName,
   System.string HintString,
   System.string BitmapFileName,
   System.int MenuItemTypeOption
)
```

```

System.bool AddItemToThirdPartyPopupMenu( 
   System.int RegisterId,
   System.int DocType,
   System.String^ Item,
   System.String^ CallbackFcnAndModule,
   System.String^ CustomName,
   System.String^ HintString,
   System.String^ BitmapFileName,
   System.int MenuItemTypeOption
) 
```

#### Parameters

*RegisterId*
:   ID of shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.md)

*DocType*
:   Document type where to display shortcut menu, as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*Item*
:   Name of shortcut menu item (see **Remarks**)

*CallbackFcnAndModule*
:   Function called when user clicks the shortcut menu item (see **Remarks**)

*CustomName*
:   Empty string

*HintString*
:   Text to display in the SOLIDWORKS status bar when users move the mouse over this shortcut menu item

*BitmapFileName*
:   Path and filename of the bitmap

*MenuItemTypeOption*
:   Menu item as defined in [swMenuItemType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html)

#### Return Value

True if the shortcut menu item is added, false if not

Remarks

This method is supported in C++ applications only, and it only works in C++ applications implemented as DLLs, not as EXEs.

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

The CallbackFcnAndModule argument specifies which function to call when this shortcut menu item is selected by the user. The syntax is as follows:

"dllname@function@updatefunction"

where:

|  |  |
| --- | --- |
| dllname | Name of your library as specified in the project .def file. The actual DLL filename and the definition in the .def file must be the same. |
| function | Name of the function that gets called when the user clicks the shortcut menu item. This function must also be declared as an EXPORT in your .def file.  See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to implement your function. |
| updatefunction | Optional argument that controls the state of the shortcut menu item. If specified, then SOLIDWORKS calls this function before the shortcut menu item is displayed. Define your updatefunction to return an integer and declare it as an EXPORT or included in your .def file.  The display of the third-party shortcut menu item is controlled by the return value of the function as follows:   - return 0 - Unchecked and disabled. - return 1 - Unchecked and enabled. This is the default menu state if no updatefunction is specified. - return 2 - Checked and disabled. - return 3 - Checked and enabled.   See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to implement your updatefunction. |

Example

- [C++](#i-tab-content-357a052a-bccb-4bb3-a908-2a77d10ee6fe)

```

To add a section title or break to the shortcut menu:

iSwApp->AddItemToThirdPartyPopupMenu
(
registerIdPMenu1,
swDocPART,
CComBSTR(_T("Menu Break")),
CComBSTR(_T("")),
CComBSTR(_T("")),
CComBSTR(_T("")),
CComBSTR(_T("")),
swMenuItemType_Break,
&itemAdded
);

To add an icon to a menu bar above the shortcut menu:

iSwApp->AddItemToThirdPartyPopupMenu
(
registerIdPMenu1,
swDocPART,
CComBSTR(_T("")),
CComBSTR(_T("UserPopupMenus.dll@UserItem1_Menu1_Callback")),
CComBSTR(_T("")),
CComBSTR(_T("UserItem1_Menu1_Callback_hint")),
UserItem1_Menu1_bitmapFile,
swMenuItemType_Default,
&itemAdded
);

To add an actionable item to the shortcut menu:

iSwApp->AddItemToThirdPartyPopupMenu
(
registerIdPMenu1,
swDocPART,
CComBSTR(_T("UserItem1_Menu1_Callback")),
CComBSTR(_T("UserPopupMenus.dll@UserItem1_Menu1_Callback")),
CComBSTR(_T("")),
CComBSTR(_T("UserItem1_Menu1_Callback_hint")),
UserItem1_Menu1_bitmapFile,
swMenuItemType_Default,
&itemAdded
);

To add a separator bar to the shortcut menu:

iSwApp->AddItemToThirdPartyPopupMenu
(
registerIdPMenu1,
swDocPART,
CComBSTR(_T("")),
CComBSTR(_T("")),
CComBSTR(_T("")),
CComBSTR(_T("")),
CComBSTR(_T("")),
swMenuItemType_Separator,
&itemAdded
);
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddItemToThirdPartyPopupMenu2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.md)

# AddMenuPopupIcon2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon2`

Obsolete. Superseded by IFrame::AddMenuPopupIcon3.
Obsolete. Superseded by [IFrame::AddMenuPopupIcon3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuPopupIcon2( _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal HintString As System.String, _
   ByVal Identifier As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal CallbackUpdateFunction As System.String, _
   ByVal CustomNames As System.String, _
   ByVal BitmapFilePath As System.String _
) As System.Boolean
```

```

Dim instance As IFrame
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim HintString As System.String
Dim Identifier As System.Integer
Dim CallbackFunction As System.String
Dim CallbackUpdateFunction As System.String
Dim CustomNames As System.String
Dim BitmapFilePath As System.String
Dim value As System.Boolean
 
value = instance.AddMenuPopupIcon2(DocType, SelectType, HintString, Identifier, CallbackFunction, CallbackUpdateFunction, CustomNames, BitmapFilePath)
```

```

System.bool AddMenuPopupIcon2( 
   System.int DocType,
   System.int SelectType,
   System.string HintString,
   System.int Identifier,
   System.string CallbackFunction,
   System.string CallbackUpdateFunction,
   System.string CustomNames,
   System.string BitmapFilePath
)
```

```

System.bool AddMenuPopupIcon2( 
   System.int DocType,
   System.int SelectType,
   System.String^ HintString,
   System.int Identifier,
   System.String^ CallbackFunction,
   System.String^ CallbackUpdateFunction,
   System.String^ CustomNames,
   System.String^ BitmapFilePath
) 
```

#### Parameters

*DocType*
:   [Document type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html) whose context-sensitive menus display the icon

*SelectType*
:   [Selection type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) whose context-sensitive menus display the icon

*HintString*
:   Text displayed in the SOLIDWORKS status bar when the user moves the pointer over the icon

*Identifier*
:   ID of the add-in; value of the Cookie argument passed by [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*CallbackFunction*
:   Function called when user clicks the context-sensitive menu icon (**see Remarks**)

*CallbackUpdateFunction*
:   Optional function that controls the state of the icon; if specified, then SOLIDWORKS calls this function before displaying the icon

    | If CallbackUpdateFunction returns... | Then SOLIDWORKS... |
    | --- | --- |
    | 0 | Deselects and disables the item |
    | 1 | Deselects and enables the item; this is the default state if no update function is specified |
    | 4 | Hides the item |

    (see **Remarks**)

*CustomNames*
:   Names of custom feature types (see **Remarks**)

*BitmapFilePath*
:   Path and file name of the bitmap for the context-sensitive menu icon

#### Return Value

True if the context-sensitive menu icon is added, false if not

Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify CallbackFunction and CallbackUpdateFunction.

When the icon is clicked, the function specified in CallbackFunction can perform actions such as [displaying a third-party pop-up menu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.md).

CustomNames is a semi-colon separated list of the names of the custom feature types. This argument is applicable only if SelectType is a custom feature type (like swSelATTRIBUTES); in the case of swSelATTRIBUTES, set this field to the name of the attribute definition.

Example

[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)  
[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md)  
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)  
[IFrame::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2.md)  
[IFrame::GetMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.md)  
[IFrame::GetMenux64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenux64.md)  
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)  
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.md)  
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md)  
[IFrame::RemoveMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.md)  
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md)  
[IFrame::MenuPinned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~MenuPinned.md)  
[IFrame::AddMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.md)  
[ISldWorks::AddItemToThirdPartyPopupMenu2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.md)

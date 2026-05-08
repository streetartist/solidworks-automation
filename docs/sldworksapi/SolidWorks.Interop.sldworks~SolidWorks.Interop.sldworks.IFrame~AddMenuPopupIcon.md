# AddMenuPopupIcon Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon`

Adds an icon to a context-sensitive menu of a C++ SOLIDWORKS add-in.
Adds an icon to a context-sensitive menu of a C++ SOLIDWORKS add-in.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuPopupIcon( _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal HintString As System.String, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal CustomNames As System.String, _
   ByVal BitmapFilePath As System.String _
) As System.Boolean
```

```

Dim instance As IFrame
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim HintString As System.String
Dim CallbackFcnAndModule As System.String
Dim CustomNames As System.String
Dim BitmapFilePath As System.String
Dim value As System.Boolean
 
value = instance.AddMenuPopupIcon(DocType, SelectType, HintString, CallbackFcnAndModule, CustomNames, BitmapFilePath)
```

```

System.bool AddMenuPopupIcon( 
   System.int DocType,
   System.int SelectType,
   System.string HintString,
   System.string CallbackFcnAndModule,
   System.string CustomNames,
   System.string BitmapFilePath
)
```

```

System.bool AddMenuPopupIcon( 
   System.int DocType,
   System.int SelectType,
   System.String^ HintString,
   System.String^ CallbackFcnAndModule,
   System.String^ CustomNames,
   System.String^ BitmapFilePath
) 
```

#### Parameters

*DocType*
:   [Document type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html) to which to add the context-sensitive menu icon

*SelectType*
:   [Selection type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) to which to add the context-sensitive menu icon

*HintString*
:   Text displayed in the SOLIDWORKS status bar when the user moves the mouse over the icon

*CallbackFcnAndModule*
:   Function called when user clicks the context-sensitive menu icon (see **Remarks**)

*CustomNames*
:   Names of custom feature types (see **Remarks**)

*BitmapFilePath*
:   Path and file name of the bitmap for the context-sensitive menu icon

#### Return Value

True if the context-sensitive menu icon is added, false if not

Remarks

This method is supported in C++ applications only, and it only works for C++ applications implemented as **.dll** files, not as **.exe** files. Any function exposed as a callback from an context-sensitive menu icon must be declared as an EXPORT or included in your **.def** file.

The CallbackFcnAndModule argument specifies which function to call when the shortcut menu icon is clicked by the user. The syntax is as follows:

dllname@function

where:

|  |  |
| --- | --- |
| dllname | Name of your library as specified in the project **.def** file. The actual file name and the definition in the **.def** file must be the same. |
| function | Name of the function that gets called when the user clicks the icon. This function must also be declared as an EXPORT in your **.def** file.  See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to implement your callback function. |

CustomNames is a semi-colon separated list of the names of the custom feature types. This argument is applicable only if SelectType is a custom feature type (like swSelATTRIBUTES); in the case of swSelATTRIBUTES, set this field to the name of the attribute definition.

Example

- [C++](#i-tab-content-237890da-8241-42db-8526-d13790097978)

```

//Add a single icon to the standard
//SOLIDWORKS face context menu.
swFrame->AddMenuPopupIcon(
swDocPART,
swSelFACES,
CComBSTR(_T("UserPopupMenus.dll@MinibarItem1_Menu1_Callback,Facehintstring")),
CComBSTR(_T("UserPopupMenus.dll@MinibarItem1_Menu1_Callback")),
CComBSTR(_T("")),
UserItem1_Menu1_bitmapFile,
&iconSuccess
);
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::RemoveMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.md)  
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md)  
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)  
[IFrame::GetMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.md)  
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)  
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md)  
[IFrame::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2.md)  
[IFrame::AddMenuPopupIcon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon2.md)  
[ISldWorks::AddItemToThirdPartyPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.md)

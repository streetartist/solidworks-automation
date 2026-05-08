# AddMenuPopupItem2 Method (IFrame)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2`

Adds a menu item or separator to a shortcut menu (i.e., a right-click pop-up menu).
Adds a menu item or separator to a shortcut menu (i.e., a right-click pop-up menu).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuPopupItem2( _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal Item As System.String, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal CustomNames As System.String, _
   ByVal Unused As System.Integer, _
   ByVal BitmapFileName As System.String _
) As System.Boolean
```

```

Dim instance As IFrame
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim Item As System.String
Dim CallbackFcnAndModule As System.String
Dim CustomNames As System.String
Dim Unused As System.Integer
Dim BitmapFileName As System.String
Dim value As System.Boolean
 
value = instance.AddMenuPopupItem2(DocType, SelectType, Item, CallbackFcnAndModule, CustomNames, Unused, BitmapFileName)
```

```

System.bool AddMenuPopupItem2( 
   System.int DocType,
   System.int SelectType,
   System.string Item,
   System.string CallbackFcnAndModule,
   System.string CustomNames,
   System.int Unused,
   System.string BitmapFileName
)
```

```

System.bool AddMenuPopupItem2( 
   System.int DocType,
   System.int SelectType,
   System.String^ Item,
   System.String^ CallbackFcnAndModule,
   System.String^ CustomNames,
   System.int Unused,
   System.String^ BitmapFileName
) 
```

#### Parameters

*DocType*
:   [Document type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html) to which to add the shortcut menu item

*SelectType*
:   [Selection type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) to which to add the shortcut menu item

*Item*
:   Description that appears on the shortcut menu item

*CallbackFcnAndModule*
:   :   Functions called when user clicks the shortcut menu item (see **Remarks**)

*CustomNames*
:   :   Names of custom feature types (see **Remarks**)

*Unused*
:   Reserved for future use, set to 0

*BitmapFileName*
:   Path and filename of bitmap for the shortcut menu item

#### Return Value

True if shortcut menu item is added, false if not

Remarks

To add a separator, set the Item argument to NULL or an empty string.

If you want to create a pull-down menu, use [IFrame::AddMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md).

This method only works for the C++ application implemented as a DLL, not as an EXE. Any function exposed as a callback from a menu item must be declared as an EXPORT or included in your .def file.

You can add a new menu to any one of the four SOLIDWORKS frames (Main frame, part frame, assembly frame, or drawing frame). To do this, you must get the [IFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md) object when the desired frame is active. For example, if you want your menu to be available when a part document is active, then call [ISldWorks::Frame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Frame.md) when a part is first loaded or created, and use that IFrame object to call this method. Once you add your menu to the part frame, you do not need to do it again during the current SOLIDWORKS session.

The CallbackFcnAndModule argument specifies which function to call when this menu item is selected by the user. The syntax is as follows:

"dllname@function@updatefunction,hintstring"

where:

|  |  |
| --- | --- |
| dllname | Name of your library as specified in the project .def file. The actual DLL filename and the definition in the .def file must be the same. |
| function | Name of the function that gets called when the user clicks the button. This function must also be declared as an EXPORT in your .def file.  See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to implement your callback function. |
| updatefunction | Optional argument that controls the state of the button. If specified, then SOLIDWORKS calls this function before the button is displayed. Define your updatefunction to return an integer and declare it as an EXPORT or included in your .def file. The display of the button is controlled by the return value of the function as follows:   - return 0 - Menu item is unchecked and disabled. - return 1 - Menu item is unchecked and enabled. This is the default menu state if no updatefunction is specified. - return 2 - Menu item is checked and disabled. - return 3 - Menu item is checked and enabled.   See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to implement your updatefunction. |
| hintstring | Optional argument that contains a text hint displayed in the SOLIDWORKS status bar when the user moves the mouse over this menu option. If hintstring is specified, then it must be preceded by a comma. For example:  Userdll@AddBox@checkForUserSelects,Add a box |

CustomNames is semi-colon separated list of the names of the custom feature types. This argument is applicable only if SelectType is a custom feature type (like swSelATTRIBUTES); in the case of swSelATTRIBUTES, set this field to the name of the attribute definition.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)  
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)  
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.md)  
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md)  
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md)

# RemoveMenu Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu`

Removes a menu item from the specified document frame.
Removes a menu item from the specified document frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveMenu( _
   ByVal DocType As System.Integer, _
   ByVal MenuItemString As System.String, _
   ByVal CallbackFcnAndModule As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim DocType As System.Integer
Dim MenuItemString As System.String
Dim CallbackFcnAndModule As System.String
Dim value As System.Boolean
 
value = instance.RemoveMenu(DocType, MenuItemString, CallbackFcnAndModule)
```

```

System.bool RemoveMenu( 
   System.int DocType,
   System.string MenuItemString,
   System.string CallbackFcnAndModule
)
```

```

System.bool RemoveMenu( 
   System.int DocType,
   System.String^ MenuItemString,
   System.String^ CallbackFcnAndModule
) 
```

#### Parameters

*DocType*
:   Document type as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*MenuItemString*
:   Menu string (e.g., submenuString@menuString)

*CallbackFcnAndModule*
:   Callback function and module for this menu item as specified when the menu item was added; see [IFrame::AddMenuItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)

#### Return Value

True if the menu item was removed successfully, false if not

Remarks

When a menu item is added with [ISldWorks::AddMenuItem4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem4.md) or [IFrame::AddMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md), the document type for which the menu appears is specified. The DocType argument for this method must match the one used when the menu was created.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetMenuStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.md)  
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md)  
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.md)  
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.md)  
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.md)  
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.md)  
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.md)

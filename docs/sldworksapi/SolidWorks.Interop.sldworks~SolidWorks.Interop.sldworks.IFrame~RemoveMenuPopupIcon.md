# RemoveMenuPopupIcon Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon`

Removes an icon from a context-sensitive shortcut (popup) menu.
Removes an icon from a context-sensitive shortcut (popup) menu.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveMenuPopupIcon( _
   ByVal Index As System.Integer, _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer _
) As System.Boolean
```

```

Dim instance As IFrame
Dim Index As System.Integer
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveMenuPopupIcon(Index, DocType, SelectType)
```

```

System.bool RemoveMenuPopupIcon( 
   System.int Index,
   System.int DocType,
   System.int SelectType
)
```

```

System.bool RemoveMenuPopupIcon( 
   System.int Index,
   System.int DocType,
   System.int SelectType
) 
```

#### Parameters

*Index*
:   Index value of the context-sensitive menu icon; index is 1-based

*DocType*
:   Document type as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*SelectType*
:   [Selection type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) from which to remove the context-sensitive menu icon

#### Return Value

True if the icon is removed from the context-sensitive menu, false if not

Remarks

This method is supported in C++ applications only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::AddMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.md)  
[IFrame::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2.md)  
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md)  
[IFrame::GetMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.md)  
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)  
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.md)  
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md)

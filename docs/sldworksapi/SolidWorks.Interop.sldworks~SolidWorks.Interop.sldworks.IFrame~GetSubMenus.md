# GetSubMenus Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus`

Gets the submenus for this frame.
Gets the submenus for this frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSubMenus( _
   ByVal DocType As System.Integer, _
   ByVal FullMenuName As System.String _
) As System.Object
```

```

Dim instance As IFrame
Dim DocType As System.Integer
Dim FullMenuName As System.String
Dim value As System.Object
 
value = instance.GetSubMenus(DocType, FullMenuName)
```

```

System.object GetSubMenus( 
   System.int DocType,
   System.string FullMenuName
)
```

```

System.Object^ GetSubMenus( 
   System.int DocType,
   System.String^ FullMenuName
) 
```

#### Parameters

*DocType*
:   Type of document as defined by [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*FullMenuName*
:   Full name of menu

#### Return Value

Pointer to an array of the names of the submenus

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md)  
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)  
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.md)  
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md)  
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md)  
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md)

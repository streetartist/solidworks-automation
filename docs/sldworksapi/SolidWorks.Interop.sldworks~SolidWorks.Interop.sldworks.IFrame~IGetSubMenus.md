# IGetSubMenus Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus`

Gets the submenus for this frame.
Gets the submenus for this frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSubMenus( _
   ByVal DocType As System.Integer, _
   ByVal FullMenuName As System.String, _
   ByVal NumSubMenus As System.Integer _
) As System.String
```

```

Dim instance As IFrame
Dim DocType As System.Integer
Dim FullMenuName As System.String
Dim NumSubMenus As System.Integer
Dim value As System.String
 
value = instance.IGetSubMenus(DocType, FullMenuName, NumSubMenus)
```

```

System.string IGetSubMenus( 
   System.int DocType,
   System.string FullMenuName,
   System.int NumSubMenus
)
```

```

System.String^ IGetSubMenus( 
   System.int DocType,
   System.String^ FullMenuName,
   System.int NumSubMenus
) 
```

#### Parameters

*DocType*
:   Type of document as defined by [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*FullMenuName*
:   Full name of menu

*NumSubMenus*
:   Number of submenus

#### Return Value

- in-process, unmanaged C++: Pointer to an array of the names of the submenus of size NumSubMenus

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IFrame::GetSubMenuCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.md) before calling this method to get the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md)  
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md)  
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.md)  
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.md)

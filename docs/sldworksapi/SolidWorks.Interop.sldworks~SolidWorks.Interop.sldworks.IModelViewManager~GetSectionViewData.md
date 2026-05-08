# GetSectionViewData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData`

Gets access to the data of the specified section view.
Gets access to the data of the specified section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSectionViewData( _
   ByVal ViewName As System.String _
) As SectionViewData
```

```

Dim instance As IModelViewManager
Dim ViewName As System.String
Dim value As SectionViewData
 
value = instance.GetSectionViewData(ViewName)
```

```

SectionViewData GetSectionViewData( 
   System.string ViewName
)
```

```

SectionViewData^ GetSectionViewData( 
   System.String^ ViewName
) 
```

#### Parameters

*ViewName*
:   Name of the section view or an empty string for the active section view

#### Return Value

[Section view data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)

Remarks

If the specified string refers to a non-existent section view or a view that is not sectioned, then this method returns Nothing or null.

Example

[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)  
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)  
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md)  
[IModelViewManager::CreateSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.md)  
[IModelViewManager::RemoveSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView.md)

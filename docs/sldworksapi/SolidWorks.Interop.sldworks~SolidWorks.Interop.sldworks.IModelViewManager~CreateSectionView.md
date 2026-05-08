# CreateSectionView Method (IModelViewManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView`

Creates a section view in parts and assemblies.
Creates a section view in parts and assemblies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSectionView( _
   ByVal SectionData As SectionViewData _
) As System.Boolean
```

```

Dim instance As IModelViewManager
Dim SectionData As SectionViewData
Dim value As System.Boolean
 
value = instance.CreateSectionView(SectionData)
```

```

System.bool CreateSectionView( 
   SectionViewData SectionData
)
```

```

System.bool CreateSectionView( 
   SectionViewData^ SectionData
) 
```

#### Parameters

*SectionData*
:   [Section view data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)

#### Return Value

True if the section view is created, false if not (**see** **Remarks**)

Remarks

To create a section view in a part or assembly:

1. Use [IModelViewManager::CreateSectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.md) to create the SectionViewData object.
2. Set the properties of [ISectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md).
3. Use IModelViewManager::CreateSectionView to create the section view. This method only returns whether it successfully created the section view. It does not return whether it created valid section bodies. Set [ISectionViewData::Redraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~Redraw.md) to true to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views.

Example

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)  
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)  
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::GetSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData.md)  
[IModelViewManager::RemoveSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView.md)

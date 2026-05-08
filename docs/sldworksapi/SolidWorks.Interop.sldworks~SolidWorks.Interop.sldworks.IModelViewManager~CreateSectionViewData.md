# CreateSectionViewData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData`

Creates an empty ISectionViewData object whose properties you set before creating a section view in a part or an assembly.
Creates an empty [ISectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md) object whose properties you set before [creating a section view in a part or an assembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSectionViewData() As SectionViewData
```

```

Dim instance As IModelViewManager
Dim value As SectionViewData
 
value = instance.CreateSectionViewData()
```

```

SectionViewData CreateSectionViewData()
```

```

SectionViewData^ CreateSectionViewData(); 
```

#### Return Value

[Section view data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)

Remarks

To create a section view in a part or assembly:

1. Use this method to create the SectionViewData object.
2. Set the properties of [ISectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md).
3. Use [IModelViewManager::CreateSectionView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md) to create the section view. IModelViewManager::CreateSectionView only returns whether it successfully created the section view. It does not return whether it created valid section bodies. Set [ISectionViewData::Redraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~Redraw.md) to true to have IModelViewManager::CreateSectionView validate and return a status for section bodies.

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

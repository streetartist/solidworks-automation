# RemoveSectionView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView`

Removes a section view from a part and assembly.
Removes a section view from a part and assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveSectionView() As System.Boolean
```

```

Dim instance As IModelViewManager
Dim value As System.Boolean
 
value = instance.RemoveSectionView()
```

```

System.bool RemoveSectionView()
```

```

System.bool RemoveSectionView(); 
```

#### Return Value

True if the section view is removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md)  
[IModelViewManager::CreateSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.md)  
[IModelViewManager::GetSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData.md)  
[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)

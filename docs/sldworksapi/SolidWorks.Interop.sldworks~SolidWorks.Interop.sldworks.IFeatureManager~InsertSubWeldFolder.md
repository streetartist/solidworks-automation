# InsertSubWeldFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder`

Creates a sub weld folder feature containing solid bodies that are pre-selected in the user interface.
Creates a sub weld folder feature containing solid bodies that are pre-selected in the user interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSubWeldFolder() As Feature
```

```

Dim instance As IFeatureManager
Dim value As Feature
 
value = instance.InsertSubWeldFolder()
```

```

Feature InsertSubWeldFolder()
```

```

Feature^ InsertSubWeldFolder(); 
```

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

The part must contain a weldment folder (Solid Bodies or Cut List) to create a sub-weldment folder. See [IFeatureManager::InsertWeldmentFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentFeature.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertSubWeldFolder2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder2.md)

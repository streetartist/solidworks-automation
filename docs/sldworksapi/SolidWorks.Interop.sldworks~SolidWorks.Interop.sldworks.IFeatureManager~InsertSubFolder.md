# InsertSubFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubFolder`

Creates a subfolder in the Solid Bodies folder in the FeatureManager design tree and moves the selected solid bodies or subfolders in the Solid Bodies folder to the new subfolder.
Creates a subfolder in the Solid Bodies folder in the FeatureManager design tree and moves the selected solid bodies or subfolders in the Solid Bodies folder to the new subfolder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSubFolder() As Feature
```

```

Dim instance As IFeatureManager
Dim value As Feature
 
value = instance.InsertSubFolder()
```

```

Feature InsertSubFolder()
```

```

Feature^ InsertSubFolder(); 
```

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object, the new subfolder

Remarks

This method requires that the features (solid bodies or subfolders or both) be selected interactively or programmatically. To select the features programmatically, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) and pass the feature names and the appropriate object types and the selection coordinates 0,0,0. To determine the feature names and object types, use the [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) methods, respectively.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)

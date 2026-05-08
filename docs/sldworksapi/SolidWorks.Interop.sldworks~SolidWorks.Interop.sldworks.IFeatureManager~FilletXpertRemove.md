# FilletXpertRemove Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove`

Deletes the fillets on the selected faces.
Deletes the fillets on the selected faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FilletXpertRemove() As Feature
```

```

Dim instance As IFeatureManager
Dim value As Feature
 
value = instance.FilletXpertRemove()
```

```

Feature FilletXpertRemove()
```

```

Feature^ FilletXpertRemove(); 
```

#### Return Value

Pointer to [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::FeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.md)  
[IFeatureManager::FilletXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.md)

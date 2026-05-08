# FeatureAdvancedTableDrivenPattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureAdvancedTableDrivenPattern`

Obsolete. See IFeatureManager::CreateFeature and the Remarks in IDimPatternFeatureData.
Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) and the Remarks in [IDimPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureAdvancedTableDrivenPattern() As Feature
```

```

Dim instance As IFeatureManager
Dim value As Feature
 
value = instance.FeatureAdvancedTableDrivenPattern()
```

```

Feature FeatureAdvancedTableDrivenPattern()
```

```

Feature^ FeatureAdvancedTableDrivenPattern(); 
```

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This method inserts a variable pattern feature, which uses a table to store the dimensions and values of the pattern instances.

Call this method after calling [IFeatureManager::InsertVaryInstanceOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride.md) to create an advanced variable pattern feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)

# EditFreeze Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze`

Obsolete. Superseded by IFeatureManager::EditFreeze2.
Obsolete. Superseded by [IFeatureManager::EditFreeze2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditFreeze( _
   ByVal Location As System.Integer, _
   ByVal FeatureName As System.String, _
   ByVal UpdateAllConfigs As System.Boolean _
) As System.Integer
```

```

Dim instance As IFeatureManager
Dim Location As System.Integer
Dim FeatureName As System.String
Dim UpdateAllConfigs As System.Boolean
Dim value As System.Integer
 
value = instance.EditFreeze(Location, FeatureName, UpdateAllConfigs)
```

```

System.int EditFreeze( 
   System.int Location,
   System.string FeatureName,
   System.bool UpdateAllConfigs
)
```

```

System.int EditFreeze( 
   System.int Location,
   System.String^ FeatureName,
   System.bool UpdateAllConfigs
) 
```

#### Parameters

*Location*
:   Location as defined in [swMoveFreezeBarTo\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFreezeBarTo_e.html)

*FeatureName*
:   Name of the feature

*UpdateAllConfigs*
:   True to update all configurations, false to not

#### Return Value

0 indicates that the freeze bar did not move to the specified location in the FeatureManager design tree; a non-0 value indicates that the freeze bar did move to the specified location in the FeatureManager design tree

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.md)  
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.md)  
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.md)  
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.md)  
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.md)  
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.md)

# IsFrozen Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen`

Gets whether this feature is frozen.
Gets whether this feature is frozen.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsFrozen() As System.Boolean
```

```

Dim instance As IFeature
Dim value As System.Boolean
 
value = instance.IsFrozen()
```

```

System.bool IsFrozen()
```

```

System.bool IsFrozen(); 
```

#### Return Value

True if the feature is frozen, false if not (see **Remarks**)

Remarks

When a feature is frozen, you cannot edit the feature and the feature is excluded from rebuilds of the model.

Example

[Get Whether Feature is Frozen (VBA)](Get_Whether_Feature_is_Locked_Example_VB.htm)  
[Get Whether Feature is Frozen (VB.NET)](Get_Whether_Feature_is_Locked_Example_VBNET.htm)  
[Get Whether Feature is Frozen (C#)](Get_Whether_Feature_is_Locked_Example_CSharp.htm)  
[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)  
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)  
[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.md)  
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.md)  
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.md)  
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.md)  
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.md)  
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.md)  
[IFeatureManager::InsertFeatureLock Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureLock.md)

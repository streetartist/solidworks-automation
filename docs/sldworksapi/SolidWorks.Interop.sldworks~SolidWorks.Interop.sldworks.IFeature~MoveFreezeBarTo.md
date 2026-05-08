# MoveFreezeBarTo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo`

Obsolete. Superseded by IFeature::MoveFreezeBarTo2.
Obsolete. Superseded by [IFeature::MoveFreezeBarTo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MoveFreezeBarTo( _
   ByVal Location As System.Integer, _
   ByVal UpdateAllConfigs As System.Boolean _
) As System.Integer
```

```

Dim instance As IFeature
Dim Location As System.Integer
Dim UpdateAllConfigs As System.Boolean
Dim value As System.Integer
 
value = instance.MoveFreezeBarTo(Location, UpdateAllConfigs)
```

```

System.int MoveFreezeBarTo( 
   System.int Location,
   System.bool UpdateAllConfigs
)
```

```

System.int MoveFreezeBarTo( 
   System.int Location,
   System.bool UpdateAllConfigs
) 
```

#### Parameters

*Location*
:   - [swMoveFreezeBarTo\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFreezeBarTo_e.html).swMoveFreezeBarToBeforeFeature  
        
      -or-

    - swMoveFreezeBarTo\_e.swMoveFreezeBarToAfterFeature

*UpdateAllConfigs*
:   True to update all configurations, false to not

#### Return Value

0 indicates that the freeze bar did not move to the specified location in the FeatureManager design tree; a non-0 value indicates that the freeze bar did move to the specified location in the FeatureManager design tree

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.md)  
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.md)  
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.md)  
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.md)  
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.md)  
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.md)

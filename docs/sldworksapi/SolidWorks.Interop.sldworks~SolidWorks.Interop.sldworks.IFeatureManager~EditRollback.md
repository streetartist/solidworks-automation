# EditRollback Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditRollback`

Rolls back or forward the rollback bar to a specific location in the FeatureManager design tree.
Rolls back or forward the rollback bar to a specific location in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditRollback( _
   ByVal Location As System.Integer, _
   ByVal Feature As System.String _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Location As System.Integer
Dim Feature As System.String
Dim value As System.Boolean
 
value = instance.EditRollback(Location, Feature)
```

```

System.bool EditRollback( 
   System.int Location,
   System.string Feature
)
```

```

System.bool EditRollback( 
   System.int Location,
   System.String^ Feature
) 
```

#### Parameters

*Location*
:   Location to which to move the rollback bar as defined in [swMoveRollbackBarTo\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveRollbackBarTo_e.html)

*Feature*
:   Name of the feature

#### Return Value

True if moving the rollback bar back or forward was successful, false if not

Remarks

When the model is in a rollback state, it reverts to an earlier state, suppressing recently added features. You can add new features or edit existing features while the model is in the rolled-back state.

Example

[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)  
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)  
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeature::IsRolledBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsRolledBack.md)

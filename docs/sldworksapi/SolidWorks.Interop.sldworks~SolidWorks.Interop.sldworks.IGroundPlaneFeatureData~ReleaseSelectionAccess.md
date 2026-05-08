# ReleaseSelectionAccess Method (IGroundPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~ReleaseSelectionAccess`

Releases access to the selections that define this ground plane feature.
Releases access to the selections that define this ground plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ReleaseSelectionAccess() 
```

```

Dim instance As IGroundPlaneFeatureData
 
instance.ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess(); 
```

Remarks

[IGroundPlaneFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~AccessSelections.md) puts the model into a rollback state to allow access to the selections that define this ground plane feature.

Use this method to restore the rollback state if you did not modify the ground plane feature, or use [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) if you did modify the ground plane feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGroundPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.md)  
[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.md)

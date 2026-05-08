# ReleaseSelectionAccess Method (IFillSurfaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ReleaseSelectionAccess`

Releases access to selections that define this fill-surface feature.
Releases access to selections that define this fill-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ReleaseSelectionAccess() 
```

```

Dim instance As IFillSurfaceFeatureData
 
instance.ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess(); 
```

Remarks

[IFillSurfaceFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~AccessSelections.md) and [IFillSurfaceFeatureData::IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IAccessSelections.md) put the model into a rollback state to allow access to the selections that define the fill-surface feature.

Use this method to restore the rollback state if you did not modify the fill-surface feature, or use [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) if you did modify the fill-surface feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)

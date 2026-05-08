# ReleaseSelectionAccess Method (IDomeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ReleaseSelectionAccess`

Releases access to the selections used to define this dome feature.
Releases access to the selections used to define this dome feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ReleaseSelectionAccess() 
```

```

Dim instance As IDomeFeatureData2
 
instance.ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess(); 
```

Remarks

[IDomeFeatureData2::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~AccessSelections.md) and [IDomeFeatureData2::IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IAccessSelections.md) put the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) if you did.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md)  
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.md)

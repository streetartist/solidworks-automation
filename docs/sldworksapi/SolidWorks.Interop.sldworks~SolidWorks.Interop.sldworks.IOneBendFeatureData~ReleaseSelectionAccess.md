# ReleaseSelectionAccess Method (IOneBendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReleaseSelectionAccess`

Accesses the selections that describe this bend feature.
Accesses the selections that describe this bend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ReleaseSelectionAccess() 
```

```

Dim instance As IOneBendFeatureData
 
instance.ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess(); 
```

Remarks

[IOneBendFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~AccessSelections.md) and [IOneBendFeatureDAta::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IAccessSelections2.md) put the model in a rollback state to allow access to the selections that define the bend feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) if you did modify the feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)

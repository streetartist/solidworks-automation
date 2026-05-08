# ReleaseSelectionAccess Method (IFoldsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~ReleaseSelectionAccess`

Releases access to selections that describe this fold feature.
Releases access to selections that describe this fold feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ReleaseSelectionAccess() 
```

```

Dim instance As IFoldsFeatureData
 
instance.ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess()
```

```

void ReleaseSelectionAccess(); 
```

Remarks

[IFoldsFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~AccessSelections.md) and [IFoldsFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IAccessSelections2.md) put the model into a rollback state to allow access to the selections that define the fold feature.

Use this method to restore the rollback state if you did not modify the fold feature, or use [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) if you did modify the fold feature.

Example

[Insert and Access Fold Feature (C#)](Insert_and_Access_Fold_Feature_Example_CSharp.htm)  
[Insert and Access Fold Feature (VB.NET)](Insert_and_Access_Fold_Feature_Example_VBNET.htm)  
[Insert and Access Fold Feature (VBA)](Insert_and_Access_Fold_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.md)  
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.md)

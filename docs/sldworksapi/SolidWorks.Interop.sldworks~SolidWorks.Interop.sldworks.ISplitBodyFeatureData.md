# ISplitBodyFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData`

Allows access to a Split feature.
Allows access to a Split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISplitBodyFeatureData 
```

```

Dim instance As ISplitBodyFeatureData
```

```

public interface ISplitBodyFeatureData 
```

```

public interface class ISplitBodyFeatureData 
```

Remarks

[IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) return:

- **Split** for a feature that was created by splitting a part into multiple parts by using either [IFeatureManager::PostSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md) or the **Split** feature in the user interface. You can access a split-body feature's data using the ISplitBodyFeatureData interface.
- **SplitBody** for a body created by splitting a part and saving the body to a part. You cannot access the data of a split body saved to a part.

Example

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)  
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)  
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.md)

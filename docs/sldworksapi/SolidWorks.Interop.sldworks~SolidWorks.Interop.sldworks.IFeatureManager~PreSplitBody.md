# PreSplitBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody`

Obsolete. Superseded by IFeatureManager::PreSplitBody2.
Obsolete. Superseded by [IFeatureManager::PreSplitBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PreSplitBody() As System.Object
```

```

Dim instance As IFeatureManager
Dim value As System.Object
 
value = instance.PreSplitBody()
```

```

System.object PreSplitBody()
```

```

System.Object^ PreSplitBody(); 
```

#### Return Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that result from splitting a body

Remarks

To create a split-body feature:

1. Select the cutting tools.
2. Call this method to get all of the bodies that will result from the split operation.
3. Create the split-body feature using [IFeatureManager::PostSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md).

To find out if the bodies in a split-body feature were consumed, use [ISplitBodyFeatureData::Consume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)

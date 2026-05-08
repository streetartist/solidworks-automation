# PreSplitBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody2`

Gets all of the bodies created by splitting a part.
Gets all of the bodies created by splitting a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PreSplitBody2() As System.Object
```

```

Dim instance As IFeatureManager
Dim value As System.Object
 
value = instance.PreSplitBody2()
```

```

System.object PreSplitBody2()
```

```

System.Object^ PreSplitBody2(); 
```

#### Return Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that result from splitting a part (see **Remarks**)

Remarks

The difference between this method and the now obsolete IFeatureManager::PreSplitBody is that this method supports the splitting of surfaces.

To create a Split feature:

1. Select the cutting tools to use to split the part into multiple bodies.
2. Call this method to get all of the split bodies.
3. Create the Split feature using [IFeatureManager::PostSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md).

To find out whether the bodies in a Split feature are consumed, use [ISplitBodyFeatureData::Consume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~Consume.md).

Example

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)  
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)  
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISplitBodyFeatureData::GetSplitBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md)  
[ISplitBodyFeatureData::SetSplitBodies2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md)

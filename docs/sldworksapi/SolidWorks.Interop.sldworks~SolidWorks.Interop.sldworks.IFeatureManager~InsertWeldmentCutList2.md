# InsertWeldmentCutList2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentCutList2`

Inserts a cut-list-item folder feature containing the specified weldment bodies.
Inserts a cut-list-item folder feature containing the specified weldment bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertWeldmentCutList2( _
   ByVal Bodies As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Bodies As System.Object
Dim value As Feature
 
value = instance.InsertWeldmentCutList2(Bodies)
```

```

Feature InsertWeldmentCutList2( 
   System.object Bodies
)
```

```

Feature^ InsertWeldmentCutList2( 
   System.Object^ Bodies
) 
```

#### Parameters

*Bodies*
:   Array of [Body2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) objects

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Insert Weldment Cut List Example #2 (VBA)](Insert_Weldment_Cut_List2_Example_VB.htm)  
[Insert Weldment Cut List Example #2 (VB.NET)](Insert_Weldment_Cut_List2_Example_VBNET.htm)  
[Insert Weldment Cut List Example #2 (C#)](Insert_Weldment_Cut_List2_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md)  
[IFeatureManager::InsertWeldmentCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentCutList.md)

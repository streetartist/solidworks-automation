# InsertCombineFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCombineFeature`

Combines the specified bodies in the multibody part to create a combine feature.
Combines the specified bodies in the multibody part to create a combine feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCombineFeature( _
   ByVal OperationType As System.Integer, _
   ByVal MainBody As Body2, _
   ByVal ToolVar As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim OperationType As System.Integer
Dim MainBody As Body2
Dim ToolVar As System.Object
Dim value As Feature
 
value = instance.InsertCombineFeature(OperationType, MainBody, ToolVar)
```

```

Feature InsertCombineFeature( 
   System.int OperationType,
   Body2 MainBody,
   System.object ToolVar
)
```

```

Feature^ InsertCombineFeature( 
   System.int OperationType,
   Body2^ MainBody,
   System.Object^ ToolVar
) 
```

#### Parameters

*OperationType*
:   Operation as defined in [swBodyOperationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyOperationType_e.html)

*MainBody*
:   | If OperationType is ... | Then set MainBody to ... |
    | --- | --- |
    | swBodyOperationType\_e.SWBODYADD | Nothing or null |
    | swBodyOperationType\_e.SWBODYCUT | Target [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) |
    | swBodyOperationType\_e.SWBODYINTERSECT | Nothing or null |

    (See **Remarks**)

*ToolVar*
:   Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to combine (see **Remarks**)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

You can either call this method, directly passing in the bodies with MainBody and ToolVar, or you can:

1. Select the bodies using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) as follows:

   | To select... | Use Mark... |
   | --- | --- |
   | MainBody | 1 |
   | ToolVar bodies | 2 |
2. Call this method, setting MainBody to Nothing or null and ToolVar to an empty array.

See the SOLIDWORKS Help for more information about the combine feature.

Example

[Combine Bodies (C#)](Combine_Bodies_Example_CSharp.htm)  
[Combine Bodies (VB.NET)](Combine_Bodies_Example_VBNET.htm)  
[Combine Bodies (VBA)](Combine_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::IInsertCombineFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertCombineFeature.md)  
[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.md)

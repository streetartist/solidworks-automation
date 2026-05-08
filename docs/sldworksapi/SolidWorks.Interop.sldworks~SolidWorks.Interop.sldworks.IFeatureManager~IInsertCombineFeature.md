# IInsertCombineFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertCombineFeature`

Combines the specified bodies in the multibody part to create a combine feature.
Combines the specified bodies in the multibody part to create a combine feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertCombineFeature( _
   ByVal OperationType As System.Integer, _
   ByVal MainBody As Body2, _
   ByVal ToolsCount As System.Integer, _
   ByRef ToolsArr As Body2 _
) As Feature
```

```

Dim instance As IFeatureManager
Dim OperationType As System.Integer
Dim MainBody As Body2
Dim ToolsCount As System.Integer
Dim ToolsArr As Body2
Dim value As Feature
 
value = instance.IInsertCombineFeature(OperationType, MainBody, ToolsCount, ToolsArr)
```

```

Feature IInsertCombineFeature( 
   System.int OperationType,
   Body2 MainBody,
   System.int ToolsCount,
   ref Body2 ToolsArr
)
```

```

Feature^ IInsertCombineFeature( 
   System.int OperationType,
   Body2^ MainBody,
   System.int ToolsCount,
   Body2^% ToolsArr
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

*ToolsCount*
:   Number of bodies to combine

*ToolsArr*
:   - in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to combine of size ToolsCount (see **Remarks**)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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

See the SOLIDWORKS Help for more information about the combined feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertCombineFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCombineFeature.md)  
[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.md)

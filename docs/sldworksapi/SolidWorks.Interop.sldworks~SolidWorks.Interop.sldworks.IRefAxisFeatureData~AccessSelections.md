# AccessSelections Method (IRefAxisFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~AccessSelections`

Gains access to the selections that define this reference axis feature.
Gains access to the selections that define this reference axis feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

```

Dim instance As IRefAxisFeatureData
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean
 
value = instance.AccessSelections(TopDoc, Component)
```

```

System.bool AccessSelections( 
   System.object TopDoc,
   System.object Component
)
```

```

System.bool AccessSelections( 
   System.Object^ TopDoc,
   System.Object^ Component
) 
```

#### Parameters

*TopDoc*
:   Top-level document (see **Remarks**)

*Component*
:   Component in which the feature is to be modified (see **Remarks**)

#### Return Value

True if the selections were successfully accessed, false if not

Remarks

|  |  |
| --- | --- |
| **To modify a feature in a...** | **Then...** |
| Part | - TopDoc argument is the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) for the part - Component argument is NULL |
| Assembly | - TopDoc is the IModelDoc2 object for the assembly - Component argument is the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) if you modified the feature
- [IRefAxisFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ReleaseSelectionAccess.md) if you did not

Example

[Get Selections for Reference Axis Feature (C#)](Get_Selections_for_Reference_Axis_Feature_Example_CSharp.htm)  
[Get Selections for Reference Axis Feature (VB.NET)](Get_Selections_for_Reference_Axis_Feature_Example_VBNET.htm)  
[Get Selections for Reference Axis Feature (VBA)](Get_Selections_for_Reference_Axis_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.md)  
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.md)  
[IRefAxisFeatureData::IAccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IAccessSelections.md)

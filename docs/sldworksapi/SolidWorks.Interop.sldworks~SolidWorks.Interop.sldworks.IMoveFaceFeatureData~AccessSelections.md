# AccessSelections Method (IMoveFaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~AccessSelections`

Gains access to selections that define this Move Face feature.
Gains access to selections that define this Move Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AccessSelections( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

```

Dim instance As IMoveFaceFeatureData
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean
 
value = instance.AccessSelections(TopDoc, Component)
```

```

System.bool AccessSelections( 
   ModelDoc2 TopDoc,
   Component2 Component
)
```

```

System.bool AccessSelections( 
   ModelDoc2^ TopDoc,
   Component2^ Component
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
- [IMoveFaceFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ReleaseSelectionAccess.md) if you did not

Example

[Change Direction Reference of Move Face Feature (VBA)](Change_Direction_Reference_of_Move_Face_Feature_Example_VB.htm)  
[Change Faces of Move Face Feature (VBA)](Change_Faces_of_Move_Face_Feature_Example_VB.htm)  
[Rotate Move Face Feature (VB.NET)](Rotate_Move_Face_Feature_Example_VBNET.htm)  
[Create and Modify Move Face Feature (C#)](Create_and_Modify_Move_Face_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)

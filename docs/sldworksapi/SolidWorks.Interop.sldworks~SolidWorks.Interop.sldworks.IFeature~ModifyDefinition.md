# ModifyDefinition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition`

Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::GetDefinition.
Updates the definition of a feature with the new values in an associated feature data object obtained with [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ModifyDefinition( _
   ByVal Data As System.Object, _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

```

Dim instance As IFeature
Dim Data As System.Object
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean
 
value = instance.ModifyDefinition(Data, TopDoc, Component)
```

```

System.bool ModifyDefinition( 
   System.object Data,
   System.object TopDoc,
   System.object Component
)
```

```

System.bool ModifyDefinition( 
   System.Object^ Data,
   System.Object^ TopDoc,
   System.Object^ Component
) 
```

#### Parameters

*Data*
:   Feature data object

*TopDoc*
:   Top-level document (see **Remarks**)

*Component*
:   Component for the feature (see Remarks)

#### Return Value

True if the feature definition modified successfully, false if not

Remarks

If this method returns:

- False, you may have specified invalid properties in the feature data modifier object. The feature definition was not modified, so the feature may have rolled back to its previous state.
- True, the feature was updated using the feature data modifier object provided. This method will return true even if the feature data modifier object does not include any changed properties or references; some feature data modifier objects reject invalid changes before this method is called. For some feature modifications, this method applies the new properties, returns true, but results in a new rebuild error on the feature.

In either case, this method may leave the feature in an unpredictable state due to errors. After calling this method, call [IFeature::GetErrorCode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.md) to ascertain whether the feature has rebuild errors. If so, try again with valid feature data. To correct rebuild errors, call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md). You can also move the rollback bar in the FeatureManager design tree to before and after the feature to correct its state.

You should carefully read specific feature data interface documentation to learn how to correctly specify feature data properties and how this method works with specific features.

| **To modify a feature in...** | **Then TopDoc argument...** |
| --- | --- |
| A part | Is the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object for the part and the Component argument should be Nothing or null |
| An assembly | Should be the assembly IModelDoc2 object and the Component argument should be the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object in which the feature is to be modified |

When you modify a feature in an assembly, this method leaves the assembly in Editing Part mode. You can switch back to editing the assembly by calling [IAssemblyDoc::EditAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditAssembly.md).

Example

[Change Bend Radius of Sheet Metal Part (VBA)](Change_Bend_Radius_of_Sheet_Metal_Part_Example_VB.htm)  
[Get and Set Constraint for Dome Feature (VBA)](Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm)  
[Modify Plane By Editing its Definition (VBA)](Modify_Plane_by_Editing_Its_Definition_Example_VB.htm)  
[Insert and Change DeleteFace Feature (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)  
[Insert and Change DeleteFace Feature (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)  
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.md)  
[IFeature::IModifyDefinition2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md)

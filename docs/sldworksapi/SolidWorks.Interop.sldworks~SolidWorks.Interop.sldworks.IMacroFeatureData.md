# IMacroFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData`

Allows access to the data that defines a macro feature.
Allows access to the data that defines a macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IMacroFeatureData 
```

```

Dim instance As IMacroFeatureData
```

```

public interface IMacroFeatureData 
```

```

public interface class IMacroFeatureData 
```

Remarks

|  |  |
| --- | --- |
| **Macro features can...** | **For the** [**rebuild function**](sldworksapiprogguide.chm::/Macro_Features/Rebuild_Function.htm) **only, the macro associated with a macro feature cannot:** |
| - be inserted into a part, assembly, or drawing document - create multiple bodies - edit multiple existing bodies | - insert a feature from a macro feature in the same model - edit definitions of other features if these features are in the same model as the macro feature - rebuild, roll back, or roll forward the FeatureManager design tree   NOTE: These limitations are intended to prevent nested-feature regeneration in the model that contains the macro feature. |

When the feature is creating multiple bodies, then the return value from the rebuild function should contain the array of bodies that are the result of the operation. [IMacroFeatureData::EditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.md) is not expected to contain a body when the rebuild function returns to SOLIDWORKS.

When the feature is modifying a body and the result is multiple bodies, then IMacroFeatureData::EditBodies should contain all of the resulting bodies.

Whether creating multiple bodies or modifying a body that results in multiple bodies, call [IMacroFeatureData::EnableMultiBodyConsume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume.md) from the [rebuild](sldworksapiprogguide.chm::/Macro_Features/Rebuild_Function.htm) function to specify whether multiple bodies replace or append the original edit body in the FeatureManager design tree Solid Bodies folder.

If your application allows the user to decide which bodies to keep, your application must determine what it means to select the bodies and subsequently store the selected bodies with the feature.

To edit a macro feature in a drawing, do not use [IMacroFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~AccessSelections.md), [IMacroFeatureData::IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IAccessSelections.md),  or [IMacroFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ReleaseSelectionAccess.md) because the concept of a rollback bar does not exist. You can still use [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) to update an IMacroFeatureData object.

If the user decides to cancel the changes made to the IMacroFeatureData object, then discard the IMacroFeatureData object. This action is equivalent to using IMacroFeatureData::ReleaseSelectionAccess.

See [Overview of Macro Features](sldworksapiprogguide.chm::/Macro_Features/Overview_of_Macro_Features.htm) for more information.

Example

[Create Macro Feature Subfeature (VBA)](Create_Macro_Feature_Subfeature_Example_VB.htm)  
[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)  
[Assign Tracking ID Using Macro Feature (VBA)](Assign_Tracking_ID_Using_Macro_Feature_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::IInsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.md)  
[IFeatureManager::InsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md)

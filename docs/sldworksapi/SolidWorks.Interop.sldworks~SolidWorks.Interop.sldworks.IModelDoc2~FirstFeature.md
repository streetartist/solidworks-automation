# FirstFeature Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature`

Gets the first feature in the document.
Gets the first feature in the document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FirstFeature() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.FirstFeature()
```

```

System.object FirstFeature()
```

```

System.Object^ FirstFeature(); 
```

#### Return Value

First [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) in the document

Remarks

This method:

- is identical to [IPartDoc::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.md), but is available on the IModelDoc2 interface to include access to assemblies and drawings.
- can access the first feature even if it is suppressed.
- returns features in the current order for the model, and this order changes when the model is edited.

Your application should not assume that:

- features retain the same relative or absolute position throughout the model’s lifetime. For example, you should not assume that Sketch1 always appears before Sketch2.
- any feature has a specific name. Because features can be renamed, you cannot assume that the first reference plane feature is named Plane1.

When traversing the FeatureManager design tree, your application should use [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) and [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to identify specific features instead of relying solely on [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md).

This method returns features in the model definition order, which is not the same as the order displayed in the user interface. See [ITreeControlItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md) for details.

To access the next feature in the FeatureManager design tree and subfeatures, use [IFeature::GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md) or [IFeature::IGetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.md) and [IFeature::GetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.md) or [IFeature::IGetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.md) methods, respectively.

Example

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)  
[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)  
[Select Plane (VBA)](Select_Plane_Example_VB.htm)  
[Set Dimensions to Mid-Tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)  
[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)  
[Traverse Assembly and Hide All Sketches (VBA)](Traverse_Assembly_and_Hide_All_Sketches_Example_VB.htm)  
[Insert and Change DeleteFace Feature (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)  
[Insert and Change DeleteFace Feature (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)  
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)  
[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)  
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)  
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureCount.md)  
[IModelDoc2::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.md)  
[IModelDoc2::IFeatureByPositionReverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.md)  
[IModelDoc2::FeatureByPositionReverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.md)  
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.md)  
[IPartDoc::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFirstFeature.md)  
[IComponent2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.md)

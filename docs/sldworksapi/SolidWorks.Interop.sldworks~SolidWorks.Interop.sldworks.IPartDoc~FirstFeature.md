# FirstFeature Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature`

Gets the first feature in the part.
Gets the first feature in the part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FirstFeature() As System.Object
```

```

Dim instance As IPartDoc
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

First [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) in the part

Remarks

This method returns features in the current order for the part, and this order changes when the part is edited.

Your application should not assume that:

- features retain the same relative or absolute position throughout the part’s lifetime. For example, you should not assume that Sketch1 always appears before Sketch2.
- any feature has a specific name. Because features can be renamed, you cannot assume that the first reference plane feature is named Plane1.

When traversing the FeatureManager design tree, your application should use [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) and [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to identify specific features instead of relying solely on [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md).

This method returns features in the model definition order, which is not the same as the order displayed in the user interface. See [ITreeControlItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md) for details.

If a feature is suppressed, then this method can still access the feature.

To access the next feature in the FeatureManager design tree and subfeatures, use [IFeature::GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md) or [IFeature::IGetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.md) and [IFeature::GetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.md) or [IFeature::IGetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.md).

Example

[Suppress or Unsuppress Feature (VBA)](Feature_Suppression_Example_VB.htm)  
[Traverse Subfeatures (VBA)](Traverse_SubFeatures_Example_VB.htm)  
[Autodimension All Sketches (C#)](Autodimension_All_Sketches_Example_CSharp.htm)  
[Autodimension All Sketches (VB.NET)](Autodimension_All_Sketches_Example_VBNET.htm)  
[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFirstFeature.md)  
[IComponent2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.md)  
[IModelDoc2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md)  
[IModelDoc2::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.md)  
[IPartDoc::ReorderFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.md)

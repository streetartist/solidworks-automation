# FeatureByPositionReverse Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureByPositionReverse`

Gets the nth from last feature in the document.
Gets the nth from last feature in the document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureByPositionReverse( _
   ByVal Num As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim Num As System.Integer
Dim value As System.Object
 
value = instance.FeatureByPositionReverse(Num)
```

```

System.object FeatureByPositionReverse( 
   System.int Num
)
```

```

System.Object^ FeatureByPositionReverse( 
   System.int Num
) 
```

#### Parameters

*Num*
:   Number of feature from the last feature in the FeatureManager design tree; 0 is the last feature in FeatureManager design tree

#### Return Value

Pointer to the *n*th from last [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) in the document

Remarks

This method returns features in the current order for the model, and this order changes when the model is edited.

Your application should not assume that:

- features retain the same relative or absolute position throughout the model’s lifetime. For example, you should not assume that Sketch1 always appears before Sketch2.
- any feature has a specific name. Because features can be renamed, you cannot assume that the first reference plane feature is named Plane1.

When traversing the FeatureManager design tree, your application should use [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) and [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to identify specific features instead of relying solely on [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md).

This method returns features in the model definition order, which is not the same as the order displayed in the user interface. See [ITreeControlItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md) for details.

Because SOLIDWORKS does not guarantee the name or positioning of default features, your application should not make any assumptions in this area. If your application is trying to access geometric features (i.e., sketches, fillets, bosses, reference surfaces, etc.) using IModelDoc2::FeatureByPositionReverse, then it is safest to determine the number of default features at the top and bottom of the list for each particular document. This could be done once for each document by traversing the FeatureManager design tree using [IModelDoc2::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md) and [IFeature::GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md). Based on the feature type, IFeature::GetTypeName, you can recognize where new features will be placed in the FeatureManager design tree upon creation.

For example, a new fillet is created at position (n-1) where n is the total number of features in the part. Therefore, to obtain this feature, then specify 1 for PositionFromEnd. This allows you to obtain the newly created fillet feature which is 1 from the bottom of the list.

If you are using this method to obtain the last feature object created by your application, then, as a precaution, you might also want to check the feature count immediately before your feature creation and immediately after your feature creation. If the feature count has increased by 1, then it is relatively safe to assume that only your application has modified the document and added a feature. However, this is not a guaranteed methodology because another third-party applications might be running and might have also modified your document. Feature count can be determined by calling [IModelDoc2::GetFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureCount.md). However, IModelDoc2::GetFeatureCount does not recognize Sheet-Metal and Flat-Pattern folders as features in the FeatureManager design tree. Sheet-Metal and Flat-Pattern folders were introduced in SOLIDWORKS 2013.

To access the first feature in the FeatureManager design tree and sub-features, use IModelDoc2::FirstFeature and [IFeature::GetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.md) methods, respectively.

IModelDoc2::FeatureByPositionReverse can access suppressed features.

Example

[Traverse Features By Reverse Position (C#)](Traverse_Features_By_Reverse_Position_Example_CSharp.htm)  
[Traverse Features By Reverse Position (VB.NET)](Traverse_Features_By_Reverse_Position_Example_VBNET.htm)  
[Traverse Features By Reverse Position (VBA)](Traverse_Features_By_Reverse_Position_Example_VB.htm)  
[Get Features in Reverse Order (C#)](Get_Features_in_Reverse_Order_Example_CSharp.htm)  
[Get Features in Reverse Order (VB.NET)](Get_Features_in_Reverse_Order_Example_VBNET.htm)  
[Get Features in Reverse Order (VBA)](Get_Features_in_Reverse_Order_Example_VB.htm)  
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)  
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)  
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)  
[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IFeatureByPositionReverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.md)

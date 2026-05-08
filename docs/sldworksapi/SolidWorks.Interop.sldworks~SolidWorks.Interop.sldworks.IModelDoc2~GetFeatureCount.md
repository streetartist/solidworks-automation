# GetFeatureCount Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureCount`

Gets the number of features in this document.
Gets the number of features in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureCount() As System.Integer
```

```

Dim instance As IModelDoc2
Dim value As System.Integer
 
value = instance.GetFeatureCount()
```

```

System.int GetFeatureCount()
```

```

System.int GetFeatureCount(); 
```

#### Return Value

Number of features in this document; this number does not include subfeatures

Remarks

The number of features returned by this method does not include subfeatures. Subfeatures include, for example, mate features within a mategroup, drawing views on a sheet, and so on. One way to identify a subfeature is whether it can be returned by:

- [IFeature::GetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.md) or [IFeature::IGetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.md)
- [IFeature::GetNextSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.md) or [IFeature::IGetNextSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.md).

This method returns the number of features returned when traversing the Feature list with [IModelDoc2::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md) or [IModelDoc2::IFirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.md) and [IFeature::GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md) or [IFeature::IGetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.md). This value may be useful in feature traversal or if accessing the feature by position using [IModelDoc2::FeatureByPositionReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.md) or [IModelDoc2::IFeatureByPositionReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.md).

Example

[Traverse Features By Reverse Position (C#)](Traverse_Features_By_Reverse_Position_Example_CSharp.htm)  
[Traverse Features By Reverse Position (VB.NET)](Traverse_Features_By_Reverse_Position_Example_VBNET.htm)  
[Traverse Features By Reverse Position (VBA)](Traverse_Features_By_Reverse_Position_Example_VB.htm)  
[Get Features in Reverse Order (C#)](Get_Features_in_Reverse_Order_Example_CSharp.htm)  
[Get Features in Reverse Order (VB.NET)](Get_Features_in_Reverse_Order_Example_VBNET.htm)  
[Get Features in Reverse Order (VBA)](Get_Features_in_Reverse_Order_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)

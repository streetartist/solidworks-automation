# PatternFeature Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~PatternFeature`

Gets or sets the pattern feature for this derived pattern feature.
Gets or sets the pattern feature for this derived pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternFeature As System.Object
```

```

Dim instance As IDerivedPatternFeatureData
Dim value As System.Object
 
instance.PatternFeature = value
 
value = instance.PatternFeature
```

```

System.object PatternFeature {get; set;}
```

```

property System.Object^ PatternFeature {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) on which to base this derived pattern feature

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Create Derived Pattern Feature (C#)](Create_Derived_Pattern_Feature_Example_CSharp.htm)  
[Create Derived Pattern Feature (VB.NET)](Create_Derived_Pattern_Feature_Example_VBNET.htm)  
[Create Derived Pattern Feature (VBA)](Create_Derived_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.md)  
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.md)  
[IDerivedPatternFeatureData::DrivingFeatureSkippedItemArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~DrivingFeatureSkippedItemArray.md)

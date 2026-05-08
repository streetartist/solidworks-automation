# PatternFeatureArray Property (IFillPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternFeatureArray`

Gets or sets the array of features to pattern in this fill pattern feature.
Gets or sets the array of features to pattern in this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternFeatureArray As System.Object
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Object
 
instance.PatternFeatureArray = value
 
value = instance.PatternFeatureArray
```

```

System.object PatternFeatureArray {get; set;}
```

```

property System.Object^ PatternFeatureArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)s to pattern

Remarks

This property is valid only if [IFillPatternFeatureData::PatternElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternElement.md) is [swPatternElementSelection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html).swFeatureFaces.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

# PatternLayoutType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType`

Gets or sets the layout of the pattern instances within the fill boundary of this fill pattern feature.
Gets or sets the layout of the pattern instances within the fill boundary of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternLayoutType As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
instance.PatternLayoutType = value
 
value = instance.PatternLayoutType
```

```

System.int PatternLayoutType {get; set;}
```

```

property System.int PatternLayoutType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Fill pattern layout type as defined in [swPatternLayoutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html)

Remarks

After specifying this property, specify the following:

- [IFillPatternFeatureData::Margins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Margins.md)
- [IFillPatternFeatureData::PatternDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternDirection.md)
- [IFillPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~GeometryPattern.md)
- [IFillPatternFeatureData::PropagateVisualProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PropagateVisualProperty.md)
- [IFillPatternFeatureData::FeaturesToPatternType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.md)

Specify other properties as required by the settings above.

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

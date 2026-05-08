# ShowSlitInCornerRelief Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief`

Get or set whether to show the slit in the corner relief of this Flat-Pattern feature.
Get or set whether to show the slit in the corner relief of this Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowSlitInCornerRelief As System.Boolean
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean
 
instance.ShowSlitInCornerRelief = value
 
value = instance.ShowSlitInCornerRelief
```

```

System.bool ShowSlitInCornerRelief {get; set;}
```

```

property System.bool ShowSlitInCornerRelief {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the slit in the corner relief of this feature, false to not

Remarks

When you create a rectangular or circular corner relief that is smaller than the bend area, a slit is added so that the part can bend. Setting this property to true makes the slit available in the flat pattern.

This property corresponds to the **Show Slit** option in the Parameters section of the Flat-Pattern PropertyManager.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::CornerTrimReliefType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.md)  
[IFlatPatternFeatureData::GetAddCornerTrim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.md)  
[IFlatPatternFeatureData::SetAddCornerTrim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetAddCornerTrim.md)  
[IFlatPatternFeatureData::CornerTreatment Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTreatment.md)  
[IFlatPatternFeatureData::CornerTrimRatioToThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.md)  
[IFlatPatternFeatureData::CornerTrimReliefDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.md)  
[IFlatPatternFeatureData::UseRatioToThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.md)

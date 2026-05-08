# GetAddCornerTrim Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim`

Gets whether to add a corner trim to the Flat-Pattern feature.
Gets whether to add a corner trim to the Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAddCornerTrim( _
   ByRef PFeat As Feature _
) As System.Boolean
```

```

Dim instance As IFlatPatternFeatureData
Dim PFeat As Feature
Dim value As System.Boolean
 
value = instance.GetAddCornerTrim(PFeat)
```

```

System.bool GetAddCornerTrim( 
   out Feature PFeat
)
```

```

System.bool GetAddCornerTrim( 
   [Out] Feature^ PFeat
) 
```

#### Parameters

*PFeat*
:   Flat-Pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

#### Return Value

True to add a corner trim, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::CornerTrimRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.md)  
[IFlatPatternFeatureData::CornerTrimReliefDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.md)  
[IFlatPatternFeatureData::CornerTrimReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.md)  
[IFlatPatternFeatureData::UseRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.md)  
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.md)

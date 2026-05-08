# D2IsEqualSpaced Property (ILocalCurvePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2IsEqualSpaced`

Gets or sets whether to use equal spacing between instances of the pattern in Direction 2 for this bidirectional curve-driven component pattern feature.
Gets or sets whether to use equal spacing between instances of the pattern in Direction 2 for this bidirectional curve-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2IsEqualSpaced As System.Boolean
```

```

Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Boolean
 
instance.D2IsEqualSpaced = value
 
value = instance.D2IsEqualSpaced
```

```

System.bool D2IsEqualSpaced {get; set;}
```

```

property System.bool D2IsEqualSpaced {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use equal spacing in Direction 2, false to use the value set by [ILocalCurvePatternFeatureData::D2Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Spacing.md)

Remarks

[ILocalCurvePatternFeatureData::Dir2Specified](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~Dir2Specified.md) must be set to true for this property have an effect.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.md)  
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.md)  
[ILocalCurvePatternFeatureData::D2Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.md)  
[ILocalCurvePatternFeatureData::D2InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2InstanceCount.md)  
[ILocalCurvePatternFeatureData::D2PatternSeedOnly Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2PatternSeedOnly.md)  
[ILocalCurvePatternFeatureData::D2ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2ReverseDirection.md)  
[ILocalCurvePatternFeatureData::D1IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1IsEqualSpaced.md)

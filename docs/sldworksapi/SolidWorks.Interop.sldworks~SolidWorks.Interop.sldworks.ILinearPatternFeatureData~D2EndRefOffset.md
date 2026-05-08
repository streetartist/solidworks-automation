# D2EndRefOffset Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndRefOffset`

Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear pattern feature.
Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2EndRefOffset As System.Double
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Double
 
instance.D2EndRefOffset = value
 
value = instance.D2EndRefOffset
```

```

System.double D2EndRefOffset {get; set;}
```

```

property System.double D2EndRefOffset {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Offset of the last pattern instance from [ILinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndReference.md)

Remarks

This property is valid only if [ILinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndCondition.md) is set to [swPatternEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition\_UpToReference.

Whether to offset instance geometry or a centroid is governed by [ILinearPatternFeatureData::D2EndUseSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndUseSeedReference.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)

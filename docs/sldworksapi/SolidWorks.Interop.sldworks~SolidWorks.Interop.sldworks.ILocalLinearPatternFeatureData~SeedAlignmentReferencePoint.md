# SeedAlignmentReferencePoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SeedAlignmentReferencePoint`

Gets or sets the type of reference point with which to align each pattern instance to the seed feature.
Gets or sets the type of reference point with which to align each pattern instance to the seed feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SeedAlignmentReferencePoint As System.Integer
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Integer
 
instance.SeedAlignmentReferencePoint = value
 
value = instance.SeedAlignmentReferencePoint
```

```

System.int SeedAlignmentReferencePoint {get; set;}
```

```

property System.int SeedAlignmentReferencePoint {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Seed alignment reference point as defined in [swSeedAlignmentReferencePoint\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSeedAlignmentReferencePoint_e.html)

Remarks

This property is valid only if [ILocalLinearPatternFeatureData::AlignToSeed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~AlignToSeed.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)

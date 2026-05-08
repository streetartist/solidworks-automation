# SeedCutFlipShapeDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedCutFlipShapeDirection`

Gets or sets whether to reverse the direction of the seed instance cut of this fill pattern feature.
Gets or sets whether to reverse the direction of the seed instance cut of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SeedCutFlipShapeDirection As System.Boolean
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Boolean
 
instance.SeedCutFlipShapeDirection = value
 
value = instance.SeedCutFlipShapeDirection
```

```

System.bool SeedCutFlipShapeDirection {get; set;}
```

```

property System.bool SeedCutFlipShapeDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of the seed instance cut, false to not

Remarks

This property is valid only if [IFillPatternFeatureData::FeaturesToPatternType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.md) = [swFeaturesToPatternType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut.

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)  
[IFillPatternFeatureData::CreateSeedCutType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.md)

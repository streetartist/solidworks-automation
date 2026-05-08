# CreateSeedCutType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType`

Gets or sets the type of cut for this fill pattern's seed instance.
Gets or sets the type of cut for this fill pattern's seed instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CreateSeedCutType As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
instance.CreateSeedCutType = value
 
value = instance.CreateSeedCutType
```

```

System.int CreateSeedCutType {get; set;}
```

```

property System.int CreateSeedCutType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of seed instance cut as defined in [swCreateSeedCutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSeedCutType_e.html)

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)  
[IFillPatternFeatureData::Diameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Diameter.md)  
[IFillPatternFeatureData::Dimension Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Dimension.md)  
[IFillPatternFeatureData::Diagonal Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Diagonal.md)  
[IFillPatternFeatureData::Rotation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Rotation.md)  
[IFillPatternFeatureData::CreateSeedCutPolygonSides Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutPolygonSides.md)  
[IFillPatternFeatureData::InnerRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~InnerRadius.md)  
[IFillPatternFeatureData::OuterRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~OuterRadius.md)  
[IFillPatternFeatureData::SeedCutFlipShapeDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedCutFlipShapeDirection.md)

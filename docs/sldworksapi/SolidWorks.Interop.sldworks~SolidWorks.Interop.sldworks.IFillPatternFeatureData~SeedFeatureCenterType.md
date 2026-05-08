# SeedFeatureCenterType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenterType`

Gets or sets the type of entity where to place the center of the seed cut feature for this fill pattern feature.
Gets or sets the type of entity where to place the center of the seed cut feature for this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property SeedFeatureCenterType As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
value = instance.SeedFeatureCenterType
```

```

System.int SeedFeatureCenterType {get;}
```

```

property System.int SeedFeatureCenterType {
   System.int get();
}
```

#### Property Value

Type of entity as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)  
[IFillPatternFeatureData::SeedFeatureCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenter.md)

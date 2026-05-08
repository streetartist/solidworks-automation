# SeedFeatureCenter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenter`

Gets or sets the vertex or sketch point where to place the center of the seed cut feature of this fill pattern feature.
Gets or sets the vertex or sketch point where to place the center of the seed cut feature of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SeedFeatureCenter As System.Object
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Object
 
instance.SeedFeatureCenter = value
 
value = instance.SeedFeatureCenter
```

```

System.object SeedFeatureCenter {get; set;}
```

```

property System.Object^ SeedFeatureCenter {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) or [sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) where to place the center of the seed cut feature

Remarks

This property is valid only if [IFillPatternFeatureData::FeaturesToPatternType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.md) = [swFeaturesToPatternType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)  
[IFillPatternFeatureData::SeedFeatureCenterType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenterType.md)

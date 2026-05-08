# CreateSeedCutPolygonSides Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutPolygonSides`

Gets or sets the number of sides in a polygon-cut seed instance of this fill pattern feature.
Gets or sets the number of sides in a polygon-cut seed instance of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CreateSeedCutPolygonSides As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
instance.CreateSeedCutPolygonSides = value
 
value = instance.CreateSeedCutPolygonSides
```

```

System.int CreateSeedCutPolygonSides {get; set;}
```

```

property System.int CreateSeedCutPolygonSides {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of sides in a polygon-cut seed instance

Remarks

This property is valid only if both are true:

- [IFillPatternFeatureData::FeaturesToPatternType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.md) = [swFeaturesToPatternType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut
- [IFillPatternFeatureData::CreateSeedCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.md) = [swCreateSeedCutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSeedCutType_e.html).swCreateSeedCutPolygon

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

# FeaturesToPatternType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType`

Gets or sets the type of object to pattern in this fill pattern feature.
Gets or sets the type of object to pattern in this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeaturesToPatternType As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
instance.FeaturesToPatternType = value
 
value = instance.FeaturesToPatternType
```

```

System.int FeaturesToPatternType {get; set;}
```

```

property System.int FeaturesToPatternType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of object to pattern as defined in [swFeaturesToPatternType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html)

Remarks

| If this property is set to... | Then call... |
| --- | --- |
| swFeaturesToPatternType\_e.swFeaturesToPatternCreateSeedCut | [IFillPatternFeatureData::CreateSeedCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.md) to get or set the type of seed cut to pattern |
| swFeaturesToPatternType\_e.swFeaturesToPatternSelectedFeatures | - [IFillPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternFeatureArray.md) to get or set the array of features to pattern - [IFillPatternFeatureData::PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternFaceArray.md) to get or set the array of faces to pattern - [IFillPatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternBodyArray.md) to get or set the array of bodies to pattern |

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

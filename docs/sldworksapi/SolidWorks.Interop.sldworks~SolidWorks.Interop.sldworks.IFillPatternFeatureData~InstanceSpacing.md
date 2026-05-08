# InstanceSpacing Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~InstanceSpacing`

Gets or sets the distance between the pattern instance centers of this fill pattern feature.
Gets or sets the distance between the pattern instance centers of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InstanceSpacing As System.Double
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Double
 
instance.InstanceSpacing = value
 
value = instance.InstanceSpacing
```

```

System.double InstanceSpacing {get; set;}
```

```

property System.double InstanceSpacing {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance between pattern instance centers

Remarks

| This property is.... | If... |
| --- | --- |
| Always valid | [IFillPatternFeatureData::PatternLayoutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.md) = [swPatternLayoutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutPerforation |
| Only valid | Both are true:  [IFillPatternFeatureData::LayoutSpacingType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~LayoutSpacingType.md) = [swPatternLayoutSpacingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutSpacingType_e.html).swPatternLayoutTargetSpacing  And:  IFillPatternFeatureData::PatternLayoutType is set to one of the following:  - swPatternLayoutType\_e.swPatternLayoutCircle - swPatternLayoutType\_e.swPatternLayoutSquare - swPatternLayoutType\_e.swPatternLayoutPolygon |

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

# LoopSpacing Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~LoopSpacing`

Gets or sets the distance between loops of pattern instances in this fill pattern feature.
Gets or sets the distance between loops of pattern instances in this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LoopSpacing As System.Double
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Double
 
instance.LoopSpacing = value
 
value = instance.LoopSpacing
```

```

System.double LoopSpacing {get; set;}
```

```

property System.double LoopSpacing {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance between loops of pattern instances

Remarks

All fill patterns except those with perforated layouts are created by positioning a pattern seed instance within the fill boundary and copying the pattern in concentric loops about the seed instance. This property sets the spacing between the centers of instances in adjacent pattern loops.

This property is valid only if [IFillPatternFeatureData::PatternLayoutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.md) is set to one of the following:

- [swPatternLayoutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutCircular
- swPatternLayoutType\_e.swPatternLayoutPolygon
- swPatternLayoutType\_e.swPatternLayoutSquare

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

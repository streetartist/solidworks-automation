# PatternLayoutPolygonSides Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutPolygonSides`

Gets or sets the number of sides in the polygonal layout of this fill pattern feature.
Gets or sets the number of sides in the polygonal layout of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternLayoutPolygonSides As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
instance.PatternLayoutPolygonSides = value
 
value = instance.PatternLayoutPolygonSides
```

```

System.int PatternLayoutPolygonSides {get; set;}
```

```

property System.int PatternLayoutPolygonSides {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of sides in the polygonal layout of this fill pattern

Remarks

This property is valid only if [IFillPatternFeatureData::PatternLayoutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.md) = [swPatternLayoutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutPolygon.

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

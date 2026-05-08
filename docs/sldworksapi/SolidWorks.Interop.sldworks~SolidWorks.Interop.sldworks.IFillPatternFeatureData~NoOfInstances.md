# NoOfInstances Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~NoOfInstances`

Gets or sets the number of instances per loop or side of the layout of this fill pattern feature.
Gets or sets the number of instances per loop or side of the layout of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NoOfInstances As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
instance.NoOfInstances = value
 
value = instance.NoOfInstances
```

```

System.int NoOfInstances {get; set;}
```

```

property System.int NoOfInstances {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of instances per loop or side of the pattern layout

Remarks

This property is valid only if both are true:

- [IFillPatternFeatureData::LayoutSpacingType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~LayoutSpacingType.md) = [swPatternLayoutSpacingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutSpacingType_e.html).swPatternLayoutInstances

And:

- [IFillPatternFeatureData::PatternLayoutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.md) is set to one of the following:
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

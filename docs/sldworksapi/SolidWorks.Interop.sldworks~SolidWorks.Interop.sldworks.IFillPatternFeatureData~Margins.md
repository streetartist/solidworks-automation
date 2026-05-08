# Margins Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Margins`

Gets or sets the distance between the fill boundary and the outermost pattern instance in the layout of this fill pattern feature.
Gets or sets the distance between the fill boundary and the outermost pattern instance in the layout of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Margins As System.Double
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Double
 
instance.Margins = value
 
value = instance.Margins
```

```

System.double Margins {get; set;}
```

```

property System.double Margins {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance between the fill boundary and the outermost pattern instance in the layout; 0 for no margin

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)  
[IFillPatternFeatureData::PatternLayoutType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.md)

# PatternDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternDirection`

Gets or sets the direction reference for the layout of this fill pattern feature.
Gets or sets the direction reference for the layout of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternDirection As System.Object
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Object
 
instance.PatternDirection = value
 
value = instance.PatternDirection
```

```

System.object PatternDirection {get; set;}
```

```

property System.Object^ PatternDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Direction reference for the pattern layout

Remarks

Before calling this property, call [IFillPatternFeatureData::PatternDirectionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternDirectionType.md) to get the type of pattern direction reference returned by this property. If this property is not specified, SOLIDWORKS chooses an appropriate reference for the specified [IFillPatternFeatureData::PatternLayoutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

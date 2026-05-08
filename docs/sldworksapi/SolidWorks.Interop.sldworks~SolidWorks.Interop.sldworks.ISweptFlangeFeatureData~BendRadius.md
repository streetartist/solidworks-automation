# BendRadius Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~BendRadius`

Gets or sets the bend radius of this swept flange feature.
Gets or sets the bend radius of this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendRadius As System.Double
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Double
 
instance.BendRadius = value
 
value = instance.BendRadius
```

```

System.double BendRadius {get; set;}
```

```

property System.double BendRadius {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Bend radius

Remarks

The setter of this property is valid only if [ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~OverrideDefaultSheetMetalParameters.md) is true.

This property gets a:

  - Default bend radius if:

> - [ISweptFlangeFeatureData::UseDefaultRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultRadius.md) is true,
>
>     - and -
>
> - ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is false.

  - Custom bend radius if:

> - ISweptFlangeFeatureData::UseDefaultRadius is false,
>
>     - and -
>
> - ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

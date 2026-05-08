# BendRadius Property (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~BendRadius`

Gets or sets the bend radius of this bend flange feature.
Gets or sets the bend radius of this bend flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendRadius As System.Double
```

```

Dim instance As IBaseFlangeFeatureData
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

Value of the bend radius

Remarks

The setter of this property is valid only if [IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideDefaultSheetMetalParameters.md) is true and [IBaseFlangeFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.md) is false.

This property gets a:

  - Default bend radius if:

> - IBaseFlangeFeatureData::UseMaterialSheetMetalParameters is true,
>
>     - and -
>
> - IBaseFlangeFeatureData:: OverrideDefaultSheetMetalParameters is false.

  - Custom bend radius if:

> - IBaseFlangeFeatureData::UseDefaultRadius is false,
>
>     - and -
>
> - IBaseFlangeFeatureData:: OverrideDefaultSheetMetalParameters is true.

Example

See [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)

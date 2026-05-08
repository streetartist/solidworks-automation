# OverrideDefaultSheetMetalParameters Property (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideDefaultSheetMetalParameters`

Gets or sets whether to override the default sheet metal parameters for this sheet metal base flange feature.
Gets or sets whether to override the default sheet metal parameters for this sheet metal base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideDefaultSheetMetalParameters As System.Boolean
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean
 
instance.OverrideDefaultSheetMetalParameters = value
 
value = instance.OverrideDefaultSheetMetalParameters
```

```

System.bool OverrideDefaultSheetMetalParameters {get; set;}
```

```

property System.bool OverrideDefaultSheetMetalParameters {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the default values, false to not

Remarks

This property is valid only when creating the base flange in a non-sheet-metal part.

If this property is:

- True, then [IBaseFlangeFeatureData::Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Thickness.md) and [IBaseFlangeFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~BendRadius.md) get and set user-defined values.
- False, then IBaseFlangeFeatureData::Thickness and IBaseFlangeFeatureData::BendRadius are invalid setters; those properties only get default values.

Example

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)

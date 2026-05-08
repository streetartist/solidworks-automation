# OverrideDefaultSheetMetalParameters Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~OverrideDefaultSheetMetalParameters`

Gets or sets whether to override the default sheet metal parameters for this swept flange feature.
Gets or sets whether to override the default sheet metal parameters for this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideDefaultSheetMetalParameters As System.Boolean
```

```

Dim instance As ISweptFlangeFeatureData
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

This property is valid only when creating the swept flange in a non-sheet-metal part.

If this property is:

- True, then [ISweptFlangeFeatureData::Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Thickness.md) and [ISweptFlangeFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~BendRadius.md) get and set user-defined values.
- False, then ISweptFlangeFeatureData::Thickness and ISweptFlangeFeatureData::BendRadius are invalid as setters and get only default values.

Example

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

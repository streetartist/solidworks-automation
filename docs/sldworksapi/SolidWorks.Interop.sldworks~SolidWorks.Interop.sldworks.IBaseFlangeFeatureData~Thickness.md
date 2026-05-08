# Thickness Property (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Thickness`

Gets or sets the thickness for this base flange feature.
Gets or sets the thickness for this base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Thickness As System.Double
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Double
 
instance.Thickness = value
 
value = instance.Thickness
```

```

System.double Thickness {get; set;}
```

```

property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value for thickness

Remarks

This property is valid only when not creating the base flange on an existing sheet metal feature.

The setter of this property is valid only if [IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideDefaultSheetMetalParameters.md) is true and [IBaseFlangeFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.md) is false.

This property gets:

- Default thickness if IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters is false.

- Custom thickness if IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters is true.

Example

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::ReverseThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReverseThickness.md)

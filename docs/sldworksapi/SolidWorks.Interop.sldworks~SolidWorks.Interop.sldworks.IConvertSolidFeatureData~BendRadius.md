# BendRadius Property (IConvertSolidFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~BendRadius`

Gets or sets the default radius for bends in this convert solid feature.
Gets or sets the default radius for bends in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendRadius As System.Double
```

```

Dim instance As IConvertSolidFeatureData
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

The setter of this property is valid only if [IConvertSolidFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultSheetMetalParameters.md) is true.

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)

# UseMaterialSheetMetalParameters Property (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters`

Gets whether the properties of the material applied are used when creating this base flange.
Gets whether the properties of the material applied are used when creating this base flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property UseMaterialSheetMetalParameters As System.Boolean
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean
 
value = instance.UseMaterialSheetMetalParameters
```

```

System.bool UseMaterialSheetMetalParameters {get;}
```

```

property System.bool UseMaterialSheetMetalParameters {
   System.bool get();
}
```

#### Property Value

True uses the applied material's sheet metal parameters, false does not

Remarks

This property is valid only:

- when not creating the base flange on an existing sheet metal feature,

    - and -

- when [IBaseFlangeFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.md) is false.

If this property returns false, then specify sheet metal parameters using:

- [IBaseFlangeFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~BendRadius.md)
- [IBaseFlangeFeatureData::Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Thickness.md)
- [IBaseFlangeFeatureData::ReverseThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReverseThickness.md)

Whether to use the applied material's sheet metal parameters was set during the [initialization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.md) of this base flange and cannot be changed.

Example

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)

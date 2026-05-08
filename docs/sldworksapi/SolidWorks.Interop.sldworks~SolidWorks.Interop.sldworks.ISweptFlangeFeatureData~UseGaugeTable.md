# UseGaugeTable Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable`

Gets or sets whether to use an Excel gauge table for this swept flange feature.
Gets or sets whether to use an Excel gauge table for this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseGaugeTable As System.Boolean
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean
 
instance.UseGaugeTable = value
 
value = instance.UseGaugeTable
```

```

System.bool UseGaugeTable {get; set;}
```

```

property System.bool UseGaugeTable {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use an Excel gauge table, false to not

Remarks

This property is valid only:

- if [ISweptFlangeFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseMaterialSheetMetalParameters.md) is false,

    - and -

- when not creating the swept flange on an existing sheet metal feature.

If this property is true, then use [ISweptFlangeFeatureData::GetGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetGaugeTableParameters.md) and [ISweptFlangeFeatureData::SetGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetGaugeTableParameters.md) to get and set the gauge table.

Example

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

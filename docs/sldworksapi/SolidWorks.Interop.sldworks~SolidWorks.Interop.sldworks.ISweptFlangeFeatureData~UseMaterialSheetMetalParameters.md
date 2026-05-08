# UseMaterialSheetMetalParameters Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseMaterialSheetMetalParameters`

Gets or sets whether to use the material sheet metal parameters in this swept flange feature.
Gets or sets whether to use the material sheet metal parameters in this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseMaterialSheetMetalParameters As System.Boolean
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean
 
instance.UseMaterialSheetMetalParameters = value
 
value = instance.UseMaterialSheetMetalParameters
```

```

System.bool UseMaterialSheetMetalParameters {get; set;}
```

```

property System.bool UseMaterialSheetMetalParameters {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the material sheet metal parameters, false to not

Remarks

This property is valid only:

- when not creating the swept flange on an existing sheet metal feature,

    - and -

- when [ISweptFlangeFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.md) is false.

Example

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

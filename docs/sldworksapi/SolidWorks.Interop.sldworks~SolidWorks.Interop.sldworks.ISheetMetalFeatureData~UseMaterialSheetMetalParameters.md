# UseMaterialSheetMetalParameters Property (ISheetMetalFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseMaterialSheetMetalParameters`

Gets or sets whether to use the properties of the material applied when creating this sheet metal feature.
Gets or sets whether to use the properties of the material applied when creating this sheet metal feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseMaterialSheetMetalParameters As System.Boolean
```

```

Dim instance As ISheetMetalFeatureData
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

This property is valid only when [ISheetMetalFeatureData::GetUseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.md) returns false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)  
[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.md)

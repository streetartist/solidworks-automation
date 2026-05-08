# OverrideSheetThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideSheetThickness`

Gets or sets whether to override the gauge thickness for this convert solid feature.
Gets or sets whether to override the gauge thickness for this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideSheetThickness As System.Boolean
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean
 
instance.OverrideSheetThickness = value
 
value = instance.OverrideSheetThickness
```

```

System.bool OverrideSheetThickness {get; set;}
```

```

property System.bool OverrideSheetThickness {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the gauge thickness, false to not

Remarks

This property is related to the gauge table only. This property is valid only before calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) to create a new sheet metal feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)

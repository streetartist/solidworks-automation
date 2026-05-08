# OverrideRadius Property (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius`

Gets or sets whether to override the bend radius value specified in the gauge table for this base flange feature.
Gets or sets whether to override the bend radius value specified in the gauge table for this base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideRadius As System.Boolean
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean
 
instance.OverrideRadius = value
 
value = instance.OverrideRadius
```

```

System.bool OverrideRadius {get; set;}
```

```

property System.bool OverrideRadius {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the bend radius value, false to not

Example

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::GetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.md)  
[IBaseFlangeFeatureData::GetTableRadiiCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.md)  
[IBaseFlangeFeatureData::IGetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.md)  
[IBaseFlangeFeatureData::TableRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableRadius.md)

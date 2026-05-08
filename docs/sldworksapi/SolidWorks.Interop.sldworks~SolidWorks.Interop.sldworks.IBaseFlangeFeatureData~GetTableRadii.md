# GetTableRadii Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii`

Gets the bend radii from the gauge table for this base flange feature.
Gets the bend radii from the gauge table for this base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableRadii( _
   ByVal ThicknessTableName As System.String _
) As System.Object
```

```

Dim instance As IBaseFlangeFeatureData
Dim ThicknessTableName As System.String
Dim value As System.Object
 
value = instance.GetTableRadii(ThicknessTableName)
```

```

System.object GetTableRadii( 
   System.string ThicknessTableName
)
```

```

System.Object^ GetTableRadii( 
   System.String^ ThicknessTableName
) 
```

#### Parameters

*ThicknessTableName*
:   Gauge table thickness names (see **Remarks**)

#### Return Value

Array of bend radii

Remarks

Before calling this method call, [IBaseFlangeFeatureData::GetTableThicknesses](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknesses.md) to get the names of the thicknesses in the gauge table.

Example

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::IGetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.md)  
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.md)  
[IBaseFlangeFeatureData::GetTableRadiiCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.md)  
[IBaseFlangeFeatureData::OverrideRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius.md)  
[IBaseFlangeFeatureData::TableRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableRadius.md)  
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.md)

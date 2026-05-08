# IGetTableRadii Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii`

Gets the bend radii from the gauge table for this base flange feature.
Gets the bend radii from the gauge table for this base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableRadii( _
   ByVal ThicknessTableName As System.String, _
   ByVal NCount As System.Integer _
) As System.Double
```

```

Dim instance As IBaseFlangeFeatureData
Dim ThicknessTableName As System.String
Dim NCount As System.Integer
Dim value As System.Double
 
value = instance.IGetTableRadii(ThicknessTableName, NCount)
```

```

System.double IGetTableRadii( 
   System.string ThicknessTableName,
   System.int NCount
)
```

```

System.double IGetTableRadii( 
   System.String^ ThicknessTableName,
   System.int NCount
) 
```

#### Parameters

*ThicknessTableName*
:   Gauge table thickness names (see **Remarks**)

*NCount*
:   Number of bend radii (see **Remarks**)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of bend radii

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method call:

- [IBaseFlangeFeatureData::IGetTableThicknesses](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableThicknesses.md) to get the names of the thicknesses in the gauge table.
- [IBaseFlangeFeatureData::GetTableRadiiCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.md) to get the value for NCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::GetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.md)  
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.md)  
[IBaseFlangeFeatureData::OverrideThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideThickness.md)  
[IBaseFlangeFeatureData::ThicknessTableName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ThicknessTableName.md)  
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.md)

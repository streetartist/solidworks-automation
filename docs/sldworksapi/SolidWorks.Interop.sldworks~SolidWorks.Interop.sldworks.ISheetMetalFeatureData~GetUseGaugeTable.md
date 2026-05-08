# GetUseGaugeTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetUseGaugeTable`

Gets whether to use a sheet metal feature gauge table.
Gets whether to use a sheet metal feature gauge table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseGaugeTable( _
   ByRef UseGaugeTable As System.Boolean, _
   ByRef GaugeTableFile As System.String _
) As System.Integer
```

```

Dim instance As ISheetMetalFeatureData
Dim UseGaugeTable As System.Boolean
Dim GaugeTableFile As System.String
Dim value As System.Integer
 
value = instance.GetUseGaugeTable(UseGaugeTable, GaugeTableFile)
```

```

System.int GetUseGaugeTable( 
   out System.bool UseGaugeTable,
   out System.string GaugeTableFile
)
```

```

System.int GetUseGaugeTable( 
   [Out] System.bool UseGaugeTable,
   [Out] System.String^ GaugeTableFile
) 
```

#### Parameters

*UseGaugeTable*
:   True to use a gauge table, false to not

*GaugeTableFile*
:   Gauge table file name; valid only if UseGaugeTable is true

#### Return Value

Result code as defined in [swSheetMetalModifierError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

Example

See [ISheetMetalFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)  
[ISheetMetalFeatureData::SetUseGaugeTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetUseGaugeTable.md)

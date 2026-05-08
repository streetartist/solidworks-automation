# SetInstanceDimensionValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceDimensionValue`

Sets a new value for the pattern dimension of the specified pattern instance in this variable pattern feature.
Sets a new value for the pattern dimension of the specified pattern instance in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetInstanceDimensionValue( _
   ByVal TableRowIndex As System.Integer, _
   ByVal ControlDimName As System.String, _
   ByVal NewValue As System.Double _
) As System.String
```

```

Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim ControlDimName As System.String
Dim NewValue As System.Double
Dim value As System.String
 
value = instance.SetInstanceDimensionValue(TableRowIndex, ControlDimName, NewValue)
```

```

System.string SetInstanceDimensionValue( 
   System.int TableRowIndex,
   System.string ControlDimName,
   System.double NewValue
)
```

```

System.String^ SetInstanceDimensionValue( 
   System.int TableRowIndex,
   System.String^ ControlDimName,
   System.double NewValue
) 
```

#### Parameters

*TableRowIndex*
:   Index of the pattern instance in the pattern table (see **Remarks**)

*ControlDimName*
:   Name of the controlling dimension of the pattern instance (see **Remarks**)

*NewValue*
:   New value for the pattern dimension

#### Return Value

| If a new value for the pattern dimension is... | Then Return Value is an... |
| --- | --- |
| Set | Empty string indicating success |
| Not set | Error string |

Remarks

Use:

- [IDimPatternFeatureData::GetTableRowIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex.md) to get TableRowIndex.
- [IDimPatternFeatureData::GetControllingDimensionName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetControllingDimensionName.md) to get ControlDimName.

Example

[Delete and Insert Instances in Variable Pattern Feature (C#)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_CSharp.htm)  
[Delete and Insert Instances in Variable Pattern Feature (VB.NET)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VBNET.htm)  
[Delete and Insert Instances in Variable Pattern Feature (VBA)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::GetInstanceDimensionName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceDimensionName.md)

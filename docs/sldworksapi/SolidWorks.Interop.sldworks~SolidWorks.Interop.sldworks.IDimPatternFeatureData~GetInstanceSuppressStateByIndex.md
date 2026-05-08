# GetInstanceSuppressStateByIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex`

Gets whether the pattern instance at the specified index in the pattern table is suppressed in this variable pattern feature.
Gets whether the pattern instance at the specified index in the pattern table is suppressed in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInstanceSuppressStateByIndex( _
   ByVal TableRowIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim value As System.Boolean
 
value = instance.GetInstanceSuppressStateByIndex(TableRowIndex)
```

```

System.bool GetInstanceSuppressStateByIndex( 
   System.int TableRowIndex
)
```

```

System.bool GetInstanceSuppressStateByIndex( 
   System.int TableRowIndex
) 
```

#### Parameters

*TableRowIndex*
:   Index of the pattern instance in the pattern table (see **Remarks**)

#### Return Value

True if the pattern instance is suppressed, false if not

Remarks

Use [IDimPatternFeatureData::GetTableRowIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex.md) to get TableRowIndex.

Example

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)  
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)  
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::SetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex.md)  
[IDimPatternFeatureData::GetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName.md)  
[IDimPatternFeatureData::SetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName.md)

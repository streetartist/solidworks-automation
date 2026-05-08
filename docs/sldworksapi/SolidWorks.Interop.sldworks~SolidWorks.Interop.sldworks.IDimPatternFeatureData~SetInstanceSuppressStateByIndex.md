# SetInstanceSuppressStateByIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex`

Sets whether the pattern instance with the specified index in the pattern table is suppressed in this variable pattern feature.
Sets whether the pattern instance with the specified index in the pattern table is suppressed in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetInstanceSuppressStateByIndex( _
   ByVal TableRowIndex As System.Integer, _
   ByVal SuppressState As System.Boolean _
) As System.String
```

```

Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim SuppressState As System.Boolean
Dim value As System.String
 
value = instance.SetInstanceSuppressStateByIndex(TableRowIndex, SuppressState)
```

```

System.string SetInstanceSuppressStateByIndex( 
   System.int TableRowIndex,
   System.bool SuppressState
)
```

```

System.String^ SetInstanceSuppressStateByIndex( 
   System.int TableRowIndex,
   System.bool SuppressState
) 
```

#### Parameters

*TableRowIndex*
:   Index of the pattern instance in the pattern table to suppress (see **Remarks**)

*SuppressState*
:   True to suppress the pattern instance, false to not

#### Return Value

| If the pattern instance is... | Then Return Value is an... |
| --- | --- |
| Suppressed | Empty string indicating success |
| Not suppressed | Error string |

Remarks

Use [IDimPatternFeatureData::GetTableRowIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex.md) to get TableRowIndex.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::GetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex.md)  
[IDimPatternFeatureData::GetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName.md)  
[IDimPatternFeatureData::SetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName.md)

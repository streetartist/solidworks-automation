# GetInstanceNameByIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex`

Gets the name of the pattern instance at the specified index in the pattern table in this variable pattern feature.
Gets the name of the pattern instance at the specified index in the pattern table in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInstanceNameByIndex( _
   ByVal TableRowIndex As System.Integer _
) As System.String
```

```

Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim value As System.String
 
value = instance.GetInstanceNameByIndex(TableRowIndex)
```

```

System.string GetInstanceNameByIndex( 
   System.int TableRowIndex
)
```

```

System.String^ GetInstanceNameByIndex( 
   System.int TableRowIndex
) 
```

#### Parameters

*TableRowIndex*
:   1-based index of the pattern instance in the pattern table (see **Remarks**)

#### Return Value

Name of the pattern instance

Remarks

Use [IDimPatternFeatureData::GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.md) to get TableRowIndex.

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

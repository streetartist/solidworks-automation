# GetTableRowIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex`

Gets the index of the specified pattern instance in the pattern table in this variable pattern feature.
Gets the index of the specified pattern instance in the pattern table in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableRowIndex( _
   ByVal InstanceName As System.String _
) As System.Integer
```

```

Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim value As System.Integer
 
value = instance.GetTableRowIndex(InstanceName)
```

```

System.int GetTableRowIndex( 
   System.string InstanceName
)
```

```

System.int GetTableRowIndex( 
   System.String^ InstanceName
) 
```

#### Parameters

*InstanceName*
:   Name of the pattern instance (see **Remarks**)

#### Return Value

Index in the pattern table for InstanceName (see **Remarks**)

Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.md) to get InstanceName.

**NOTE**: The index returned by this method is a value in a row in the **Instance** column in the pattern table.

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
[IDimPatternFeatureData::GetInstanceIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceIndex.md)

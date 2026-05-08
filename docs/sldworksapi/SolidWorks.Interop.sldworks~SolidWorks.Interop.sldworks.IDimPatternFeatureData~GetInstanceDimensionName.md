# GetInstanceDimensionName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceDimensionName`

Gets the name of the pattern dimension for the pattern instance in this variable pattern feature.
Gets the name of the pattern dimension for the pattern instance in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInstanceDimensionName( _
   ByVal InstanceName As System.String, _
   ByVal ControllingDimName As System.String _
) As System.String
```

```

Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim ControllingDimName As System.String
Dim value As System.String
 
value = instance.GetInstanceDimensionName(InstanceName, ControllingDimName)
```

```

System.string GetInstanceDimensionName( 
   System.string InstanceName,
   System.string ControllingDimName
)
```

```

System.String^ GetInstanceDimensionName( 
   System.String^ InstanceName,
   System.String^ ControllingDimName
) 
```

#### Parameters

*InstanceName*
:   Name of the pattern instance (see **Remarks**)

*ControllingDimName*
:   Controlling dimension of the pattern instance (see **Remarks**)

#### Return Value

Name of the pattern dimension

Remarks

| Use.. | To get... |
| --- | --- |
| [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.md) | InstanceName |
| [IDimPatternFeatureData::GetControllingDimensionName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetControllingDimensionName.md) | ControllingDimName |

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
[IDimPatternFeatureData::SetInstanceDimensionValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceDimensionValue.md)

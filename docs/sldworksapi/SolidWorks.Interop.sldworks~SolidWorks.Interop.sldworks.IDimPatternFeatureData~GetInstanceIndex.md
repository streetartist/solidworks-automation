# GetInstanceIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceIndex`

Gets the index of the pattern instance in the FeatureManager design tree in the variable pattern feature.
Gets the index of the pattern instance in the FeatureManager design tree in the variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInstanceIndex( _
   ByVal InstanceName As System.String _
) As System.Integer
```

```

Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim value As System.Integer
 
value = instance.GetInstanceIndex(InstanceName)
```

```

System.int GetInstanceIndex( 
   System.string InstanceName
)
```

```

System.int GetInstanceIndex( 
   System.String^ InstanceName
) 
```

#### Parameters

*InstanceName*
:   Name of the pattern instance (see **Remarks**)

#### Return Value

Index of InstanceName in the FeatureManager design tree

Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.md) to get InstanceName.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::GetInstanceCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.md)

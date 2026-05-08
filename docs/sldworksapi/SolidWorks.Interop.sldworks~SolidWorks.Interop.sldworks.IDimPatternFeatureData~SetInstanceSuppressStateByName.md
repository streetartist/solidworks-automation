# SetInstanceSuppressStateByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName`

Sets whether a pattern instance with the specified name is suppressed in this variable pattern feature.
Sets whether a pattern instance with the specified name is suppressed in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetInstanceSuppressStateByName( _
   ByVal InstanceName As System.String, _
   ByVal SuppressState As System.Boolean _
) As System.String
```

```

Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim SuppressState As System.Boolean
Dim value As System.String
 
value = instance.SetInstanceSuppressStateByName(InstanceName, SuppressState)
```

```

System.string SetInstanceSuppressStateByName( 
   System.string InstanceName,
   System.bool SuppressState
)
```

```

System.String^ SetInstanceSuppressStateByName( 
   System.String^ InstanceName,
   System.bool SuppressState
) 
```

#### Parameters

*InstanceName*
:   Name of pattern instance to suppress (see **Remarks**)

*SuppressState*
:   True if the pattern instance is suppressed, false if not

#### Return Value

| If the pattern instance is... | Then Return Value is an... |
| --- | --- |
| Suppressed | Empty string indicating success |
| Not suppressed | Error string |

Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.md) to get InstanceName.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::GetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName.md)  
[IDimPatternFeatureData::GetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex.md)  
[IDimPatternFeatureData::SetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex.md)

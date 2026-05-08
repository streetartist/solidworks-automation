# GetInstanceSuppressStateByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName`

Gets whether the pattern instance with the specified name is suppressed in this variable pattern feature.
Gets whether the pattern instance with the specified name is suppressed in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInstanceSuppressStateByName( _
   ByVal InstanceName As System.String _
) As System.Boolean
```

```

Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim value As System.Boolean
 
value = instance.GetInstanceSuppressStateByName(InstanceName)
```

```

System.bool GetInstanceSuppressStateByName( 
   System.string InstanceName
)
```

```

System.bool GetInstanceSuppressStateByName( 
   System.String^ InstanceName
) 
```

#### Parameters

*InstanceName*
:   Name of the pattern instance (see **Remarks**)

#### Return Value

True if the pattern instance is suppressed, false if not

Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.md) to get InstanceName.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::SetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName.md)  
[IDimPatternFeatureData::GetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex.md)  
[IDimPatternFeatureData::SetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex.md)

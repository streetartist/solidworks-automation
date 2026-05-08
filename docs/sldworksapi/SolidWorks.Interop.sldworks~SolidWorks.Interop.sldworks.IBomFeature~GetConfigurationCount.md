# GetConfigurationCount Method (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurationCount`

Gets the number of configurations available to this BOM table or used in this BOM table.
Gets the number of configurations available to this BOM table or used in this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConfigurationCount( _
   ByVal OnlyVisible As System.Boolean _
) As System.Integer
```

```

Dim instance As IBomFeature
Dim OnlyVisible As System.Boolean
Dim value As System.Integer
 
value = instance.GetConfigurationCount(OnlyVisible)
```

```

System.int GetConfigurationCount( 
   System.bool OnlyVisible
)
```

```

System.int GetConfigurationCount( 
   System.bool OnlyVisible
) 
```

#### Parameters

*OnlyVisible*
:   True to get the number of configurations currently displayed in this table, false to get the total number of configurations available in this table

#### Return Value

Number of configurations in this BOM table or available to this BOM table

Remarks

The view associated with this BOM can contain a model with multiple configurations.

For a top-level only style BOM table, there can be several Quantity columns, each showing the results for a different configuration.  For the other styles of BOM tables, only a particular configuration can be shown in the table, and that configuration can be changed. To determine the style of the BOM table, use [IBomFeature::TableType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType.md).

|  |  |
| --- | --- |
| **If OnlyVisible is...** | **Then the value returned is...** |
| True | Number of configurations currently shown in the BOM table.  For a top-level only style BOM table, this could be any number from 0 to the total number of configurations available. For the other styles of BOM tables, this value is always 1. |
| false | Total number of configurations available. |

To get the configuration names, call [IBomFeature::GetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.md) or [IBomFeature::IGetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.md).

Call this method before calling IBomFeature::IGetConfigurations to get the number of configurations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)

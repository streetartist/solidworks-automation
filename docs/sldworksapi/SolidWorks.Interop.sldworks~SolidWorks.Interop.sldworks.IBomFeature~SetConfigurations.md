# SetConfigurations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations`

Sets the configurations used in this BOM table.
Sets the configurations used in this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetConfigurations( _
   ByVal OnlyVisible As System.Boolean, _
   ByVal Visible As System.Object, _
   ByVal Names As System.Object _
) As System.Boolean
```

```

Dim instance As IBomFeature
Dim OnlyVisible As System.Boolean
Dim Visible As System.Object
Dim Names As System.Object
Dim value As System.Boolean
 
value = instance.SetConfigurations(OnlyVisible, Visible, Names)
```

```

System.bool SetConfigurations( 
   System.bool OnlyVisible,
   System.object Visible,
   System.object Names
)
```

```

System.bool SetConfigurations( 
   System.bool OnlyVisible,
   System.Object^ Visible,
   System.Object^ Names
) 
```

#### Parameters

*OnlyVisible*
:   Indicator of the contents of the arrays (see **Remarks**)

*Visible*
:   Array of Booleans indicating the visibility of the configurations

*Names*
:   Array of strings of the names of the configurations

#### Return Value

True if configurations are set, false if not

Remarks

Although this method works on all styles of BOM tables (top-level only, parts-only, indented subassemblies), it is only necessary for top-level only style tables. For the other style tables, where only a single configuration is shown at a time, using [IBomFeature::Configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Configuration.md) is simpler and more efficient.

**NOTE:** If the **Restrict top-level only BOMs to one configuration** option on the **Document Properties > Tables > Bill of Materials** dialog or [IModelDocExtension::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html).swOneConfigOnlyTopLevelBom) returns true, then only the active or default configuration of the drawing view is inserted in the BOM.

The view associated with this BOM can contain a model with multiple configurations. For a top-level only style BOM table, there can be several Quantity columns, each showing the results for a different configuration. For the other styles of BOM tables, only a particular configuration can be shown in the table, and that configuration can be changed. To determine the BOM table style, use the [IBomFeature::TableType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType.md) property.

|  |  |  |
| --- | --- | --- |
| ****If OnlyVisible is...**** | **Then Names contains the names of...** | **And Visible...** |
| True | Only the configurations currently shown in the BOM table.    For a top-level only style BOM table, this could be any number of configurations. For the other styles of BOM tables, it is one configuration name. | Can be passed in as null or nothing.  If it is passed in as non-null or non-nothing, then the array contains true for all items. |
| False | All configurations available. | Contains Booleans that correspond to each item in Names indicating if that particular configuration is shown in the BOM table or not. |

To get the number of configurations, use [IBomFeature::GetConfigurationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurationCount.md).

Example

[Insert BOM Table (C#)](Insert_BOM_Table_Example_CSharp.htm)  
[Insert BOM Table (VB.NET)](Insert_BOM_Table_Example_VBNET.htm)  
[Insert BOM Table (VBA)](Insert_BOM_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::GetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.md)  
[IBomFeature::ISetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.md)

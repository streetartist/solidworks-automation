# Configuration Property (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Configuration`

Gets or sets the name of configuration for this BOM table.
Gets or sets the name of configuration for this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Configuration As System.String
```

```

Dim instance As IBomFeature
Dim value As System.String
 
instance.Configuration = value
 
value = instance.Configuration
```

```

System.string Configuration {get; set;}
```

```

property System.String^ Configuration {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the configuration shown in the BOM table

Remarks

You can only use this property for BOM tables that show one configuration at a time, such as for parts and indented subassembly style BOM tables.

You cannot use this property for top-level only BOM tables because information on multiple configurations can be shown at once in that style table. In that scenario, getting this property returns an empty string and setting the property has no effect. Use the [IBomFeature::GetConfigurationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurationCount.md), [IBomFeature::GetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.md), [IBomFeature::IGetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.md), [IBomFeature::SetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.md), or [IBomFeature::ISetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.md) for that type of table.

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Example

[Insert BOM Table and BOM Balloon (VB.NET)](Insert_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)  
[Insert BOM Table and BOM Balloon (VBA)](Insert_BOM_Table_and_BOM_Balloon_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)

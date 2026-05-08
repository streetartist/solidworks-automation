# AddRebuildSaveMark Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark`

Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data saved every time you save the model document.
Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data saved every time you save the model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddRebuildSaveMark As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.AddRebuildSaveMark = value
 
value = instance.AddRebuildSaveMark
```

```

System.bool AddRebuildSaveMark {get; set;}
```

```

property System.bool AddRebuildSaveMark {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to mark the configuration as needing to be rebuilt and its configuration data saved every time you save the model document, false to mark the configuration as not needing to be rebuilt and its configuration data not saved every time you save the model document

Example

[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)  
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)  
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.md)  
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md)  
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md)  
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.md)  
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.md)  
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.md)  
[IConfigurationManager::RemoveMarkForAllConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations.md)

# AddRebuildSaveMark Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark`

Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved.
Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddRebuildSaveMark( _
   ByVal WhichConfigurations As System.Integer, _
   ByVal ConfigNames As System.Object _
) As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim WhichConfigurations As System.Integer
Dim ConfigNames As System.Object
Dim value As System.Boolean
 
value = instance.AddRebuildSaveMark(WhichConfigurations, ConfigNames)
```

```

System.bool AddRebuildSaveMark( 
   System.int WhichConfigurations,
   System.object ConfigNames
)
```

```

System.bool AddRebuildSaveMark( 
   System.int WhichConfigurations,
   System.Object^ ConfigNames
) 
```

#### Parameters

*WhichConfigurations*
:   One of the following options in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html):

    - swAllConfiguration
    - swSpecifyConfiguration
    - swThisConfiguration
    - swSpeedpakConfiguration

*ConfigNames*
:   Array of configuration names to which to apply the mark; valid only if WhichConfigurations is set to swInConfigurationOpts\_e.swSpecifyConfiguration

#### Return Value

True if configurations marked successfully, false if not

Example

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfiguration::NeedsRebuild Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.md)  
[IModelDoc2::EditRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md)  
[IModelDocExtension::EditRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.md)  
[IModelDocExtension::ForceRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.md)  
[IConfiguration::AddRebuildSaveMark Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.md)  
[IConfigurationManager::RemoveMarkForAllConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations.md)

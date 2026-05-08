# AddConfiguration2 Method (IConfigurationManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration2`

Creates a new configuration.
Creates a new configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddConfiguration2( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer, _
   ByVal ParentConfigName As System.String, _
   ByVal Description As System.String, _
   ByVal Rebuild As System.Boolean _
) As Configuration
```

```

Dim instance As IConfigurationManager
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim ParentConfigName As System.String
Dim Description As System.String
Dim Rebuild As System.Boolean
Dim value As Configuration
 
value = instance.AddConfiguration2(Name, Comment, AlternateName, Options, ParentConfigName, Description, Rebuild)
```

```

Configuration AddConfiguration2( 
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options,
   System.string ParentConfigName,
   System.string Description,
   System.bool Rebuild
)
```

```

Configuration^ AddConfiguration2( 
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options,
   System.String^ ParentConfigName,
   System.String^ Description,
   System.bool Rebuild
) 
```

#### Parameters

*Name*
:   Name of the configuration

*Comment*
:   Comment displayed in Configuration Properties

*AlternateName*
:   Alternate configuration name (i.e., user-specified name); used if Options is set to swConfigurationOptions2\_e\_UseAlternateName

*Options*
:   Combination of one or more configuration options as defined in [swConfigurationOptions2\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see **Remarks**)

*ParentConfigName*
:   Name of parent configuration

*Description*
:   Text that identifies the configuration

*Rebuild*
:   True to rebuild the model after adding this configuration, false to not

#### Return Value

Newly created [configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)

Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption\_SuppressByDefault
- swConfigOption\_HideByDefault
- swConfigOption\_MinFeatureManager
- swConfigOption\_UseAlternateName

Example

[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IAssemblyDoc::AddComponentConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration.md)  
[IModelDoc2::AddConfiguration3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md)  
[IConfiguration::GetChildren Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.md)  
[IConfiguration::GetParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.md)  
[IConfiguration::Name Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.md)  
[IConfigurationManager::ActiveConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)

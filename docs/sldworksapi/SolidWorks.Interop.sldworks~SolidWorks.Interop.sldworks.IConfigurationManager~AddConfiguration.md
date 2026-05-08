# AddConfiguration Method (IConfigurationManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration`

Obsolete. Superseded by IConfigurationManager::AddConfiguration2.
Obsolete. Superseded by [IConfigurationManager::AddConfiguration2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddConfiguration( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer, _
   ByVal ParentConfigName As System.String, _
   ByVal Description As System.String _
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
Dim value As Configuration
 
value = instance.AddConfiguration(Name, Comment, AlternateName, Options, ParentConfigName, Description)
```

```

Configuration AddConfiguration( 
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options,
   System.string ParentConfigName,
   System.string Description
)
```

```

Configuration^ AddConfiguration( 
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options,
   System.String^ ParentConfigName,
   System.String^ Description
) 
```

#### Parameters

*Name*
:   Name of the configuration

*Comment*
:   Comment displayed in Configuration Properties

*AlternateName*
:   Alternate configuration name (i.e., user-specified name); used if swConfigOption\_UseAlternateName is set to true

*Options*
:   Combination of one or more Boolean configuration options as defined in [swConfigurationOptions2\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see **Remarks**)

*ParentConfigName*
:   Name of parent configuration

*Description*
:   Text that identifies the configuration

#### Return Value

Newly created [configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)

Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption\_SuppressByDefault - True if you want to suppress newly added features and mates in this configuration, false if not
- swConfigOption\_HideByDefault - True if you want newly added components to be hidden, false if not
- swConfigOption\_MinFeatureManager - True if you want newly added components to only display their component name in the FeatureManager design tree, false if you want newly added components to display their name and each of their features in the FeatureManager design tree

Example

[Set Dimensions to Mid-Tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)  
[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IAssembly::AddComponentConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration.md)  
[IComponent2::Name2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.md)  
[IConfiguration::AlternateName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.md)  
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.md)  
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.md)  
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.md)  
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.md)  
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)  
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md)

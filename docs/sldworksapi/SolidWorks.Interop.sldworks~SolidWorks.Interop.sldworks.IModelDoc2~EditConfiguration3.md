# EditConfiguration3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditConfiguration3`

Edits the specified configuration.
Edits the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditConfiguration3( _
   ByVal Name As System.String, _
   ByVal NewName As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Name As System.String
Dim NewName As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim value As System.Boolean
 
value = instance.EditConfiguration3(Name, NewName, Comment, AlternateName, Options)
```

```

System.bool EditConfiguration3( 
   System.string Name,
   System.string NewName,
   System.string Comment,
   System.string AlternateName,
   System.int Options
)
```

```

System.bool EditConfiguration3( 
   System.String^ Name,
   System.String^ NewName,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options
) 
```

#### Parameters

*Name*
:   Current configuration name

*NewName*
:   New configuration name

*Comment*
:   Comment used in configuration properties

*AlternateName*
:   Alternate configuration name; used if swConfigOption\_UseAlternateName is set to True

*Options*
:   Combination of one or more BOOLEAN configuration options as defined in  [swConfigurationOptions2\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see **Remarks**)

#### Return Value

True if configuration name was changed, false if not

Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption\_SuppressByDefault True if you want to suppress newly added features and mates in this configuration, false if not
- swConfigOption\_HideByDefault - True if you want newly added components to be hidden, false if not
- swConfigOption\_MinFeatureManager True if you want newly added components to only display their component name in the FeatureManager design tree, false if you want newly added components to display their name and each of their features in the FeatureManager design tree

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md)  
[IModelDoc2::DeleteConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.md)  
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.md)  
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.md)  
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.md)  
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.md)  
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.md)  
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.md)  
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.md)  
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IModelDoc2::IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.md)

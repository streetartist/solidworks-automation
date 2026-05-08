# IGetConfigurationByName Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName`

Gets the specified configuration.
Gets the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConfigurationByName( _
   ByVal Name As System.String _
) As Configuration
```

```

Dim instance As IModelDoc2
Dim Name As System.String
Dim value As Configuration
 
value = instance.IGetConfigurationByName(Name)
```

```

Configuration IGetConfigurationByName( 
   System.string Name
)
```

```

Configuration^ IGetConfigurationByName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Specified configuration name

#### Return Value

[Configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md) or NULL if the operation fails

Remarks

If the specified configuration has not been activated, then some data may be unavailable. For example, attempting to traverse assembly components for a configuration that has not been activated results in a NULL root component being returned from [IConfiguration::IGetRootComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md). However, the IConfiguration object returned is useful for obtaining data that is stored with the IConfiguration object, such as the [IConfiguration::AlternateName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.md) value. The specified configuration does not have to be activated to obtain this type of stored information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md)  
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.md)  
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.md)  
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.md)  
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.md)  
[IModelDoc2::DeleteConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration.md)  
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.md)  
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.md)  
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.md)  
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)

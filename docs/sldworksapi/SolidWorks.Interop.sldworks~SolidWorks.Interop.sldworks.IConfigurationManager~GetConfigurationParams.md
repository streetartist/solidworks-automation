# GetConfigurationParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams`

Gets the parameters for this configuration.
Gets the parameters for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConfigurationParams( _
   ByVal ConfigName As System.String, _
   ByRef Params As System.Object, _
   ByRef Values As System.Object _
) As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim ConfigName As System.String
Dim Params As System.Object
Dim Values As System.Object
Dim value As System.Boolean
 
value = instance.GetConfigurationParams(ConfigName, Params, Values)
```

```

System.bool GetConfigurationParams( 
   System.string ConfigName,
   out System.object Params,
   out System.object Values
)
```

```

System.bool GetConfigurationParams( 
   System.String^ ConfigName,
   [Out] System.Object^ Params,
   [Out] System.Object^ Values
) 
```

#### Parameters

*ConfigName*
:   Name of the configuration

*Params*
:   Array of the names of the parameters for this configuration

*Values*
:   Array of values of the parameters for this configuration

#### Return Value

True if successful in getting the names and values of the parameters for this configuration, false if unsuccessful

Remarks

The output values may not be accurate if a design table was not added to the model.

Example

[Extract Configuration-specific Parameters (VBA)](Extract_Configuration-Specific_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.md)  
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.md)  
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.md)  
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.md)  
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)  
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.md)  
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.md)  
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.md)  
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.md)  
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.md)

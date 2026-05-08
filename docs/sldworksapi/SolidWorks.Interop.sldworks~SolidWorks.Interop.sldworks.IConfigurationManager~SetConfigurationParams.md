# SetConfigurationParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams`

Sets the parameters for this configuration.
Sets the parameters for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetConfigurationParams( _
   ByVal ConfigName As System.String, _
   ByRef ParamNames As System.Object, _
   ByRef ParamValues As System.Object _
) As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim ConfigName As System.String
Dim ParamNames As System.Object
Dim ParamValues As System.Object
Dim value As System.Boolean
 
value = instance.SetConfigurationParams(ConfigName, ParamNames, ParamValues)
```

```

System.bool SetConfigurationParams( 
   System.string ConfigName,
   ref System.object ParamNames,
   ref System.object ParamValues
)
```

```

System.bool SetConfigurationParams( 
   System.String^ ConfigName,
   System.Object^% ParamNames,
   System.Object^% ParamValues
) 
```

#### Parameters

*ConfigName*
:   Name of the configuration (see **Remarks**)

*ParamNames*
:   Array of the names of the parameters for ConfigName (see **Remarks**)

*ParamValues*
:   Array of values for the parameters for ConfigName (see **Remarks**)

#### Return Value

True if the names and values of parameters for the specified configuration are set, false if not

Remarks

In ConfigName, if you specify the name of a configuration that:

- does not exist, this method creates a new configuration with ParamNames and ParamValues.
- exists, this method sets that configuration with ParamNames and ParamValues.

You can control these parameters in a part document:

- Dimension values. Specify the dimension name in ParamNames for example, D1@Sketch1) and the value in ParamValues (for example, 60.0mm).
- Suppression state of features. Specify the feature name in ParamNames (for example, $STATE@Extrude2) and the suppression state in ParamValues (S=Suppressed or R=Resolved).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.md)  
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.md)  
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.md)  
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.md)  
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)  
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.md)  
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.md)  
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.md)  
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.md)  
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.md)

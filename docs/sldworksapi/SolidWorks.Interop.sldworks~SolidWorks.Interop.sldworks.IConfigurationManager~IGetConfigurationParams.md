# IGetConfigurationParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams`

Gets the parameters for this configuration.
Gets the parameters for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConfigurationParams( _
   ByVal ConfigName As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamValues As System.String _
) As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim ConfigName As System.String
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamValues As System.String
Dim value As System.Boolean
 
value = instance.IGetConfigurationParams(ConfigName, ParamCount, ParamNames, ParamValues)
```

```

System.bool IGetConfigurationParams( 
   System.string ConfigName,
   System.int ParamCount,
   out System.string ParamNames,
   out System.string ParamValues
)
```

```

System.bool IGetConfigurationParams( 
   System.String^ ConfigName,
   System.int ParamCount,
   [Out] System.String^ ParamNames,
   [Out] System.String^ ParamValues
) 
```

#### Parameters

*ConfigName*
:   Name of the configuration

*ParamCount*
:   Number of parameters for this configuration

*ParamNames*
:   - in-process, unmanaged C++: Pointer to an an array of the names of the parameters for this configuration of size ParamCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*ParamValues*
:   - in-process, unmanaged C++: Pointer to an array of values of the parameters for this configuration of size ParamCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if successful in getting the names and values of the parameters for this configuration, false if unsuccessful

Remarks

Call [IConfgurationManager::GetConfigurationParamsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.md) before calling this method to get the value for ParamCount.

The output values may not be accurate if a design table was not added to the model.

Example

[Get Configuration Parameters (C++)](Get_Configuration_Parameters_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.md)  
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.md)  
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.md)  
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)  
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.md)  
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.md)  
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.md)  
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.md)  
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.md)

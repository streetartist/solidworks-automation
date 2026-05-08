# ISetParameters Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters`

Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.
Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetParameters( _
   ByVal NParamCount As System.Integer, _
   ByRef Params As System.String, _
   ByRef Values As System.String _
) 
```

```

Dim instance As IConfiguration
Dim NParamCount As System.Integer
Dim Params As System.String
Dim Values As System.String
 
instance.ISetParameters(NParamCount, Params, Values)
```

```

void ISetParameters( 
   System.int NParamCount,
   ref System.string Params,
   ref System.string Values
)
```

```

void ISetParameters( 
   System.int NParamCount,
   System.String^% Params,
   System.String^% Values
) 
```

#### Parameters

*NParamCount*
:   Number of parameters

*Params*
:   - in-process, unmanaged C++: Pointer to an array of the names of the parameters of size NParamCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Values*
:   - in-process, unmanaged C++: Pointe to an array of the values for the parameters of size NParamCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To get the number of parameters to set for this configuration, call [IConfiguration::GetParameterCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.md).

You can control these parameters in a part document:

- Dimension values. Specify the dimension name in params for example, D1@Sketch1) and the value in values (for example, 60.0mm).
- Suppression state of features. Specify the feature name in params (for example, $STATE@Extrude2) and the suppression state in values (S=suppressed or U=Unsuppressed).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.md)  
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.md)  
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.md)  
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.md)  
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.md)  
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.md)  
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.md)  
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.md)  
[IConfigurationManager::IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.md)

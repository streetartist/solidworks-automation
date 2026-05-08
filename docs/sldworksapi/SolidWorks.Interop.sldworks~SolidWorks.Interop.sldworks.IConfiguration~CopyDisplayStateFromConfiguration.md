# CopyDisplayStateFromConfiguration Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration`

Copies the specified display state from the specified configuration to this configuration.
Copies the specified display state from the specified configuration to this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CopyDisplayStateFromConfiguration( _
   ByVal CopyFromConfig As Configuration, _
   ByVal DisplayStateNameToCopy As System.String _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim CopyFromConfig As Configuration
Dim DisplayStateNameToCopy As System.String
Dim value As System.Boolean
 
value = instance.CopyDisplayStateFromConfiguration(CopyFromConfig, DisplayStateNameToCopy)
```

```

System.bool CopyDisplayStateFromConfiguration( 
   Configuration CopyFromConfig,
   System.string DisplayStateNameToCopy
)
```

```

System.bool CopyDisplayStateFromConfiguration( 
   Configuration^ CopyFromConfig,
   System.String^ DisplayStateNameToCopy
) 
```

#### Parameters

*CopyFromConfig*
:   Pointer to the [configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md) from which to copy the display state

*DisplayStateNameToCopy*
:   Name of the display state to copy

#### Return Value

True if the specified display is copied to this configuration, false if not

Remarks

Use [IConfiguration::GetDisplayStates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md) or [IConfiguration::IGetDisplayStates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.md) to get the names of the display states from the configuration from which to copy the display state.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.md)  
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.md)  
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.md)  
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.md)  
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.md)  
[IConfigurationManager::LinkDisplayStatesToConfigurations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.md)

# GetDisplayStates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates`

Gets the names of the display states for this configuration.
Gets the names of the display states for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayStates() As System.Object
```

```

Dim instance As IConfiguration
Dim value As System.Object
 
value = instance.GetDisplayStates()
```

```

System.object GetDisplayStates()
```

```

System.Object^ GetDisplayStates(); 
```

#### Return Value

Array of the names of the display states for this configuration

Remarks

The first name in the list is the active display state. If more than one display state is active in the current model, call [IComponent2::ReferencedDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState.md) to obtain the active display state for each component in the model that references this configuration.

Example

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)  
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)  
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)  
[Get Display States and Visibilities of Components (C#)](Get_Display_State_Names_and_Visibilites_of_Components_Example_CSharp.htm)  
[Get Display States and Visibilities of Components (VB.NET)](Get_Display_State_Names_and_Visibilites_of_Components_Example_VBNET.htm)  
[Get Display States and Visibilities of Components (VBA)](Get_Display_State_Names_and_Visibilites_of_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.md)  
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.md)  
[IConfiguration::IGetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.md)  
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.md)  
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.md)  
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.md)  
[IConfigurationManager::LinkDisplayStatesToConfigurations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.md)  
[IConfiguration::GetDisplayStateBodyProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.md)  
[IConfiguration::GetDisplayStateComponentProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.md)  
[IConfiguration::GetDisplayStateComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.md)  
[IConfiguration::GetDisplayStateFaceProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.md)  
[IConfiguration::GetDisplayStateFeatureProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.md)  
[IConfiguration::GetDisplayStateProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.md)

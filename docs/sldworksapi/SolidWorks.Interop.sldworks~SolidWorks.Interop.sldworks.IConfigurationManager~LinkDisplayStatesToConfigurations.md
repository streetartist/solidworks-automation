# LinkDisplayStatesToConfigurations Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations`

Gets or sets whether to link or unlink display states to or from the active configuration.
Gets or sets whether to link or unlink display states to or from the active configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkDisplayStatesToConfigurations As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim value As System.Boolean
 
instance.LinkDisplayStatesToConfigurations = value
 
value = instance.LinkDisplayStatesToConfigurations
```

```

System.bool LinkDisplayStatesToConfigurations {get; set;}
```

```

property System.bool LinkDisplayStatesToConfigurations {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to keep specific display states linked to the active configuration, false to unlink specific display states and make all display states available to the active configuration

Example

[Link Display States to Configurations (C#)](Link_Display_States_to_Configurations_Example_CSharp.htm)  
[Link Display States to Configurations (VB.NET)](Link_Display_States_to_Configurations_Example_VBNET.htm)  
[Link Display States to Configurations (VBA)](Link_Display_States_to_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IComponent2::ReferencedDisplayState Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState.md)  
[IConfiguration::ApplyDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.md)  
[IConfiguration::CopyDisplayStateFromConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.md)  
[IConfiguration::CreateDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.md)  
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md)  
[IConfiguration::IGetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.md)  
[IModelDocExtension::LinkedDisplayState Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LinkedDisplayState.md)  
[IPartDoc::RemoveAllDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~RemoveAllDisplayStates.md)  
[IAssemblyDoc ActiveDisplayStateChangePostNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.md)  
[IAssemblyDoc ActiveDisplayStateChangePreNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.md)  
[IPartDoc ActiveDisplayStateChangePostNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.md)  
[IPartDoc ActiveDisplayStateChangePreNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.md)

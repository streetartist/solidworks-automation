# LinkedDisplayState Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LinkedDisplayState`

Gets or sets whether a display state is linked in this part.
Gets or sets whether a display state is linked in this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkedDisplayState As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
instance.LinkedDisplayState = value
 
value = instance.LinkedDisplayState
```

```

System.bool LinkedDisplayState {get; set;}
```

```

property System.bool LinkedDisplayState {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if linked, false if not linked

Example

[Create, Unlink, and Purge Display States in Part (VB.NET)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VBNET.htm)  
[Create, Unlink, and Purge Display States in Part (VBA)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VB.htm)  
[Create, Unlink, and Purge Display States in Part (C#)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.md)  
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.md)  
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.md)  
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md)  
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.md)  
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.md)  
[IModelDocExtension::PurgeDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PurgeDisplayState.md)  
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.md)

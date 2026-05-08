# SetSpeedPakConfigurations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations`

Sets the configurations in the selected subassemblies to which to apply SpeedPak in this assembly.
Sets the configurations in the selected subassemblies to which to apply SpeedPak in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSpeedPakConfigurations( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetSpeedPakConfigurations(Config_opt, Config_names)
```

```

System.bool SetSpeedPakConfigurations( 
   System.int Config_opt,
   System.object Config_names
)
```

```

System.bool SetSpeedPakConfigurations( 
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html) (see **Remarks**)

*Config\_names*
:   Array of the names of the configurations in the selected subassemblies to which to apply SpeedPak; valid only if Config\_opt = swInConfigurationOpts\_e.swSpecifyConfiguration (see **Remarks**)

#### Return Value

True if the specified configurations in the selected subassemblies are applied SpeedPak, false if not

Remarks

Valid option for Config\_opt is:

- swInConfigurationOpts\_e.swAllConfiguration,
- swInConfigurationOpts\_e.swSpecifyConfiguration, or
- swInConfigurationOpts\_e.swThisConfiguration

If Config\_names = swInConfigurationOpts\_e.swAllConfiguration or swInConfigurationOpts\_e.swThisConfiguration, then pass Nothing or null.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::CreateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.md)  
[IAssemblyDoc::SetSpeedPakToParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.md)  
[IAssemblyDoc::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.md)  
[IAssemblyDoc::UseSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.md)  
[IAssemblyDoc::IsSpeedPak Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak.md)

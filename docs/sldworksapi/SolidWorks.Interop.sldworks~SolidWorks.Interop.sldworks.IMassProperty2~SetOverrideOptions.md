# SetOverrideOptions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SetOverrideOptions`

Sets the mass property override options for the selected bodies/components.
Sets the mass property override options for the selected bodies/components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideOptions( _
   ByVal Options As System.Object, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IMassProperty2
Dim Options As System.Object
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetOverrideOptions(Options, Config_option, Config_names)
```

```

System.bool SetOverrideOptions( 
   System.object Options,
   System.int Config_option,
   System.object Config_names
)
```

```

System.bool SetOverrideOptions( 
   System.Object^ Options,
   System.int Config_option,
   System.Object^ Config_names
) 
```

#### Parameters

*Options*
:   [IMassPropertyOverrideOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)

*Config\_option*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names; valid only if Config\_option = swInConfigurationOpts\_e.swSpecifyConfiguration

#### Return Value

True if the mass property override options are set successfully, false if not

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)  
[IMassProperty2::GetOverrideOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetOverrideOptions.md)

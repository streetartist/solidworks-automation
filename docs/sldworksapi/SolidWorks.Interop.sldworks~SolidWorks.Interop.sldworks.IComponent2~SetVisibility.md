# SetVisibility Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility`

Sets the visibility state for this component.
Sets the visibility state for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVisibility( _
   ByVal State As System.Integer, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) 
```

```

Dim instance As IComponent2
Dim State As System.Integer
Dim Config_opt As System.Integer
Dim Config_names As System.Object
 
instance.SetVisibility(State, Config_opt, Config_names)
```

```

void SetVisibility( 
   System.int State,
   System.int Config_opt,
   System.object Config_names
)
```

```

void SetVisibility( 
   System.int State,
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*State*
:   Visibility state as defined in [swComponentVisibilityState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentVisibilityState_e.html)

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names; valid only if Config\_opt is set to swInConfigurationOpts\_e.swSpecifyConfiguration

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.md)  
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.md)  
[IComponent2::IGetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetVisibility.md)  
[IComponent2::GetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibility.md)  
[IComponent2::IsHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.md)

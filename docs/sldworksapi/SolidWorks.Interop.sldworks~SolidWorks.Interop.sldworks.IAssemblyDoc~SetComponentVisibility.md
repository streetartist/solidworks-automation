# SetComponentVisibility Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentVisibility`

Hides or shows the selected component in the specified configurations in this assembly document.
Hides or shows the selected component in the specified configurations in this assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetComponentVisibility( _
   ByVal Visibility As System.Boolean, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) 
```

```

Dim instance As IAssemblyDoc
Dim Visibility As System.Boolean
Dim Config_opt As System.Integer
Dim Config_names As System.Object
 
instance.SetComponentVisibility(Visibility, Config_opt, Config_names)
```

```

void SetComponentVisibility( 
   System.bool Visibility,
   System.int Config_opt,
   System.object Config_names
)
```

```

void SetComponentVisibility( 
   System.bool Visibility,
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Visibility*
:   True to show the selected component, false to hide it

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of the names of the configurations for the component

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.md)  
[IComponent2::GetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibility.md)  
[IComponent2::SetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.md)  
[IComponent2::IGetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetVisibility.md)  
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.md)  
[IAssemblyDoc::ISetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentVisibility.md)

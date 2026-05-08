# RemoveTexture Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTexture`

Removes the texture from this component in the specified configuration.
Removes the texture from this component in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveTexture( _
   ByVal Config_name As System.String _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim Config_name As System.String
Dim value As System.Boolean
 
value = instance.RemoveTexture(Config_name)
```

```

System.bool RemoveTexture( 
   System.string Config_name
)
```

```

System.bool RemoveTexture( 
   System.String^ Config_name
) 
```

#### Parameters

*Config\_name*
:   Name of the configuration

#### Return Value

True if texture is removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.md)  
[IComponent2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTexture.md)  
[IComponent2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTextureByDisplayState.md)  
[IComponent2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTextureByDisplayState.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

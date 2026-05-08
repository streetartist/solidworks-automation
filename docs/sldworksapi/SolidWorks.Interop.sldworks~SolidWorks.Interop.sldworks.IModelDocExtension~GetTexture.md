# GetTexture Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture`

Gets the texture applied to the specified configuration.
Gets the texture applied to the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTexture( _
   ByVal Config_name As System.String _
) As Texture
```

```

Dim instance As IModelDocExtension
Dim Config_name As System.String
Dim value As Texture
 
value = instance.GetTexture(Config_name)
```

```

Texture GetTexture( 
   System.string Config_name
)
```

```

Texture^ GetTexture( 
   System.String^ Config_name
) 
```

#### Parameters

*Config\_name*
:   Name of configuration or NULL if texture is not present

#### Return Value

[Texture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)

Example

[Remove Textures from Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)  
[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.md)  
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.md)  
[IModelDocExtension::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.md)  
[IModelDocExtension::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.md)

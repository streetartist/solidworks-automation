# RemoveTexture2 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2`

Removes the texture from the specified configuration.
Removes the texture from the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveTexture2( _
   ByVal Config_name As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Config_name As System.String
Dim value As System.Boolean
 
value = instance.RemoveTexture2(Config_name)
```

```

System.bool RemoveTexture2( 
   System.string Config_name
)
```

```

System.bool RemoveTexture2( 
   System.String^ Config_name
) 
```

#### Parameters

*Config\_name*
:   Name of the configuration

#### Return Value

True if the texture is removed, false if not

Example

[Remove Textures from Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)  
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.md)  
[IModelDocExtension::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.md)  
[IModelDocExtension::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.md)  
[IModelDocExtension::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.md)  
[IFace2::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture2.md)

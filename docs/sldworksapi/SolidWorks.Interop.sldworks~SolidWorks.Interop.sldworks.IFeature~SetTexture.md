# SetTexture Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture`

Applies texture to this feature in either all configurations or only the specified configuration.
Applies texture to this feature in either all configurations or only the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTexture( _
   ByVal BAllConfig As System.Boolean, _
   ByVal Config_name As System.String, _
   ByVal TextureIn As Texture _
) As System.Boolean
```

```

Dim instance As IFeature
Dim BAllConfig As System.Boolean
Dim Config_name As System.String
Dim TextureIn As Texture
Dim value As System.Boolean
 
value = instance.SetTexture(BAllConfig, Config_name, TextureIn)
```

```

System.bool SetTexture( 
   System.bool BAllConfig,
   System.string Config_name,
   Texture TextureIn
)
```

```

System.bool SetTexture( 
   System.bool BAllConfig,
   System.String^ Config_name,
   Texture^ TextureIn
) 
```

#### Parameters

*BAllConfig*
:   True to apply texture to this feature all configurations, false to apply texture to this feature in the configuration specified in config\_name only

*Config\_name*
:   Name of configuration

*TextureIn*
:   Pointer to the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md) object

#### Return Value

True if texture is applied, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.md)  
[IFeature::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)  
[IFeature::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.md)  
[IFeature::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.md)

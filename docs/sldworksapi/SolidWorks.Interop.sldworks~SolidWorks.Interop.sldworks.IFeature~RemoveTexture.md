# RemoveTexture Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture`

Removes texture from this feature in either all of the configurations or only the specified configuration.
Removes texture from this feature in either all of the configurations or only the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveTexture( _
   ByVal BAllConfig As System.Boolean, _
   ByVal Config_name As System.String _
) As System.Boolean
```

```

Dim instance As IFeature
Dim BAllConfig As System.Boolean
Dim Config_name As System.String
Dim value As System.Boolean
 
value = instance.RemoveTexture(BAllConfig, Config_name)
```

```

System.bool RemoveTexture( 
   System.bool BAllConfig,
   System.string Config_name
)
```

```

System.bool RemoveTexture( 
   System.bool BAllConfig,
   System.String^ Config_name
) 
```

#### Parameters

*BAllConfig*
:   True to remove texture from this feature in all configurations, false to remove texture from this feature in the configuration specified in Config\_name only

*Config\_name*
:   Name of configuration

#### Return Value

True if texture is removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.md)  
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.md)  
[IFeature::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.md)  
[IFeature::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

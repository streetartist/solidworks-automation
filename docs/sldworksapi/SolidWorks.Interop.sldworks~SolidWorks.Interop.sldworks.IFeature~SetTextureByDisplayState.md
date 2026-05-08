# SetTextureByDisplayState Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState`

Applies texture to this feature in the specified display state.
Applies texture to this feature in the specified display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTextureByDisplayState( _
   ByVal DisplayStateName As System.String, _
   ByVal TextureIn As Texture _
) As System.Boolean
```

```

Dim instance As IFeature
Dim DisplayStateName As System.String
Dim TextureIn As Texture
Dim value As System.Boolean
 
value = instance.SetTextureByDisplayState(DisplayStateName, TextureIn)
```

```

System.bool SetTextureByDisplayState( 
   System.string DisplayStateName,
   Texture TextureIn
)
```

```

System.bool SetTextureByDisplayState( 
   System.String^ DisplayStateName,
   Texture^ TextureIn
) 
```

#### Parameters

*DisplayStateName*
:   Display state name

*TextureIn*
:   [Texture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)

#### Return Value

True if the texture is applied to the feature, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.md)  
[IFeature::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.md)  
[IFeature::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.md)  
[IFeature::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

# RemoveTextureByDisplayState Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState`

Removes texture from this feature in the specified display state.
Removes texture from this feature in the specified display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveTextureByDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Boolean
```

```

Dim instance As IFeature
Dim DisplayStateName As System.String
Dim value As System.Boolean
 
value = instance.RemoveTextureByDisplayState(DisplayStateName)
```

```

System.bool RemoveTextureByDisplayState( 
   System.string DisplayStateName
)
```

```

System.bool RemoveTextureByDisplayState( 
   System.String^ DisplayStateName
) 
```

#### Parameters

*DisplayStateName*
:   Display state name

#### Return Value

True to remove texture from the feature, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.md)  
[IFeature::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.md)  
[IFeature::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.md)  
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

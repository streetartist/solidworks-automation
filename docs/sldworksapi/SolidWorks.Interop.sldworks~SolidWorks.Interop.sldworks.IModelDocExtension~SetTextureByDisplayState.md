# SetTextureByDisplayState Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState`

Sets the texture applied to this model in the specified display state.
Sets the texture applied to this model in the specified display state.

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

Dim instance As IModelDocExtension
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
:   Name of display state

*TextureIn*
:   [Texture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)

#### Return Value

True if texture is set on the model, false if not

Example

[Apply and Remove Texture To and From Model by Display State (C#)](Apply_and_Remove_Texture_By_Model_Display_State_Example_CSharp.htm)  
[Apply and Removed Texture To and From Model By Display State (VB.NET)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VBNET.htm)  
[Apply and Remove Texture To and From Model By Display State (VBA)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtenson::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.md)  
[IModelDocExtenson::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.md)  
[IModelDocExtenson::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.md)  
[IModelDocExtenson::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.md)  
[IModelDocExtenson::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

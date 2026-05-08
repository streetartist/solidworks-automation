# SetTextureByDisplayState Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTextureByDisplayState`

Sets the texture applied to this component in the specified display state.
Sets the texture applied to this component in the specified display state.

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

Dim instance As IComponent2
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

True if texture is applied to the component, false if not

Example

[Apply and Remove Texture To and From Component By Display State (C#)](Apply_and_Remove_Texture_By_Component_Display_State_Example_CSharp.htm)  
[Apply and Remove Texture To and From Component By Display State (VB.NET)](Apply_and_Remove_Texture_By_Component_Display_State_Example_VBNET.htm)  
[Apply and Remove Texture To and From Component By Display State (VBA)](Apply_and_Remove_Texture_By_Component_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTextureByDisplayState.md)  
[IComponent2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveTexture.md)  
[IComponent2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTexture.md)  
[IComponent2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

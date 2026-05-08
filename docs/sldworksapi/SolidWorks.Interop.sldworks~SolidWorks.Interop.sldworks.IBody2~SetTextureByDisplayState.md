# SetTextureByDisplayState Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState`

Sets the texture applied to this body in the specified display state.
Sets the texture applied to this body in the specified display state.

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

Dim instance As IBody2
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
:   :   Display state name

*TextureIn*
:   [Texture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)

#### Return Value

True if texture applied to body, false if not

Example

[Apply and Remove Texture By Body Display State (C#)](Apply_and_Remove_Texture_By_Body_Display_State_Example_CSharp.htm)  
[Apply and Remove Texture By Body Display State (VB.NET)](Apply_and_Remove_Texture_By_Body_Display_State_Example_VBNET.htm)  
[Apply and Remove Texture By Body Display State (VBA)](Apply_and_Remove_Texture_By_Body_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.md)  
[IBody2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.md)  
[IBody2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.md)  
[IBody2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTexture.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

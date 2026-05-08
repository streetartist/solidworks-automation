# RemoveTextureByDisplayState Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState`

Removes the texture applied to this face in the specified display state.
Removes the texture applied to this face in the specified display state.

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

Dim instance As IFace2
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

True if the texture is removed, false if not

Example

[Apply and Remove Texture By Display State (C#)](Apply_and_Remove_Texture_By_Display_State_Example_CSharp.htm)  
[Apply and Remove Texture By Display State (VB.NET)](Apply_and_Remove_Texture_By_Display_State_Example_VBNET.htm)  
[Apply and Remove Texture By Display State (VBA)](Apply_and_Remove_Texture_By_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.md)  
[IFace2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.md)  
[IFace2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture.md)  
[IFace2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

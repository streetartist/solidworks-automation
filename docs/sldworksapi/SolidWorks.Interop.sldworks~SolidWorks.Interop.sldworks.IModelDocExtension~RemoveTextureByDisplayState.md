# RemoveTextureByDisplayState Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState`

Removes the texture applied to this model in the specified display state.
Removes the texture applied to this model in the specified display state.

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

Dim instance As IModelDocExtension
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
:   Name of display state

#### Return Value

True if texture removed from model, false if not

Example

[Apply and Remove Texture To and From Model By Display State (C#)](Apply_and_Remove_Texture_By_Model_Display_State_Example_CSharp.htm)  
[Apply and Remove Texture To and From Model By Display State (VB.NET)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VBNET.htm)  
[Apply and Remove Texture To and From Model By Display State (VBA)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.md)  
[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.md)  
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.md)  
[IModelDocExtension::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.md)  
[IModelDocExtenson::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

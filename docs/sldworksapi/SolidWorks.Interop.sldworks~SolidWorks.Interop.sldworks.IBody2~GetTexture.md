# GetTexture Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTexture`

Gets the texture applied to this body in the specified configuration.
Gets the texture applied to this body in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTexture( _
   ByVal Config_name As System.String _
) As Texture
```

```

Dim instance As IBody2
Dim Config_name As System.String
Dim value As Texture
 
value = instance.GetTexture(Config_name)
```

```

Texture GetTexture( 
   System.string Config_name
)
```

```

Texture^ GetTexture( 
   System.String^ Config_name
) 
```

#### Parameters

*Config\_name*
:   Name of the configuration

#### Return Value

|  |  |
| --- | --- |
| **If texture is...** | **Then retval is...** |
| Applied to this body in Config\_name | Pointer to [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md) object |
| Not present | NULL |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.md)  
[IBody2::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.md)  
[IBody2::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.md)  
[IBody2::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState.md)  
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.md)

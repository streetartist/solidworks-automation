# GetModelTexture Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelTexture`

Gets the texture applied to this lightweight component in the specified configuration.
Gets the texture applied to this lightweight component in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelTexture( _
   ByVal ConfigName As System.String _
) As Texture
```

```

Dim instance As IComponent2
Dim ConfigName As System.String
Dim value As Texture
 
value = instance.GetModelTexture(ConfigName)
```

```

Texture GetModelTexture( 
   System.string ConfigName
)
```

```

Texture^ GetModelTexture( 
   System.String^ ConfigName
) 
```

#### Parameters

*ConfigName*
:   Name of the configuration

#### Return Value

[ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)

Example

[Get Model Textures (VBA)](Get_Model_Texture_Example_VB.htm)  
[Get Model Textures (VB.NET)](Get_Model_Texture_Example_VBNET.htm)  
[Get Model Textures (C#)](Get_Model_Texture_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTexture.md)

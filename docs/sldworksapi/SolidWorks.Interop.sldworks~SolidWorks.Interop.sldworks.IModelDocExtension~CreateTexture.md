# CreateTexture Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture`

Creates a texture.
Creates a texture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTexture( _
   ByVal MatName As System.String, _
   ByVal Scale As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Blend As System.Boolean _
) As Texture
```

```

Dim instance As IModelDocExtension
Dim MatName As System.String
Dim Scale As System.Double
Dim Angle As System.Double
Dim Blend As System.Boolean
Dim value As Texture
 
value = instance.CreateTexture(MatName, Scale, Angle, Blend)
```

```

Texture CreateTexture( 
   System.string MatName,
   System.double Scale,
   System.double Angle,
   System.bool Blend
)
```

```

Texture^ CreateTexture( 
   System.String^ MatName,
   System.double Scale,
   System.double Angle,
   System.bool Blend
) 
```

#### Parameters

*MatName*
:   Name of the texture file

*Scale*
:   Value by which to adjust the granularity of the texture; value between 0.001 and 1000000.00

*Angle*
:   Value by which to adjust the rotation of the texture; value between 0.0 and 360.0

*Blend*
:   True to blend the part color with the texture color, false to not

#### Return Value

[ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)

Example

[Apply and Remove Texture To and From Model By Display State (VB.NET)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VBNET.htm)  
[Apply and Remove Texture To and From Model By Display State (C#)](Apply_and_Remove_Texture_By_Model_Display_State_Example_CSharp.htm)  
[Apply and Remove Texture To and From Model By Display State (VBA)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VB.htm)  
[Change Texture on Face in Specified Configuration (VBA)](Change_Texture_on_Face_in_Specified_Configuration_Example_VB.htm)  
[Change Texture on Face in Specified Configuration (VB.NET)](Change_Texture_on_Face_in_Specified_Configuration_Example_VBNET.htm)  
[Change Texture on Face in Specified Configuration (C#)](Change_Texture_on_Face_in_Specified_Configuration_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.md)  
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.md)  
[IModelDocExtension::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.md)  
[IModelDocExtenson::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.md)  
[IModelDocExtenson::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.md)

# ApplyTexture Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ApplyTexture`

Obsolete. Superseded by IModelDocExtension::SetTexture.
Obsolete. Superseded by [IModelDocExtension::SetTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ApplyTexture( _
   ByVal Scale As System.Integer, _
   ByVal Angle As System.Double, _
   ByVal TextureFilename As System.String, _
   ByVal BlendColor As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Scale As System.Integer
Dim Angle As System.Double
Dim TextureFilename As System.String
Dim BlendColor As System.Boolean
Dim value As System.Boolean
 
value = instance.ApplyTexture(Scale, Angle, TextureFilename, BlendColor)
```

```

System.bool ApplyTexture( 
   System.int Scale,
   System.double Angle,
   System.string TextureFilename,
   System.bool BlendColor
)
```

```

System.bool ApplyTexture( 
   System.int Scale,
   System.double Angle,
   System.String^ TextureFilename,
   System.bool BlendColor
) 
```

#### Parameters

*Scale*

*Angle*

*TextureFilename*

*BlendColor*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)

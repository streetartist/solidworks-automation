# TextureRenderMode Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureRenderMode`

Gets the render mode of the texture of the decal.
Gets the render mode of the texture of the decal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property TextureRenderMode As System.Integer
```

```

Dim instance As IFaceDecalProperties
Dim value As System.Integer
 
value = instance.TextureRenderMode
```

```

System.int TextureRenderMode {get;}
```

```

property System.int TextureRenderMode {
   System.int get();
}
```

#### Property Value

Render mode of the texture of the decal:

- 0 = Image
- 1 = Luminance

Example

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.md)  
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.md)

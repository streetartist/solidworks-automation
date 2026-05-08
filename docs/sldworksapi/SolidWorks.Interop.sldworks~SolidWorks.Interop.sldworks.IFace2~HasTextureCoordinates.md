# HasTextureCoordinates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates`

Gets whether this face has texture coordinates.
Gets whether this face has texture coordinates.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HasTextureCoordinates() As System.Boolean
```

```

Dim instance As IFace2
Dim value As System.Boolean
 
value = instance.HasTextureCoordinates()
```

```

System.bool HasTextureCoordinates()
```

```

System.bool HasTextureCoordinates(); 
```

#### Return Value

True if texture coordinates exist, false if not

Remarks

Call this method before calling [IFace2::GetTessTriStripTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripTextures.md).

Texture coordinates are generated only when mapping type is set to surface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetTessTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.md)  
[IFace2::GetTexture Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.md)  
[IFace2::RemoveTexture2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture2.md)  
[IFace2::RemoveTextureByDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.md)  
[IFace2::SetTexture Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.md)  
[IFace2::SetTextureByDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.md)  
[IFace2::GetSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.md)

# GetTessTriStripTextures Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripTextures`

Gets the texture coordinate components for each vertex on each triangle strip on this face.
Gets the texture coordinate components for each vertex on each triangle strip on this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessTriStripTextures() As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
value = instance.GetTessTriStripTextures()
```

```

System.object GetTessTriStripTextures()
```

```

System.Object^ GetTessTriStripTextures(); 
```

#### Return Value

Array containing the triangle strip texture coordinate components (see **Remarks**)

Remarks

Before calling this method, call [IFace2::HasTextureCoordinates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.md).

The format of the returned data is:

     DWORD NumStrips

     DWORD [] *VertexesPerStrip*

     Double [] *TextureCoords*

where:

- NumStrips = Number of tri strips on this face
- VertexPerStrip = Array containing the number of vertex points on each tri strip
- TextureCoords = Array from 0 to (*VertexPerStrip* - 1) containing the U,V texture coordinate components for each vertex on each tri strip

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IPartDoc::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures.md)  
[IFace2::GetTessNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.md)  
[IFace2::GetTessTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.md)  
[IFace2::GetTessTriangleCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.md)  
[IFace2::GetTessTriangles Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.md)  
[IFace2::GetTessTriStripEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.md)  
[IFace2::GetTessTriStripNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.md)  
[IFace2::GetTessTriStrips Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.md)  
[IFace2::GetTessTriStripSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.md)

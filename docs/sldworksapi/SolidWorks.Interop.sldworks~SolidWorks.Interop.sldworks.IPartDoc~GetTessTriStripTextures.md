# GetTessTriStripTextures Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures`

Gets the texture coordinate components for each vertex on each triangle strip on each face of this part.
Gets the texture coordinate components for each vertex on each triangle strip on each face of this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessTriStripTextures() As System.Object
```

```

Dim instance As IPartDoc
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

The format of the returned data is:

|  |  |  |
| --- | --- | --- |
|  | DWORD FaceCount |  |
|  | DWORD StripCount |  |
|  | DWORD *Vertex*Count |  |
|  | DWORD *FaceStripCount* |  |
|  | DWORD [] *VertexesPerTriStrip* |  |
|  | Double [] *TextureCoords* |  |

where:

|  |  |  |
| --- | --- | --- |
|  | FaceCount: | Number of faces on the body |
|  | StripCount: | Total number of tri strips on the body |
|  | VertexCount: | Total number of vertexes (multiplied by 2 for U and V coordinates) |
|  | FaceStripCount: | Number of tri strips on each face |
|  | *VertexesPerTriStrip*: | Array from 0 to (*FaceStripCount* - 1 ) containing the number of vertexes on each face tri strip |
|  | TextureCoords: | Array from 0 to (*VertexesPerTriStrip* - 1) containing the U,V texture coordinate components for each vertex on each face tri strip |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IFace2::GetTessTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.md)  
[IPartDoc::GetTessNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.md)  
[IPartDoc::GetTessTriangleCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.md)  
[IPartDoc::GetTessTriangles Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.md)  
[IPartDoc::GetTessTriStripEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.md)  
[IPartDoc::GetTessTriStripNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.md)  
[IPartDoc::GetTessTriStrips Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStrips.md)  
[IPartDoc::GetTessTriStripSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.md)  
[IFace2::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripTextures.md)

# GetTessTriStripEdges Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges`

Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face.
Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessTriStripEdges() As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
value = instance.GetTessTriStripEdges()
```

```

System.object GetTessTriStripEdges()
```

```

System.Object^ GetTessTriStripEdges(); 
```

#### Return Value

Array that contains the list of edge IDs for this face (see **Remarks**)

Remarks

Returns an array of long or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) values that indicate which edges of the given triangle strip represent a face boundary. The array takes the form of:

[nStrips,

  stripEdgeCount1, stripEdgeCount2,..., stripVertCountN,

  strip1[triStripFlag, stripEdgeCount1 elements],

  strip2[triStripFlag, stripEdgeCount2 elements],...,

  stripN[triStripFlag, stripEdgeCountN elements&cd;

where:

nStrips = The number of triangle strips on the face.

stripEdgeCountN = The number of triangle edges for the Nth triangle strip + 1.

stripN = A sub-array that consists of the triStripFlag and an array of stripEdgeCountN edgeIds.

triStripFlag = Indicates if the triangle strip is a strip (=1) or if the triangle strip is a triangle (=0).

edgeId = An identifier with an arbitrary value that represents the edge of the face. Each edge has a unique edgeId.

|  |  |
| --- | --- |
|  | If you have this triangle strip, then you get a stripVertexCount of 10 using [IFace2::GetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.md) or [IFace2::IGetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.md). IFace2::GetTessTriStripEdges and [IFace2::IGetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.md) get a stripEdgeCount of 18. This means that for each triangle strip stripEdgeCount - 1 = 2(stripVertexCount - 2) + 1. The first element represents a flag indicating if the current strip is a triangle strip or a simple triangle, 1 or 0, respectively.    If one of the triangle strip edges lies on a face edge, then the value of stripN[i] = edgeId. If the triangle strip edge does not lie on a face edge, then the value of stripN[i] = 0. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.md)  
[IFace2::GetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.md)  
[IFace2::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.md)  
[IFace2::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.md)  
[IFace2::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.md)  
[IFace2::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.md)  
[IFace2::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.md)  
[IFace2::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.md)  
[IFace2::IGetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTextures.md)  
[IFace2::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.md)  
[IFace2::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.md)  
[IFace2::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdgeSize.md)  
[IFace2::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.md)  
[IFace2::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.md)

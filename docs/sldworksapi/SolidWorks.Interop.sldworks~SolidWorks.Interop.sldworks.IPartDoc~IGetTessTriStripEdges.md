# IGetTessTriStripEdges Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdges`

Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part.
Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessTriStripEdges() As System.Integer
```

```

Dim instance As IPartDoc
Dim value As System.Integer
 
value = instance.IGetTessTriStripEdges()
```

```

System.int IGetTessTriStripEdges()
```

```

System.int IGetTessTriStripEdges(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of longs containing the list of edge IDs for this part document (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The format of the returned data is:

|  |  |  |
| --- | --- | --- |
|  | DWORD FaceCount |  |
|  | DWORD StripCount |  |
|  | DWORD EdgeCount |  |
|  | ForEach Face |  |
|  | DWORD StripCount |  |
|  | DWORD [StripLengths] |  |
|  | ForEach Strip | (where this is an array of edge IDs for each strip from 1 to (VertexPerStrip-1). Element 0 indicates if that a triangle strip exists (value = 1) or a single triangle (value = 0)) |
|  | Long [EdgeIds] |  |

where:

|  |  |  |
| --- | --- | --- |
|  | FaceCount: | Number of faces on the body |
|  | StripCount: | Total number of strips on the body |
|  | EdgeCount: | Total number of vertices |
|  | NumStrips: | Number of strips on a particular face |
|  | StripLengths: | Array containing the number of vertex points on particular face strip |
|  | EdgeIds: | Array of edge IDs for each vertex on the particular face strip |

For triangle strips, EdgeIds is:

If the strip has n vertices, then there are 2(n 2) + 1 edge tags. The i-th element of the tags array (starting at i = 1) will be the tag of the edge between vertex floor((i 1) / 2) + 1 and vertex floor(i/2) + 2, where floor(x) is the integer portion of x.

For single triangles, EdgeIds is:

The i-th element of the tags array (starting at i = 1) will be the tag of the edge between vertex i-1 (if i=1 then i=n) and vertex i.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.md)  
[IPartDoc::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.md)  
[IPartDoc::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.md)  
[IPartDoc::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.md)  
[IPartDoc::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.md)  
[IPartDoc::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStrips.md)  
[IPartDoc::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.md)  
[IPartDoc::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessNorms.md)  
[IPartDoc::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriangles.md)  
[IPartDoc::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdgeSize.md)  
[IPartDoc::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripNorms.md)  
[IPartDoc::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStrips.md)  
[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)

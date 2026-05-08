# IImprintingFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFaces`

Imprints the specified tool faces onto the specified target faces.
Imprints the specified tool faces onto the specified target faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IImprintingFaces( _
   ByRef TargetEdges As Edge, _
   ByRef ToolEdges As Edge, _
   ByRef TargetVertices As Vertex, _
   ByRef ToolVertices As Vertex _
) 
```

```

Dim instance As IModeler
Dim TargetEdges As Edge
Dim ToolEdges As Edge
Dim TargetVertices As Vertex
Dim ToolVertices As Vertex
 
instance.IImprintingFaces(TargetEdges, ToolEdges, TargetVertices, ToolVertices)
```

```

void IImprintingFaces( 
   out Edge TargetEdges,
   out Edge ToolEdges,
   out Vertex TargetVertices,
   out Vertex ToolVertices
)
```

```

void IImprintingFaces( 
   [Out] Edge^ TargetEdges,
   [Out] Edge^ ToolEdges,
   [Out] Vertex^ TargetVertices,
   [Out] Vertex^ ToolVertices
) 
```

#### Parameters

*TargetEdges*
:   Array of target [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*ToolEdges*
:   Array of tool [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*TargetVertices*
:   Array of target [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

*ToolVertices*
:   Array of tool [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Remarks

Call [IModeler::IImprintingFacesCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2.md) before calling this method.

The target and tool faces must:

- belong to different bodies.
- intersect each other.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ImprintingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ImprintingFaces.md)

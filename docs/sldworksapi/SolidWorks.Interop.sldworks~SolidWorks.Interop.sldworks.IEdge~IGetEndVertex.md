# IGetEndVertex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex`

Gets the ending vertex for this edge.
Gets the ending vertex for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEndVertex() As Vertex
```

```

Dim instance As IEdge
Dim value As Vertex
 
value = instance.IGetEndVertex()
```

```

Vertex IGetEndVertex()
```

```

Vertex^ IGetEndVertex(); 
```

#### Return Value

Pointer to the [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Remarks

If no vertex exists for this edge (such as the edge of a newly created cylinder), then this method returns NULL.

This method and [IEdge::GetStartVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.md) or [IEdge::IGetStartVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.md) return distinct vertices, unless the edge is closed. Because edges have no natural direction, you cannot necessarily predict which of the two points you will get first and which last.

Use [ICoEdge::GetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md) or [ICoEdge::IGetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md) to get consistent start and end positions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.md)  
[IEdge::GetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.md)  
[IEdge::IGetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.md)

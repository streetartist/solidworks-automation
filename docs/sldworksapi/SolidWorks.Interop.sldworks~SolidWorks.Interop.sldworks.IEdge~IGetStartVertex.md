# IGetStartVertex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex`

Gets the starting vertex for this edge.
Gets the starting vertex for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetStartVertex() As Vertex
```

```

Dim instance As IEdge
Dim value As Vertex
 
value = instance.IGetStartVertex()
```

```

Vertex IGetStartVertex()
```

```

Vertex^ IGetStartVertex(); 
```

#### Return Value

Pointer to the [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Remarks

If no vertex exists for this edge (such as the edge of a newly created cylinder), then this method returns NULL.

This method and [IEdge::GetEndVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.md) or [IEdge::IGetEndVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.md) return distinct vertices, unless the edge is closed.  
Because edges have no natural direction, you cannot necessarily predict which of the two points you will get first and which last.

Use [ICoEdge::GetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md) or [ICoEdge::IGetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md) to get consistent start and end positions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.md)  
[IEdge::GetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.md)  
[IEdge::IGetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.md)

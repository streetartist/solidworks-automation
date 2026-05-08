# GetTangentEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdges`

Gets all of the edges tangent to this edge.
Gets all of the edges tangent to this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTangentEdges() As System.Object
```

```

Dim instance As IEdge
Dim value As System.Object
 
value = instance.GetTangentEdges()
```

```

System.object GetTangentEdges()
```

```

System.Object^ GetTangentEdges(); 
```

#### Return Value

Array of tangent edges

Example

[Select Tangent Edges Topologically (VBA)](Select_Tangent_Edges_Topologically_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::IGetTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTangentEdges.md)  
[IEdge::GetTangentEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdgesCount.md)  
[IModelDoc2::SelectTangency Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectTangency.md)

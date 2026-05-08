# GetCoEdges Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCoEdges`

Gets the coedges that reference this edge.
Gets the coedges that reference this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoEdges() As System.Object
```

```

Dim instance As IEdge
Dim value As System.Object
 
value = instance.GetCoEdges()
```

```

System.object GetCoEdges()
```

```

System.Object^ GetCoEdges(); 
```

#### Return Value

Array of coedges that reference the edge

Remarks

Call this method for body-related edges, not reference curve or sketch edges.

Example

[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)  
[Select Tangent Edges Via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)

# GetTangentEdgesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdgesCount`

Gets the number of edges tangent to this edge.
Gets the number of edges tangent to this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTangentEdgesCount() As System.Integer
```

```

Dim instance As IEdge
Dim value As System.Integer
 
value = instance.GetTangentEdgesCount()
```

```

System.int GetTangentEdgesCount()
```

```

System.int GetTangentEdgesCount(); 
```

#### Return Value

Number of tangent edges

Remarks

Call this method before calling [IEdge::IGetTangentEdges.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTangentEdges.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdges.md)

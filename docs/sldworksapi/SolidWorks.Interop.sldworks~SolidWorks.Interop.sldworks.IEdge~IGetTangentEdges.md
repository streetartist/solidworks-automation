# IGetTangentEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTangentEdges`

Gets all of the edges tangent to this edge.
Gets all of the edges tangent to this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTangentEdges( _
   ByVal Count As System.Integer _
) As Edge
```

```

Dim instance As IEdge
Dim Count As System.Integer
Dim value As Edge
 
value = instance.IGetTangentEdges(Count)
```

```

Edge IGetTangentEdges( 
   System.int Count
)
```

```

Edge^ IGetTangentEdges( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of tangent edges

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IEdge::GetTangentEdgesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdgesCount.md) before this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdges.md)  
[IModelDoc2::SelectTangency Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectTangency.md)

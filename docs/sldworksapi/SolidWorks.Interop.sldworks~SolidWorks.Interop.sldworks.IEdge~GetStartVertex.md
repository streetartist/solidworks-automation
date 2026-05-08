# GetStartVertex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex`

Gets the starting vertex for this edge.
Gets the starting vertex for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetStartVertex() As System.Object
```

```

Dim instance As IEdge
Dim value As System.Object
 
value = instance.GetStartVertex()
```

```

System.object GetStartVertex()
```

```

System.Object^ GetStartVertex(); 
```

#### Return Value

Vertex

Remarks

If no vertex exists for this edge (such as the edge of a newly created cylinder), then this method returns null.

This method and [IEdge::GetEndVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.md) or [IEdge::IGetEndVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.md) return distinct vertices, unless the edge is closed.  
Because edges have no natural direction, you cannot necessarily predict which of the two points you will get first and which last.

Use [ICoEdge::GetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md) or [ICoEdge::IGetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md) to get consistent start and end positions.

Example

[Check Interference Using IModeler::CheckInterference (VBA)](Check_Interference_using_Modeler_CheckInterference_Example_VB.htm)  
[Display Vertices (VBA)](Display_Vertices_Example_VB.htm)  
[Get Radius of Variable Radius Fillet (VBA)](Get_Radius_of_Variable_Radius_Fillet_Example_VB.htm)  
[Get Vertex (VBA)](Get_Vertex_Example_VB.htm)  
[Modify Fillet Weld Bead (VBA)](Modify_Fillet_Weld_Bead_Example_VB.htm)  
[Modify Fillet Weld Bead (VB.NET)](Modify_Fillet_Weld_Bead_Example_VBNET.htm)  
[Modify Fillet Weld Bead (C#)](Modify_Fillet_Weld_Bead_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::IGetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.md)  
[IEdge::GetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.md)  
[IEdge::IGetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.md)

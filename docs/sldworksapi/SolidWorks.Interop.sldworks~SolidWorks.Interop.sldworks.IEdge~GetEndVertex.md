# GetEndVertex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex`

Gets the ending vertex for this edge.
Gets the ending vertex for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEndVertex() As System.Object
```

```

Dim instance As IEdge
Dim value As System.Object
 
value = instance.GetEndVertex()
```

```

System.object GetEndVertex()
```

```

System.Object^ GetEndVertex(); 
```

#### Return Value

Vertex

Remarks

If no vertex exists for this edge (such as the edge of a newly created cylinder), then this method returns NULL.

This method and [IEdge::GetStartVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.md) or [IEdge::IGetStartVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.md) return distinct vertices, unless the edge is closed. Because edges have no natural direction, you cannot necessarily predict which of the two points you will get first and which last.

Use [ICoEdge::GetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md) or [ICoEdge::IGetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md) to get consistent start and end positions.

Example

[Check Interference Using IModeler::CheckInterfence (VBA)](Check_Interference_using_Modeler_CheckInterference_Example_VB.htm)  
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
[IEdge::IGetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.md)  
[IEdge::GetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.md)  
[IEdge::IGetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.md)

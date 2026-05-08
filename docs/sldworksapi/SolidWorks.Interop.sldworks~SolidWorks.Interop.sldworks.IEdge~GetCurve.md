# GetCurve Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve`

Gets the underlying curve for this edge.
Gets the underlying curve for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurve() As System.Object
```

```

Dim instance As IEdge
Dim value As System.Object
 
value = instance.GetCurve()
```

```

System.object GetCurve()
```

```

System.Object^ GetCurve(); 
```

#### Return Value

Pointer to the underlying [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) for this edge

Example

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)  
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)  
[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)  
[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)  
[Get Length of Edge (VBA)](Get_Length_of_Edge_Example_VB.htm)  
[Select Tangent Edges Via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)  
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)  
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)  
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[ICoEdge::GetEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetEdge.md)  
[ICoEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve.md)  
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)

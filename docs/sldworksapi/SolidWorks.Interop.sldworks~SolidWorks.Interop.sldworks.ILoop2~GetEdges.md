# GetEdges Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdges`

Gets all the edges in the loop.
Gets all the edges in the loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdges() As System.Object
```

```

Dim instance As ILoop2
Dim value As System.Object
 
value = instance.GetEdges()
```

```

System.object GetEdges()
```

```

System.Object^ GetEdges(); 
```

#### Return Value

Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) that make up the loop

Remarks

The [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) objects are returned in a clockwise (CW) or counter-clockwise (CCW) manner based on the direction of the [ILoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, use [ILoop2::IsOuter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IsOuter.md).

Because an edge is shared by multiple loops, the edge direction might be opposite to the direction of the ILoop2. To check this, use [IEdge::EdgeInFaceSense](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EdgeInFaceSense.md).

If the loop is a singular loop, use [ILoop2::GetVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetVertices.md) to get its position (a single vertex). ILoop2::GetEdges returns an empty array if the loop is singular.

Example

[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)  
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

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdgeCount.md)  
[ILoop2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetEdges.md)  
[ILoop2::EnumEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumEdges.md)

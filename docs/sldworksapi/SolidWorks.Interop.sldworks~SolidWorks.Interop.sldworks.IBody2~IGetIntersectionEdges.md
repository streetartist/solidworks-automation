# IGetIntersectionEdges Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdges`

Obsolete. Superseded by IBody2::GetIntersectionEdges2.
Obsolete. Superseded by [IBody2::GetIntersectionEdges2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetIntersectionEdges( _
   ByVal ToolBodyIn As Body2 _
) As Edge
```

```

Dim instance As IBody2
Dim ToolBodyIn As Body2
Dim value As Edge
 
value = instance.IGetIntersectionEdges(ToolBodyIn)
```

```

Edge IGetIntersectionEdges( 
   Body2 ToolBodyIn
)
```

```

Edge^ IGetIntersectionEdges( 
   Body2^ ToolBodyIn
) 
```

#### Parameters

*ToolBodyIn*
:   Temporary [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) used to perform the intersection

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method imprints a set of edges on both of these temporary bodies and returns the edges in an unordered list as shown below. The total number of edges in this array is twice the value returned from  
[IBody2::IGetIntersectionEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdgeCount.md).

> **[** *Edge1imprintedOnTarget, Edge1imprintedOnTool, Edge2imprintedOnTarget, Edge2imprintedOnTool* **]**

where the target body is the IBody2 object used to call this method and the tool body is passed into this method as the first argument.

If the two bodies are in an assembly, then IBody2::GetIntersectionEdges generates a list of the intersection edges between the two bodies. To do this, the second body must be transformed in its coordinate space so that it is positioned the same with respect to the first body as it is in assembly space.

To align the two bodies before calling IBody2::GetIntersectionEdges or IBody2::IGetIntersectionEdgeCount, calculate the transformation from the first body to the second body and set this as the transform for the second body using [IBody2::ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md).

In the case of a tangency condition (for example, a planar face contacting the cylindrical face of a cylinder), this method returns a single edge along the tangency.

You might also find that [IBody2::IOperations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md) provides an adequate solution. This method intersects a sheet body with a target body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetIntersectionEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges.md)

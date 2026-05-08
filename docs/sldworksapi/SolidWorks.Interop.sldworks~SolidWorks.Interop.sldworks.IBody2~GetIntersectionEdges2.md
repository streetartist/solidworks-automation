# GetIntersectionEdges2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges2`

Gets the edges resulting from the intersection of the specified tool body and this body.
Gets the edges resulting from the intersection of the specified tool body and this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersectionEdges2( _
   ByVal ToolBodyIn As System.Object, _
   ByVal AddFaceIds As System.Boolean _
) As System.Object
```

```

Dim instance As IBody2
Dim ToolBodyIn As System.Object
Dim AddFaceIds As System.Boolean
Dim value As System.Object
 
value = instance.GetIntersectionEdges2(ToolBodyIn, AddFaceIds)
```

```

System.object GetIntersectionEdges2( 
   System.object ToolBodyIn,
   System.bool AddFaceIds
)
```

```

System.Object^ GetIntersectionEdges2( 
   System.Object^ ToolBodyIn,
   System.bool AddFaceIds
) 
```

#### Parameters

*ToolBodyIn*
:   Temporary tool body used to perform the intersection with this body (see **Remarks**)

*AddFaceIds*
:   True to create IDs for any new faces, false to not (see **Remarks**)

#### Return Value

Array of edges

Remarks

This method imprints a set of edges on both of the bodies and returns the edges in an unordered list as shown below. The total number of edges in the returned array is twice the value returned by [IBody2::IGetIntersectionEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdgeCount.md).

> **[** *Edge1imprintedOnTarget, Edge1imprintedOnTool, Edge2imprintedOnTarget, Edge2imprintedOnTool* **]**

where *Target* is this IBody2 object, and *Tool* is the IBody2 object passed into this method as ToolBodyIn.

If the two bodies are in an assembly, then this method generates a list of the intersection edges between the two bodies. Before calling this method, the two bodies must be aligned. To align the two bodies, calculate the transformation from the first body to the second body and then apply the transform to the second body using [IBody2::ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md).

In the case of a tangency condition (for example, a planar face contacting the cylindrical face of a cylinder), this method returns a single edge along the tangency.

You might also find that [IBody2::Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2.md) provides an adequate solution when intersecting a sheet body with a target body.

AddFaceIds allows you to add IDs to any newly created faces. This may be useful if ToolBodyIn later becomes a permanent body, which can occur in macro features.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

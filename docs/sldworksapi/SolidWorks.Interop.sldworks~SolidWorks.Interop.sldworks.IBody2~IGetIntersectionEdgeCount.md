# IGetIntersectionEdgeCount Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdgeCount`

Gets the number of intersecting edges between this body and the specified tool body.
Gets the number of intersecting edges between this body and the specified tool body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetIntersectionEdgeCount( _
   ByVal ToolBodyIn As Body2 _
) As System.Integer
```

```

Dim instance As IBody2
Dim ToolBodyIn As Body2
Dim value As System.Integer
 
value = instance.IGetIntersectionEdgeCount(ToolBodyIn)
```

```

System.int IGetIntersectionEdgeCount( 
   Body2 ToolBodyIn
)
```

```

System.int IGetIntersectionEdgeCount( 
   Body2^ ToolBodyIn
) 
```

#### Parameters

*ToolBodyIn*
:   Pointer to the temporary body used to perform the intersection

#### Return Value

Number of intersection edges

Remarks

Use the return value from this method to determine the size of the array returned by [IBody2::IGetIntersectionEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdges.md).

If the two bodies are in an assembly, then IBody2::GetIntersectionEdges and IBody2::IGetIntersectionEdges generate a list of the intersection edges between the two bodies. To do this, the second body must be transformed in its coordinate space so that it is positioned the same with respect to the first body as it is in assembly space.

To align the two bodies before calling IBody2::GetIntersectionEdges, IBody2::IGetIntersectionEdges, or Body2::IGetIntersectionEdgeCount, calculate the transformation from the first body to the second body and apply the transform to the second body using [IBody2::ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

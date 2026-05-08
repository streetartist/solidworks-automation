# IGetEdges Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetEdges`

Gets all the edges in the loop.
Gets all the edges in the loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEdges() As Edge
```

```

Dim instance As ILoop2
Dim value As Edge
 
value = instance.IGetEdges()
```

```

Edge IGetEdges()
```

```

Edge^ IGetEdges(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) that make up the loop

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, use [ILoop2::IsOuter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IsOuter.md).

Because an edge is shared by multiple loops, the edge direction might be opposite to the direction of the ILoop2. To check this, use [IEdge::IEdgeInFaceSense2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2.md).

If the loop is a singular loop, use [ILoop2::IGetVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetVertices.md) to get its position (a single vertex). LIoop2::GetEdges returns an empty array if the loop is singular.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdgeCount.md)  
[ILoop2::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdges.md)  
[ILoop2::EnumEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumEdges.md)

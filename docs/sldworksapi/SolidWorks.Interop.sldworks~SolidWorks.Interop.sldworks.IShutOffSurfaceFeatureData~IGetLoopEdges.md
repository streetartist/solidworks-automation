# IGetLoopEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges`

Gets the edges in the specified loop.
Gets the edges in the specified loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLoopEdges( _
   ByVal Index As System.Integer, _
   ByVal Count As System.Integer _
) As Edge
```

```

Dim instance As IShutOffSurfaceFeatureData
Dim Index As System.Integer
Dim Count As System.Integer
Dim value As Edge
 
value = instance.IGetLoopEdges(Index, Count)
```

```

Edge IGetLoopEdges( 
   System.int Index,
   System.int Count
)
```

```

Edge^ IGetLoopEdges( 
   System.int Index,
   System.int Count
) 
```

#### Parameters

*Index*
:   Index of the loop

*Count*
:   Number of edges in the loop specified by index

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IShutOffSurfaceFeatureData::GetLoopEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount.md) before calling this method to get the value of Count.

Use [IShutOffSurfaceFeatureData::Edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Edges.md) or [IShutOffSurfaceFeatureData::ISetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~ISetEdges.md) to set the edges for the loops.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.md)  
[IShutOffSurfaceFeatureData::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetEdgeCount.md)  
[IShutOffSurfaceFeatureData::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopCount.md)  
[IShutOffSurfaceFeatureData::IGetLoopEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.md)  
[IShutOffSurfaceFeatureData::LoopEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.md)  
[IShutOffSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetEdges.md)  
[IShutOffSurfaceFeatureData::LoopPatchType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.md)  
[IShutOffSurfaceFeatureData::SetAllPatchTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.md)

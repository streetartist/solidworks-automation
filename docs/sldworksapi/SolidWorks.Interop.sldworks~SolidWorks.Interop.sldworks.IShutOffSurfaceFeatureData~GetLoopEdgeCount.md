# GetLoopEdgeCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount`

Gets the number of edges in the specified loop.
Gets the number of edges in the specified loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLoopEdgeCount( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IShutOffSurfaceFeatureData
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetLoopEdgeCount(Index)
```

```

System.int GetLoopEdgeCount( 
   System.int Index
)
```

```

System.int GetLoopEdgeCount( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Number indicating the loop for which to get the number of edges

#### Return Value

Number of edges in the loop specified by index

Remarks

Call this method before calling [IShutOffSurfaceFeatureData::IGetLoopsEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.md) to get the size of the array for that method.

Example

See [IShutOffSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.md)  
[IShutOffSurfaceFeatureData::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopCount.md)  
[IShutOffSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetEdges.md)  
[IShutOffSurfaceFeatureData::IGetLoopEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.md)  
[IShutOffSurfaceFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~ISetEdges.md)  
[IShutOffSurfaceFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Edges.md)  
[IShutOffSurfaceFeatureData::LoopEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.md)  
[IShutOffSurfaceFeatureData::LoopPatchType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.md)  
[IShutOffSurfaceFeatureData::SetAllPatchTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.md)

# Edges Property (IShutOffSurfaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Edges`

Gets or sets the edges that form closed loops for the patches.
Gets or sets the edges that form closed loops for the patches.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Edges As System.Object
```

```

Dim instance As IShutOffSurfaceFeatureData
Dim value As System.Object
 
instance.Edges = value
 
value = instance.Edges
```

```

System.object Edges {get; set;}
```

```

property System.Object^ Edges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See [IShutOffSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.md)  
[IShutOffSurfaceFeatureData::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetEdgeCount.md)  
[IShutOffSurfaceFeatureData::GetLoopEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount.md)  
[IShutOffSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetEdges.md)  
[IShutOffSurfaceFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~ISetEdges.md)  
[IShutOffSurfaceFeatureData::LoopEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.md)

# SetEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetEdges`

Sets the edge to use as the base for this ruled-surface feature.
Sets the edge to use as the base for this ruled-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEdges( _
   ByVal Edges As System.Object, _
   ByVal SideFlags As System.Object _
) 
```

```

Dim instance As IRuledSurfaceFeatureData
Dim Edges As System.Object
Dim SideFlags As System.Object
 
instance.SetEdges(Edges, SideFlags)
```

```

void SetEdges( 
   System.object Edges,
   System.object SideFlags
)
```

```

void SetEdges( 
   System.Object^ Edges,
   System.Object^ SideFlags
) 
```

#### Parameters

*Edges*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*SideFlags*
:   Array of flags indicating which side of each edge to create the ruled-surface feature

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.md)  
[IRuledSurfaceFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~ISetEdges.md)  
[IRuledSurfaceFeatureData::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdges.md)  
[IRuledSurfaceFeatureData::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdgesCount.md)  
[IRuledSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~IGetEdges.md)

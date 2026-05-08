# ISetEdges Method (IRuledSurfaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~ISetEdges`

Sets the edge to use as the base for this ruled-surface feature.
Sets the edge to use as the base for this ruled-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetEdges( _
   ByVal Count As System.Integer, _
   ByRef Entities As System.Object, _
   ByRef SideFlags As System.Integer _
) 
```

```

Dim instance As IRuledSurfaceFeatureData
Dim Count As System.Integer
Dim Entities As System.Object
Dim SideFlags As System.Integer
 
instance.ISetEdges(Count, Entities, SideFlags)
```

```

void ISetEdges( 
   System.int Count,
   ref System.object Entities,
   ref System.int SideFlags
)
```

```

void ISetEdges( 
   System.int Count,
   System.Object^% Entities,
   System.int% SideFlags
) 
```

#### Parameters

*Count*
:   Number of edges

*Entities*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*SideFlags*
:   - in-process, unmanaged C++: Pointer to an array of flags indicating which side of each edge to create the ruled-surface feature

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.md)  
[IRuledSurfaceFeatureData::SetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetEdges.md)  
[IRuledSurfaceFeatureData::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdges.md)  
[IRuledSurfaceFeatureData::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdgesCount.md)  
[IRuledSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~IGetEdges.md)

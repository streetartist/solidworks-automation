# ISetPropagatingEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~ISetPropagatingEdges`

Sets the propagating edges for this surface-extend feature.
Sets the propagating edges for this surface-extend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPropagatingEdges( _
   ByVal Count As System.Integer, _
   ByRef EdgeArr As Edge _
) 
```

```

Dim instance As ISurfaceExtendFeatureData
Dim Count As System.Integer
Dim EdgeArr As Edge
 
instance.ISetPropagatingEdges(Count, EdgeArr)
```

```

void ISetPropagatingEdges( 
   System.int Count,
   ref Edge EdgeArr
)
```

```

void ISetPropagatingEdges( 
   System.int Count,
   Edge^% EdgeArr
) 
```

#### Parameters

*Count*
:   Number of propagating edges

*EdgeArr*
:   - in-process, unmanaged C++: Pointer to an array extended items ([faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) and [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)) of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.md)  
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.md)  
[ISurfaceExtendFeatureData::GetPropagatingEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~GetPropagatingEdgesCount.md)  
[ISurfaceExtendFeatureData::IGetPropagatingEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IGetPropagatingEdges.md)  
[ISurfaceExtendFeatureData::PropagatingEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~PropagatingEdges.md)

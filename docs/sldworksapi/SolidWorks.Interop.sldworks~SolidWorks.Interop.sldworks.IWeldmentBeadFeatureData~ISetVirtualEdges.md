# ISetVirtualEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges`

Sets the edges to which to apply this weld bead.
Sets the edges to which to apply this weld bead.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetVirtualEdges( _
   ByVal Side As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef EdgesIn As Edge _
) 
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim Count As System.Integer
Dim EdgesIn As Edge
 
instance.ISetVirtualEdges(Side, Count, EdgesIn)
```

```

void ISetVirtualEdges( 
   System.int Side,
   System.int Count,
   ref Edge EdgesIn
)
```

```

void ISetVirtualEdges( 
   System.int Side,
   System.int Count,
   Edge^% EdgesIn
) 
```

#### Parameters

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*Count*
:   Number of edges to which to apply this weld bead

*EdgesIn*
:   - in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to which to apply this weld bead

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

After using [IWeldmentBeadFeatureData::ISetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.md), use [IWeldmentBeadFeatureData::IGetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.md) to get the new intersections. Then use IWeldmentBeadFeatureData::ISetVirtualEdges to specify the edges to which you want the weld bead  applied. By default, IWeldmentBeadFeatureData::ISetFaces creates the bead on all virtual edges. IWeldmentBeadFeatureData::ISetVirtualEdges lets you exclude any of these edges.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::SetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.md)  
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md)  
[IWeldmentBeadFeatureData::IGetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.md)

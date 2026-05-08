# IGetVirtualEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges`

Gets the edges to which the weld bead is applied.
Gets the edges to which the weld bead is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVirtualEdges( _
   ByVal FromFeature As System.Boolean, _
   ByVal Side As System.Integer, _
   ByVal Count As System.Integer _
) As Edge
```

```

Dim instance As IWeldmentBeadFeatureData
Dim FromFeature As System.Boolean
Dim Side As System.Integer
Dim Count As System.Integer
Dim value As Edge
 
value = instance.IGetVirtualEdges(FromFeature, Side, Count)
```

```

Edge IGetVirtualEdges( 
   System.bool FromFeature,
   System.int Side,
   System.int Count
)
```

```

Edge^ IGetVirtualEdges( 
   System.bool FromFeature,
   System.int Side,
   System.int Count
) 
```

#### Parameters

*FromFeature*
:   True gets the virtual edges used by the feature, false gets all of the virtual edges

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*Count*
:   Number of edges to which weld bead applied

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Do not perform any operations on the returned edges as they are only temporary to help you decide which edges to keep for this weld bead.

Call [IWeldmentBeadFeatureData::GetVirutalEdgesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.md) to get the number of edges.

After using [IWeldmentBeadFeatureData::ISetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.md), use IWeldmentBeadFeatureData::IGetVirtualEdges to get the new intersections. Then use [IWeldmentBeadFeatureData::ISetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.md) to specify the edges to which you want the weld bead applied. By default, IWeldmentBeadFeatureData::ISetFaces creates the bead on all virtual edges; IWeldmentBeadFeatureData::ISetVirtualEdges lets you exclude any of these edges.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::GetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.md)  
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md)  
[IWeldmentBeadFeatureData::SetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.md)

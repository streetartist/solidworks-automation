# SetVirtualEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges`

Sets the edges to which to apply this weld bead.
Sets the edges to which to apply this weld bead.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVirtualEdges( _
   ByVal Side As System.Integer, _
   ByVal EdgesIn As System.Object _
) 
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim EdgesIn As System.Object
 
instance.SetVirtualEdges(Side, EdgesIn)
```

```

void SetVirtualEdges( 
   System.int Side,
   System.object EdgesIn
)
```

```

void SetVirtualEdges( 
   System.int Side,
   System.Object^ EdgesIn
) 
```

#### Parameters

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*EdgesIn*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to which to apply this weld bead

Remarks

After using [IWeldmentBeadFeatureData::SetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md), use [IWeldmentBeadFeatureData::GetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.md) to get the new intersections. Then use IWeldmentBeadFeatureData::SetVirtualEdges to specify the edges to which you want the weld bead  applied. By default, IWeldmentBeadFeatureData::SetFaces creates the bead on all virtual edges. IWeldmentBeadFeatureData::SetVirtualEdges lets you exclude any of these edges.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::ISetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.md)  
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.md)  
[IWeldmentBeadFeatureData::IGetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.md)  
[IWeldmentBeadFeatureData::GetVirtualEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.md)  
[IWeldmentBeadFeatureData::GetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.md)

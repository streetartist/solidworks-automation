# GetVirtualEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges`

Gets the edges to which the weld bead is applied.
Gets the edges to which the weld bead is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVirtualEdges( _
   ByVal FromFeature As System.Boolean, _
   ByVal Side As System.Integer _
) As System.Object
```

```

Dim instance As IWeldmentBeadFeatureData
Dim FromFeature As System.Boolean
Dim Side As System.Integer
Dim value As System.Object
 
value = instance.GetVirtualEdges(FromFeature, Side)
```

```

System.object GetVirtualEdges( 
   System.bool FromFeature,
   System.int Side
)
```

```

System.Object^ GetVirtualEdges( 
   System.bool FromFeature,
   System.int Side
) 
```

#### Parameters

*FromFeature*
:   True gets the virtual edges used by the feature, false gets all of the virtual edges

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

#### Return Value

Array of the [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

Do not perform any operations on the returned edges as they are only temporary to help you decide which edges to keep for this weld bead.

After using [IWeldmentBeadFeatureData::SetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md), use IWeldmentBeadFeatureData::GetVirtualEdges to get the new intersections. Then use [IWeldmentBeadFeatureData::SetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.md) to specify the edges to which you want the weld bead applied. By default, IWeldmentBeadFeatureData::SetFaces creates the bead on all virtual edges; IWeldmentBeadFeatureData::SetVirtualEdges lets you exclude any of these edges.

Example

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::GetVirtualEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.md)  
[IWeldmentBeadFeatureData::IGetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.md)  
[IWeldmentBeadFeatureData::ISetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.md)  
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.md)

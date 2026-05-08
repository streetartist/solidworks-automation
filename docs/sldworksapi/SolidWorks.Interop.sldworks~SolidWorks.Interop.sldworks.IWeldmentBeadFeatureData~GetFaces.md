# GetFaces Method (IWeldmentBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces`

Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied.
Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetFaces( _
   ByVal Side As System.Integer, _
   ByRef FaceSet1 As System.Object, _
   ByRef FaceSet2 As System.Object _
) 
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim FaceSet1 As System.Object
Dim FaceSet2 As System.Object
 
instance.GetFaces(Side, FaceSet1, FaceSet2)
```

```

void GetFaces( 
   System.int Side,
   out System.object FaceSet1,
   out System.object FaceSet2
)
```

```

void GetFaces( 
   System.int Side,
   [Out] System.Object^ FaceSet1,
   [Out] System.Object^ FaceSet2
) 
```

#### Parameters

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*FaceSet1*
:   First set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*FaceSet2*
:   Second set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

After using this method, use [IWeldmentBeadFeatureData::GetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.md) to get the new intersections. Then use [IWeldmentBeadFeatureData::SetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.md) to specify the edges to which you want the weld bead applied. By default, [IWeldmentBeadFeatureData::SetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md) creates the bead on all virtual edges. [IWeldmentBeadFeatureData::SetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.md) lets  
you exclude any of these edges.

Example

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.md)  
[IWeldmentBeadFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.md)  
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md)  
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.md)

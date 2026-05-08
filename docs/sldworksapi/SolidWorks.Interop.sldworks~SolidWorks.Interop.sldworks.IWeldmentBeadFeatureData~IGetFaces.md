# IGetFaces Method (IWeldmentBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces`

Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied.
Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetFaces( _
   ByVal Side As System.Integer, _
   ByVal Count1 As System.Integer, _
   ByRef FaceSet1 As Face2, _
   ByVal Count2 As System.Integer, _
   ByRef FaceSet2 As Face2 _
) 
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim Count1 As System.Integer
Dim FaceSet1 As Face2
Dim Count2 As System.Integer
Dim FaceSet2 As Face2
 
instance.IGetFaces(Side, Count1, FaceSet1, Count2, FaceSet2)
```

```

void IGetFaces( 
   System.int Side,
   System.int Count1,
   out Face2 FaceSet1,
   System.int Count2,
   out Face2 FaceSet2
)
```

```

void IGetFaces( 
   System.int Side,
   System.int Count1,
   [Out] Face2^ FaceSet1,
   System.int Count2,
   [Out] Face2^ FaceSet2
) 
```

#### Parameters

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*Count1*
:   Number of faces in first set of faces

*FaceSet1*
:   - in-process, unmanaged C++: Pointer to an array of the first set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Count2*
:   Number of faces in second set of faces

*FaceSet2*
:   - in-process, unmanaged C++: Pointer to an array of the second set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

Remarks

Before calling this method, call [IWeldmentBeadFeatureData::GetFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.md).

After using this method, use [IWeldmentBeadFeatureData::IGetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.md) to get the new intersections. Then use [IWeldmentBeadFeatureData::ISetVirtualEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.md) to specify the edges to which you want the weld bead applied. By default, WeldmentBeadFeatureData::SetFaces creates the bead on all virtual edges. IWeldmentBeadFeatureData::ISetVirtualEdges lets you exclude any of these edges.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.md)  
[IWeldmentBeadFeatureData::GetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.md)  
[IWeldmentBeadFeatureData::GetVirtualEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.md)  
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md)  
[IWeldmentBeadFeatureData::SetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.md)

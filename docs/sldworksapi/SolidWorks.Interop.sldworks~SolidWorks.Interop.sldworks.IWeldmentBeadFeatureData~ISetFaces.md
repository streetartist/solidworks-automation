# ISetFaces Method (IWeldmentBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces`

Sets the faces to which to apply the weld bead.
Sets the faces to which to apply the weld bead.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetFaces( _
   ByVal Side As System.Integer, _
   ByVal Count1 As System.Integer, _
   ByRef FaceSet1 As Face2, _
   ByVal Count2 As System.Integer, _
   ByRef FaceSet2 As Face2 _
) As System.Boolean
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim Count1 As System.Integer
Dim FaceSet1 As Face2
Dim Count2 As System.Integer
Dim FaceSet2 As Face2
Dim value As System.Boolean
 
value = instance.ISetFaces(Side, Count1, FaceSet1, Count2, FaceSet2)
```

```

System.bool ISetFaces( 
   System.int Side,
   System.int Count1,
   ref Face2 FaceSet1,
   System.int Count2,
   ref Face2 FaceSet2
)
```

```

System.bool ISetFaces( 
   System.int Side,
   System.int Count1,
   Face2^% FaceSet1,
   System.int Count2,
   Face2^% FaceSet2
) 
```

#### Parameters

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*Count1*
:   Number of faces in the first set of faces

*FaceSet1*
:   - in-process, unmanaged C++: Pointer to an array of the first set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Count2*
:   Number of faces in the second set of faces

*FaceSet2*
:   - in-process, unmanaged C++: Pointer to an array of the second set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

#### Return Value

True if the weld bead is applied to the specified faces, false if not

Remarks

Although you must select planar faces for the face sets, fillet weld beads can follow non-planar, tangent contours when you set [IWeldmentBeadFeatureData::TangentPropagation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~TangentPropagation.md) to TRUE.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md)  
[IWeldmentBeadFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.md)  
[IWeldmentBeadFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.md)  
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.md)

# SetFaces Method (IWeldmentBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces`

Sets the faces to which to apply the weld bead.
Sets the faces to which to apply the weld bead.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFaces( _
   ByVal Side As System.Integer, _
   ByVal FaceSet1 As System.Object, _
   ByVal FaceSet2 As System.Object _
) As System.Boolean
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim FaceSet1 As System.Object
Dim FaceSet2 As System.Object
Dim value As System.Boolean
 
value = instance.SetFaces(Side, FaceSet1, FaceSet2)
```

```

System.bool SetFaces( 
   System.int Side,
   System.object FaceSet1,
   System.object FaceSet2
)
```

```

System.bool SetFaces( 
   System.int Side,
   System.Object^ FaceSet1,
   System.Object^ FaceSet2
) 
```

#### Parameters

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*FaceSet1*
:   First set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to which to apply the weld bead

*FaceSet2*
:   Second set of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to which to apply the weld bead

#### Return Value

True if the weld bead is applied to the specified faces, false if not

Remarks

Although you must select planar faces for the face sets, fillet weld beads can follow non-planar, tangent contours when you set [IWeldmentBeadFeatureData::TangentPropagation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~TangentPropagation.md) to TRUE.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Change Weld Bead Faces (VBA)](Change_Weld_Bead_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.md)  
[IWeldmentBeadFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.md)  
[IWeldmentBeadFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.md)  
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.md)

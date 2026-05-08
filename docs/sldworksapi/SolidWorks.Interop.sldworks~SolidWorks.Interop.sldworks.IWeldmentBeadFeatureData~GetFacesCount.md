# GetFacesCount Method (IWeldmentBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount`

Gets the number of faces in each sets of faces whose intersection defines the edges to which this weld bead is applied.
Gets the number of faces in each sets of faces whose intersection defines the edges to which this weld bead is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetFacesCount( _
   ByVal Side As System.Integer, _
   ByRef FaceSet1Count As System.Integer, _
   ByRef FaceSet2Count As System.Integer _
) 
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim FaceSet1Count As System.Integer
Dim FaceSet2Count As System.Integer
 
instance.GetFacesCount(Side, FaceSet1Count, FaceSet2Count)
```

```

void GetFacesCount( 
   System.int Side,
   out System.int FaceSet1Count,
   out System.int FaceSet2Count
)
```

```

void GetFacesCount( 
   System.int Side,
   [Out] System.int FaceSet1Count,
   [Out] System.int FaceSet2Count
) 
```

#### Parameters

*Side*
:   Side as defined in [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

*FaceSet1Count*
:   Number of faces in first set of faces

*FaceSet2Count*
:   Number of faces in second set of faces

Remarks

Call this method before calling [IWeldmentBeadFeatureData::IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.md)  
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.md)  
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.md)

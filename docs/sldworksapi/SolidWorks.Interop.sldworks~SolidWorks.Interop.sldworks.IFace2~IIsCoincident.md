# IIsCoincident Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IIsCoincident`

Gets whether this face and the specified face, which is located on a different body, are coincident.
Gets whether this face and the specified face, which is located on a different body, are coincident.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IIsCoincident( _
   ByVal FaceIn As Face2, _
   ByVal Tolerance As System.Double _
) As System.Integer
```

```

Dim instance As IFace2
Dim FaceIn As Face2
Dim Tolerance As System.Double
Dim value As System.Integer
 
value = instance.IIsCoincident(FaceIn, Tolerance)
```

```

System.int IIsCoincident( 
   Face2 FaceIn,
   System.double Tolerance
)
```

```

System.int IIsCoincident( 
   Face2^ FaceIn,
   System.double Tolerance
) 
```

#### Parameters

*FaceIn*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) located on a different body

*Tolerance*
:   Tolerance

#### Return Value

Result as defined in [swFaceCoincidentResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceCoincidentResult_e.html) (see Remarks)

Remarks

For two faces to be considered coincident, they must have similar corresponding loops and all points on one face must be within the specified tolerance of the other face, and vice versa.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IsCoincident Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IsCoincident.md)

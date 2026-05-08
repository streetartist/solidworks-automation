# MatchedBoolean4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean4`

Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly.
Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MatchedBoolean4( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByVal FaceList1 As System.Object, _
   ByVal FaceList2 As System.Object, _
   ByVal MatchingTolerance As System.Double, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As System.Object
Dim FaceList2 As System.Object
Dim MatchingTolerance As System.Double
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.MatchedBoolean4(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, MatchingTolerance, ErrorCode)
```

```

System.object MatchedBoolean4( 
   System.int OperationType,
   System.object ToolBody,
   System.int NumOfMatchingFaces,
   System.object FaceList1,
   System.object FaceList2,
   System.double MatchingTolerance,
   out System.int ErrorCode
)
```

```

System.Object^ MatchedBoolean4( 
   System.int OperationType,
   System.Object^ ToolBody,
   System.int NumOfMatchingFaces,
   System.Object^ FaceList1,
   System.Object^ FaceList2,
   System.double MatchingTolerance,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*OperationType*
:   One of the following operation types:

    - SWBODYADD
    - SWBODYCUT
    - SWBODYINTERSECT

*ToolBody*
:   Array of bodies

*NumOfMatchingFaces*
:   Number of matching faces

*FaceList1*
:   First face list (see Remarks)

*FaceList2*
:   Number of matching faces

*MatchingTolerance*
:   Tolerance to use to check matching faces

*ErrorCode*
:   Error indicated as defined in [swBodyOperationError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyOperationError_e.html)

Remarks

The concept of match means that the caller tells the boolean operator beforehand which faces can be considered to coincide. Basically the caller performs part of the boolean operation.

Sometimes the application knows that two faces match because of the way the bodies are constructed; i.e., the application knows which faces are intended to match.

Having a list of matching face pairs may allow the matched boolean operator to resolve other geometric operations that otherwise it would not be able to work out. In general, providing matched faces speeds up the boolean operation and makes results more reliable.

The arguments FaceList1 and FaceList2 arguments can be empty lists. If matching face pairs are passed in, these faces must match such that:

- the surface geometry is coinciding.
- for each edge in a face, there is an edge in the other face that coincides.

If MatchingTolerance is less than 1.0e-8 or 0.0, then a default tolerance of 2.0e-6 is used. You decide the tolerance value based on the similarities and subtle differences between the two bodies.

This method supports multibody parts.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IMatchedBoolean4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean4.md)

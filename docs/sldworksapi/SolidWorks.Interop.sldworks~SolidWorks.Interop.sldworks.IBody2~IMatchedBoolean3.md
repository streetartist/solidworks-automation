# IMatchedBoolean3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean3`

Obsolete. Superseded by IBody2::IMatchedBoolean4.
Obsolete. Superseded by [IBody2::IMatchedBoolean4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMatchedBoolean3( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBodyCount As System.Integer, _
   ByRef ToolBodyArr As Body2, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByRef FaceList1 As Face2, _
   ByRef FaceList2 As Face2, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies2
```

```

Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBodyCount As System.Integer
Dim ToolBodyArr As Body2
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As Face2
Dim FaceList2 As Face2
Dim ErrorCode As System.Integer
Dim value As EnumBodies2
 
value = instance.IMatchedBoolean3(OperationType, ToolBodyCount, ToolBodyArr, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

```

EnumBodies2 IMatchedBoolean3( 
   System.int OperationType,
   System.int ToolBodyCount,
   ref Body2 ToolBodyArr,
   System.int NumOfMatchingFaces,
   ref Face2 FaceList1,
   ref Face2 FaceList2,
   out System.int ErrorCode
)
```

```

EnumBodies2^ IMatchedBoolean3( 
   System.int OperationType,
   System.int ToolBodyCount,
   Body2^% ToolBodyArr,
   System.int NumOfMatchingFaces,
   Face2^% FaceList1,
   Face2^% FaceList2,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*OperationType*
:   One of these operation types:

    - SWBODYADD
    - SWBODYCUT
    - SWCODYINTERSECT

*ToolBodyCount*
:   Number of bodies

*ToolBodyArr*
:   Array of bodies of size ToolBodyCount

*NumOfMatchingFaces*
:   Number of matching faces

*FaceList1*
:   First face list (see **Remarks**)

*FaceList2*
:   Second face list  (see Remarks)

*ErrorCode*
:   Error indicated as defined in[swBodyOperationError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyOperationError_e.html)

#### Return Value

Pointer to the [IEnumBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md) object for a list of matches

Remarks

The concept of match means that the caller tells the boolean operator beforehand which faces can be considered to coincide. Basically, the caller performs part of the boolean operation.

Sometimes the application knows that two faces match because of the way the bodies are constructed; i.e., the application knows which faces are intended to match.

Having a list of matching face pairs may allow the matched boolean operator to resolve other geometric operations that otherwise it would not be able to work out. In general, providing matched faces speeds up the boolean operation and makes results more reliable.

The arguments FaceList1 and FaceList2 arguments can be empty lists. If matching face pairs are passed in, these faces must match such that:

- the surface geometry is coinciding.
- for each edge in a face, there is an edge in the other face that coincides

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::MatchedBoolean3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean3.md)

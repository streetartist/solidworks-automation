# MatchedBoolean Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~MatchedBoolean`

Obsolete. Superseded by IBody2::MatchedBoolean3.
Obsolete. Superseded by [IBody2::MatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MatchedBoolean( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByVal FaceList1 As System.Object, _
   ByVal FaceList2 As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As System.Object
Dim FaceList2 As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.MatchedBoolean(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

```

System.object MatchedBoolean( 
   System.int OperationType,
   System.object ToolBody,
   System.int NumOfMatchingFaces,
   System.object FaceList1,
   System.object FaceList2,
   out System.int ErrorCode
)
```

```

System.Object^ MatchedBoolean( 
   System.int OperationType,
   System.Object^ ToolBody,
   System.int NumOfMatchingFaces,
   System.Object^ FaceList1,
   System.Object^ FaceList2,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*OperationType*

*ToolBody*

*NumOfMatchingFaces*

*FaceList1*

*FaceList2*

*ErrorCode*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)

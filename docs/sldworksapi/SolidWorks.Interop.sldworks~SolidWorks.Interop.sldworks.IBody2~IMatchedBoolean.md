# IMatchedBoolean Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean`

Obsolete. Superseded by IBody2::IMatchedBoolean3.
Obsolete. Superseded by [IBody2::IMatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMatchedBoolean( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body2, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByRef FaceList1 As Face2, _
   ByRef FaceList2 As Face2, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies2
```

```

Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As Body2
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As Face2
Dim FaceList2 As Face2
Dim ErrorCode As System.Integer
Dim value As EnumBodies2
 
value = instance.IMatchedBoolean(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

```

EnumBodies2 IMatchedBoolean( 
   System.int OperationType,
   Body2 ToolBody,
   System.int NumOfMatchingFaces,
   ref Face2 FaceList1,
   ref Face2 FaceList2,
   out System.int ErrorCode
)
```

```

EnumBodies2^ IMatchedBoolean( 
   System.int OperationType,
   Body2^ ToolBody,
   System.int NumOfMatchingFaces,
   Face2^% FaceList1,
   Face2^% FaceList2,
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

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

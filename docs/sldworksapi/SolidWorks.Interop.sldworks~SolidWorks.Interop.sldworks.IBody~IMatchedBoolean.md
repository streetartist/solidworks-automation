# IMatchedBoolean Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IMatchedBoolean`

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
   ByVal ToolBody As Body, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByRef FaceList1 As Face, _
   ByRef FaceList2 As Face, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies
```

```

Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As Body
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As Face
Dim FaceList2 As Face
Dim ErrorCode As System.Integer
Dim value As EnumBodies
 
value = instance.IMatchedBoolean(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

```

EnumBodies IMatchedBoolean( 
   System.int OperationType,
   Body ToolBody,
   System.int NumOfMatchingFaces,
   ref Face FaceList1,
   ref Face FaceList2,
   out System.int ErrorCode
)
```

```

EnumBodies^ IMatchedBoolean( 
   System.int OperationType,
   Body^ ToolBody,
   System.int NumOfMatchingFaces,
   Face^% FaceList1,
   Face^% FaceList2,
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

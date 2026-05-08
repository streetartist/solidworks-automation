# IOperations2 Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IOperations2`

Obsolete. Superseded by IBody2::IOperations2.
Obsolete. Superseded by [IBody2::IOperations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IOperations2( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies
```

```

Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As Body
Dim ErrorCode As System.Integer
Dim value As EnumBodies
 
value = instance.IOperations2(OperationType, ToolBody, ErrorCode)
```

```

EnumBodies IOperations2( 
   System.int OperationType,
   Body ToolBody,
   out System.int ErrorCode
)
```

```

EnumBodies^ IOperations2( 
   System.int OperationType,
   Body^ ToolBody,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*OperationType*

*ToolBody*

*ErrorCode*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)

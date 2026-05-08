# Operations2 Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~Operations2`

Obsolete. Superseded by IBody2::Operations2.
Obsolete. Superseded by [IBody2::Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Operations2( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.Operations2(OperationType, ToolBody, ErrorCode)
```

```

System.object Operations2( 
   System.int OperationType,
   System.object ToolBody,
   out System.int ErrorCode
)
```

```

System.Object^ Operations2( 
   System.int OperationType,
   System.Object^ ToolBody,
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

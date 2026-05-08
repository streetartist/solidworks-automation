# IOperations Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IOperations`

Obsolete. Superseded by IBody2::IOperations2.
Obsolete. Superseded by [IBody2::IOperations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IOperations( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body, _
   ByVal NumMaxSections As System.Integer, _
   ByRef ResultingBodies As Body _
) As System.Integer
```

```

Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As Body
Dim NumMaxSections As System.Integer
Dim ResultingBodies As Body
Dim value As System.Integer
 
value = instance.IOperations(OperationType, ToolBody, NumMaxSections, ResultingBodies)
```

```

System.int IOperations( 
   System.int OperationType,
   Body ToolBody,
   System.int NumMaxSections,
   ref Body ResultingBodies
)
```

```

System.int IOperations( 
   System.int OperationType,
   Body^ ToolBody,
   System.int NumMaxSections,
   Body^% ResultingBodies
) 
```

#### Parameters

*OperationType*

*ToolBody*

*NumMaxSections*

*ResultingBodies*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)

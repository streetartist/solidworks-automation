# IOperations Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations`

Obsolete. Superseded by IBody2::Operations2.
Obsolete. Superseded by [IBody2::Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IOperations( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body2, _
   ByVal NumMaxSections As System.Integer, _
   ByRef ResultingBodies As Body2 _
) As System.Integer
```

```

Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As Body2
Dim NumMaxSections As System.Integer
Dim ResultingBodies As Body2
Dim value As System.Integer
 
value = instance.IOperations(OperationType, ToolBody, NumMaxSections, ResultingBodies)
```

```

System.int IOperations( 
   System.int OperationType,
   Body2 ToolBody,
   System.int NumMaxSections,
   ref Body2 ResultingBodies
)
```

```

System.int IOperations( 
   System.int OperationType,
   Body2^ ToolBody,
   System.int NumMaxSections,
   Body2^% ResultingBodies
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

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

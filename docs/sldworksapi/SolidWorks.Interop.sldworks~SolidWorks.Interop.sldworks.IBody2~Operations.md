# Operations Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations`

Obsolete. Superseded by IBody2::Operations2.
Obsolete. Superseded by [IBody2::Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Operations( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByVal NumMaxSections As System.Integer _
) As System.Object
```

```

Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim NumMaxSections As System.Integer
Dim value As System.Object
 
value = instance.Operations(OperationType, ToolBody, NumMaxSections)
```

```

System.object Operations( 
   System.int OperationType,
   System.object ToolBody,
   System.int NumMaxSections
)
```

```

System.Object^ Operations( 
   System.int OperationType,
   System.Object^ ToolBody,
   System.int NumMaxSections
) 
```

#### Parameters

*OperationType*

*ToolBody*

*NumMaxSections*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

# IsSafe Property (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSafe`

Not implemented.
Not implemented.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsSafe As System.Boolean
```

```

Dim instance As IBody2
Dim value As System.Boolean
 
value = instance.IsSafe
```

```

System.bool IsSafe {get;}
```

```

property System.bool IsSafe {
   System.bool get();
}
```

#### Property Value

True if the IBody2 object survived the rebuild, false if not

**NOTE:** This property is not implemented; thus, it will always return false.

Remarks

This property is read-only and does not persist from session to session.

To make a body safe, use [IBody2::GetSafeBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSafeBody.md) .

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

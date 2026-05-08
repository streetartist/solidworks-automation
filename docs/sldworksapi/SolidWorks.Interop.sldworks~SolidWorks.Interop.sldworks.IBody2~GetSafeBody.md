# GetSafeBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSafeBody`

Not implemented.
Not implemented.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSafeBody() As Body2
```

```

Dim instance As IBody2
Dim value As Body2
 
value = instance.GetSafeBody()
```

```

Body2 GetSafeBody()
```

```

Body2^ GetSafeBody(); 
```

#### Return Value

Pointer to the [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object

**NOTE:** This method is not yet implemented; thus, it will currently always return NULL.

Remarks

To determine if a body is safe, use the [IBody2::IsSafe](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSafe.md) property. This property is read-only and does not persist from session to session.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

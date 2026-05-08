# ResetEdgeTolerances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetEdgeTolerances`

Resets the tolerance on all edges of this body.
Resets the tolerance on all edges of this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ResetEdgeTolerances() 
```

```

Dim instance As IBody2
 
instance.ResetEdgeTolerances()
```

```

void ResetEdgeTolerances()
```

```

void ResetEdgeTolerances(); 
```

Remarks

Use this method if [IBody2::Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2.md) or [IBody2::IOperations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md) returns a non-manifold error. Then use IBody2::Operations2 or IBody2::IOperations2 again after using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)

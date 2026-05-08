# SetTransformAndSolve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve`

Obsolete. Superseded by IComponent2::SetTransformAndSolve2.
Obsolete. Superseded by [IComponent2::SetTransformAndSolve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTransformAndSolve( _
   ByVal XformIn As MathTransform _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim XformIn As MathTransform
Dim value As System.Boolean
 
value = instance.SetTransformAndSolve(XformIn)
```

```

System.bool SetTransformAndSolve( 
   MathTransform XformIn
)
```

```

System.bool SetTransformAndSolve( 
   MathTransform^ XformIn
) 
```

#### Parameters

*XformIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)

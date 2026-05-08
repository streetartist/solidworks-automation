# ISetXformAndSolve Method (IComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~ISetXformAndSolve`

Obsolete. Superseded by IComponent2::SetTransformAndSolve2,
Obsolete. Superseded by [IComponent2::SetTransformAndSolve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.md),

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetXformAndSolve( _
   ByRef XformIn As System.Double _
) As System.Boolean
```

```

Dim instance As IComponent
Dim XformIn As System.Double
Dim value As System.Boolean
 
value = instance.ISetXformAndSolve(XformIn)
```

```

System.bool ISetXformAndSolve( 
   ref System.double XformIn
)
```

```

System.bool ISetXformAndSolve( 
   System.double% XformIn
) 
```

#### Parameters

*XformIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.md)  
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.md)

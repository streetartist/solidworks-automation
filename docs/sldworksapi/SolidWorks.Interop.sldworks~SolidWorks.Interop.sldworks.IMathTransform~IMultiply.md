# IMultiply Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IMultiply`

Multiplies two matrices together.
Multiplies two matrices together.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMultiply( _
   ByVal TransformObjIn As MathTransform _
) As MathTransform
```

```

Dim instance As IMathTransform
Dim TransformObjIn As MathTransform
Dim value As MathTransform
 
value = instance.IMultiply(TransformObjIn)
```

```

MathTransform IMultiply( 
   MathTransform TransformObjIn
)
```

```

MathTransform^ IMultiply( 
   MathTransform^ TransformObjIn
) 
```

#### Parameters

*TransformObjIn*
:   [Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) by which to multiply the calling math transform

#### Return Value

Newly created [math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) object or null if the operation fails

Remarks

The resulting transform is the result of transforming math transform with respect to the transformObjIn coordinate frame.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[Multiply Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~Multiply.md)

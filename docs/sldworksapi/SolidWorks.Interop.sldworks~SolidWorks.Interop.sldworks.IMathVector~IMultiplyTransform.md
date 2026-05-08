# IMultiplyTransform Method (IMathVector)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IMultiplyTransform`

Multiplies this math vector by the specified math transform.
Multiplies this math vector by the specified math transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMultiplyTransform( _
   ByVal TransformObjIn As MathTransform _
) As MathVector
```

```

Dim instance As IMathVector
Dim TransformObjIn As MathTransform
Dim value As MathVector
 
value = instance.IMultiplyTransform(TransformObjIn)
```

```

MathVector IMultiplyTransform( 
   MathTransform TransformObjIn
)
```

```

MathVector^ IMultiplyTransform( 
   MathTransform^ TransformObjIn
) 
```

#### Parameters

*TransformObjIn*
:   [Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) by which to multiply the math vector

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) or NULL if the operation fails

Remarks

The matrix is rotated and then scaled. It is not transformed because the math vector is assumed to be positionless.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::MultiplyTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~MultiplyTransform.md)

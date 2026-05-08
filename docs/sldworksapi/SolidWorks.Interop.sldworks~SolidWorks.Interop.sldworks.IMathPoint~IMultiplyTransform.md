# IMultiplyTransform Method (IMathPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IMultiplyTransform`

Multiplies a math point with a math transform; the point is rotated, scaled, and then translated.
Multiplies a math point with a math transform; the point is rotated, scaled, and then translated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMultiplyTransform( _
   ByVal TransformObjIn As MathTransform _
) As MathPoint
```

```

Dim instance As IMathPoint
Dim TransformObjIn As MathTransform
Dim value As MathPoint
 
value = instance.IMultiplyTransform(TransformObjIn)
```

```

MathPoint IMultiplyTransform( 
   MathTransform TransformObjIn
)
```

```

MathPoint^ IMultiplyTransform( 
   MathTransform^ TransformObjIn
) 
```

#### Parameters

*TransformObjIn*
:   [Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) by which to multiply this math point

#### Return Value

Newly created translated [math point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) or null if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::MultiplyTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~MultiplyTransform.md)

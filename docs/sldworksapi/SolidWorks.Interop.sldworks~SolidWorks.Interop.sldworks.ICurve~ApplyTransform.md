# ApplyTransform Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ApplyTransform`

Applies the transform to a curve.
Applies the transform to a curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ApplyTransform( _
   ByVal Xform As MathTransform _
) 
```

```

Dim instance As ICurve
Dim Xform As MathTransform
 
instance.ApplyTransform(Xform)
```

```

void ApplyTransform( 
   MathTransform Xform
)
```

```

void ApplyTransform( 
   MathTransform^ Xform
) 
```

#### Parameters

*Xform*
:   Pointer to [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)

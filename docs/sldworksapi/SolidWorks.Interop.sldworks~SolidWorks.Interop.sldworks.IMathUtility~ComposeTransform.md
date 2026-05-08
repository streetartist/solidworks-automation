# ComposeTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ComposeTransform`

Creates a new transform matrix.
Creates a new transform matrix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ComposeTransform( _
   ByVal XVec As MathVector, _
   ByVal YVec As MathVector, _
   ByVal ZVec As MathVector, _
   ByVal TransVec As MathVector, _
   ByVal Scale As System.Double _
) As MathTransform
```

```

Dim instance As IMathUtility
Dim XVec As MathVector
Dim YVec As MathVector
Dim ZVec As MathVector
Dim TransVec As MathVector
Dim Scale As System.Double
Dim value As MathTransform
 
value = instance.ComposeTransform(XVec, YVec, ZVec, TransVec, Scale)
```

```

MathTransform ComposeTransform( 
   MathVector XVec,
   MathVector YVec,
   MathVector ZVec,
   MathVector TransVec,
   System.double Scale
)
```

```

MathTransform^ ComposeTransform( 
   MathVector^ XVec,
   MathVector^ YVec,
   MathVector^ ZVec,
   MathVector^ TransVec,
   System.double Scale
) 
```

#### Parameters

*XVec*
:   [X-axis of the transform origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

*YVec*
:   [Y-axis of the transform origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

*ZVec*
:   [Z-axis of the transform origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

*TransVec*
:   Translation of the [origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) in space

*Scale*
:   Scale factor (typically 1; must be > 0)

#### Return Value

New [transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Remarks

XVec, YVec and ZVec are expected to be mutually orthogonal. These three vectors can be non-unit vectors and are unitized during the construction of the [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.md)  
[IMathUtility::CreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransform.md)  
[IMathUtility::CreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransformRotateAxis.md)  
[IMathUtility::ICreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransform.md)  
[IMathUtility::ICreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis.md)

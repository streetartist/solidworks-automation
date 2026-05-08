# ICreateTransformRotateAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis`

Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.
Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateTransformRotateAxis( _
   ByVal PointObjIn As MathPoint, _
   ByVal VectorObjIn As MathVector, _
   ByVal Angle As System.Double _
) As MathTransform
```

```

Dim instance As IMathUtility
Dim PointObjIn As MathPoint
Dim VectorObjIn As MathVector
Dim Angle As System.Double
Dim value As MathTransform
 
value = instance.ICreateTransformRotateAxis(PointObjIn, VectorObjIn, Angle)
```

```

MathTransform ICreateTransformRotateAxis( 
   MathPoint PointObjIn,
   MathVector VectorObjIn,
   System.double Angle
)
```

```

MathTransform^ ICreateTransformRotateAxis( 
   MathPoint^ PointObjIn,
   MathVector^ VectorObjIn,
   System.double Angle
) 
```

#### Parameters

*PointObjIn*
:   Center [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) of the axis of the transform

*VectorObjIn*
:   Axis [vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) of the transform

*Angle*
:   Angle of rotation about the X axis vector

#### Return Value

Newly created [math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.md)  
[IMathUtility::CreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransformRotateAxis.md)  
[IMathUtility::ComposeTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ComposeTransform.md)  
[IMathUtility::CreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransform.md)  
[IMathUtility::ICreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransform.md)

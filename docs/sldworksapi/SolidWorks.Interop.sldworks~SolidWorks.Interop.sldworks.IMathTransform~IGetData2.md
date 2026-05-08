# IGetData2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2`

Gets the math vectors and data that describe the transformation matrix.
Gets the math vectors and data that describe the transformation matrix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetData2( _
   ByRef XAxisObjOut As MathVector, _
   ByRef YAxisObjOut As MathVector, _
   ByRef ZAxisObjOut As MathVector, _
   ByRef TransformObjOut As MathVector, _
   ByRef ScaleOut As System.Double _
) 
```

```

Dim instance As IMathTransform
Dim XAxisObjOut As MathVector
Dim YAxisObjOut As MathVector
Dim ZAxisObjOut As MathVector
Dim TransformObjOut As MathVector
Dim ScaleOut As System.Double
 
instance.IGetData2(XAxisObjOut, YAxisObjOut, ZAxisObjOut, TransformObjOut, ScaleOut)
```

```

void IGetData2( 
   out MathVector XAxisObjOut,
   out MathVector YAxisObjOut,
   out MathVector ZAxisObjOut,
   out MathVector TransformObjOut,
   out System.double ScaleOut
)
```

```

void IGetData2( 
   [Out] MathVector^ XAxisObjOut,
   [Out] MathVector^ YAxisObjOut,
   [Out] MathVector^ ZAxisObjOut,
   [Out] MathVector^ TransformObjOut,
   [Out] System.double ScaleOut
) 
```

#### Parameters

*XAxisObjOut*
:   [Rotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) about the x axis

*YAxisObjOut*
:   [Rotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) about the y axis

*ZAxisObjOut*
:   [Rotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) about the z axis

*TransformObjOut*
:   [Transformation vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

*ScaleOut*
:   Scale

#### Return Value

The previous version of this method, [IMathTransform::IGetData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData.md), returned inversed x, y, z axes. This version of this method returns the actual x, y, z axes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[IMathTransform::GetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData2.md)  
[IMathTransform::ISetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ISetData.md)  
[IMathTransform::SetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~SetData.md)

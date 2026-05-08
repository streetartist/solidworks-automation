# GetData2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData2`

Gets the math vectors and data that describe the transformation matrix.
Gets the math vectors and data that describe the transformation matrix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetData2( _
   ByRef XAxisObjOut As System.Object, _
   ByRef YAxisObjOut As System.Object, _
   ByRef ZAxisObjOut As System.Object, _
   ByRef TransformObjOut As System.Object, _
   ByRef ScaleOut As System.Double _
) 
```

```

Dim instance As IMathTransform
Dim XAxisObjOut As System.Object
Dim YAxisObjOut As System.Object
Dim ZAxisObjOut As System.Object
Dim TransformObjOut As System.Object
Dim ScaleOut As System.Double
 
instance.GetData2(XAxisObjOut, YAxisObjOut, ZAxisObjOut, TransformObjOut, ScaleOut)
```

```

void GetData2( 
   out System.object XAxisObjOut,
   out System.object YAxisObjOut,
   out System.object ZAxisObjOut,
   out System.object TransformObjOut,
   out System.double ScaleOut
)
```

```

void GetData2( 
   [Out] System.Object^ XAxisObjOut,
   [Out] System.Object^ YAxisObjOut,
   [Out] System.Object^ ZAxisObjOut,
   [Out] System.Object^ TransformObjOut,
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

The previous version of this method, [IMathTransform::GetData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData.md), returned inversed x, y, z axes. This version of this method returns the actual x, y, z axes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[IMathTransform::IGetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2.md)  
[IMathTransform::ISetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ISetData.md)  
[IMathTransform::SetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~SetData.md)

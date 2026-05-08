# IGetData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData`

Obsolete. See IMathTransform::IGetData2.
Obsolete. See [IMathTransform::IGetData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetData( _
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
 
instance.IGetData(XAxisObjOut, YAxisObjOut, ZAxisObjOut, TransformObjOut, ScaleOut)
```

```

void IGetData( 
   out MathVector XAxisObjOut,
   out MathVector YAxisObjOut,
   out MathVector ZAxisObjOut,
   out MathVector TransformObjOut,
   out System.double ScaleOut
)
```

```

void IGetData( 
   [Out] MathVector^ XAxisObjOut,
   [Out] MathVector^ YAxisObjOut,
   [Out] MathVector^ ZAxisObjOut,
   [Out] MathVector^ TransformObjOut,
   [Out] System.double ScaleOut
) 
```

#### Parameters

*XAxisObjOut*

*YAxisObjOut*

*ZAxisObjOut*

*TransformObjOut*

*ScaleOut*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)

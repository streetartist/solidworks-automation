# ISetData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ISetData`

Sets the math vectors and data that describe the transformation matrix.
Sets the math vectors and data that describe the transformation matrix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetData( _
   ByVal XAxisObjIn As MathVector, _
   ByVal YAxisObjIn As MathVector, _
   ByVal ZAxisObjIn As MathVector, _
   ByVal TransformObjIn As MathVector, _
   ByVal ScaleValIn As System.Double _
) 
```

```

Dim instance As IMathTransform
Dim XAxisObjIn As MathVector
Dim YAxisObjIn As MathVector
Dim ZAxisObjIn As MathVector
Dim TransformObjIn As MathVector
Dim ScaleValIn As System.Double
 
instance.ISetData(XAxisObjIn, YAxisObjIn, ZAxisObjIn, TransformObjIn, ScaleValIn)
```

```

void ISetData( 
   MathVector XAxisObjIn,
   MathVector YAxisObjIn,
   MathVector ZAxisObjIn,
   MathVector TransformObjIn,
   System.double ScaleValIn
)
```

```

void ISetData( 
   MathVector^ XAxisObjIn,
   MathVector^ YAxisObjIn,
   MathVector^ ZAxisObjIn,
   MathVector^ TransformObjIn,
   System.double ScaleValIn
) 
```

#### Parameters

*XAxisObjIn*
:   X rotation [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object of the transform

*YAxisObjIn*
:   Y rotation [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object of the transform

*ZAxisObjIn*
:   Z rotation [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object of the transform

*TransformObjIn*
:   Translation [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object of the transform

*ScaleValIn*
:   Scale component of the transform

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[IMathTransform::SetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~SetData.md)  
[IMathTransform::GetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData2.md)  
[IMathTransform::IGetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2.md)

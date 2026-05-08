# SetData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~SetData`

Sets the math vectors and data that describe the transformation matrix.
Sets the math vectors and data that describe the transformation matrix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetData( _
   ByVal XAxisObjIn As System.Object, _
   ByVal YAxisObjIn As System.Object, _
   ByVal ZAxisObjIn As System.Object, _
   ByVal TransformObjIn As System.Object, _
   ByVal ScaleValIn As System.Double _
) 
```

```

Dim instance As IMathTransform
Dim XAxisObjIn As System.Object
Dim YAxisObjIn As System.Object
Dim ZAxisObjIn As System.Object
Dim TransformObjIn As System.Object
Dim ScaleValIn As System.Double
 
instance.SetData(XAxisObjIn, YAxisObjIn, ZAxisObjIn, TransformObjIn, ScaleValIn)
```

```

void SetData( 
   System.object XAxisObjIn,
   System.object YAxisObjIn,
   System.object ZAxisObjIn,
   System.object TransformObjIn,
   System.double ScaleValIn
)
```

```

void SetData( 
   System.Object^ XAxisObjIn,
   System.Object^ YAxisObjIn,
   System.Object^ ZAxisObjIn,
   System.Object^ TransformObjIn,
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
[IMathTransform::ISetData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ISetData.md)  
[IMathTransform::GetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~GetData2.md)  
[IMathTransform::IGetData2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IGetData2.md)

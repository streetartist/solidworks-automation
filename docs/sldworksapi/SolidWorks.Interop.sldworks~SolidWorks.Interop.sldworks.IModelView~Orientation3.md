# Orientation3 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3`

Gets or sets the model view orientation matrix.
Gets or sets the model view orientation matrix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Orientation3 As MathTransform
```

```

Dim instance As IModelView
Dim value As MathTransform
 
instance.Orientation3 = value
 
value = instance.Orientation3
```

```

MathTransform Orientation3 {get; set;}
```

```

property MathTransform^ Orientation3 {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

#### Property Value

[View orientation matrix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Remarks

When modifying a model view transform, you must use IModelView::Orientation3 and [IModelView::Translation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation3.md). For example:

...

Dim xyzOrigin As SldWorks.MathPoint

dPoint(0) = 0#: dPoint(1) = 0#: dPoint(2) = 0#

Set xyzOrigin = swMathUtil.CreatePoint((dPoint))

Set swVectorZ = swVectorZ.Scale(-1)

Set swMathTrans = swMathUtil.ComposeTransform(swVectorX, swVectorY, swVectorZ, xyzOrigin.ConvertToVector, 1#)

Set swMathTrans = swMathTrans.Inverse

Set swModelView = swModel.ActiveView

Set swViewTrans = swModelView.Orientation3

swModelView.Orientation3 = swMathTrans

Dim u As Double

u = swModelView.Scale2

Set swMathPoint = swVectorT.ConvertToPoint

Set swMathPoint = swMathPoint.Scale(-1 \* u)

Set swMathPoint = swMathPoint.MultiplyTransform(swMathTrans)

swModelView.Translation3 = swMathPoint.ConvertToVector

...

Also, check the vectors by looking at the triad in the model view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.md)

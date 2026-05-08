# Transform Property (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Transform`

Gets the model space to the model view plane transform.
Gets the model space to the model view plane transform.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Transform As MathTransform
```

```

Dim instance As IModelView
Dim value As MathTransform
 
instance.Transform = value
 
value = instance.Transform
```

```

MathTransform Transform {get; set;}
```

```

property MathTransform^ Transform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

#### Property Value

[View plane transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Remarks

This method is typically used when you are grabbing the view handle using [IModelView::GetViewHWnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWnd.md) or [IModelView::GetViewHWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWndx64.md) and drawing to the view. For example, if you had a point located at 2,2,2 in model space coordinates, then you could multiply it by this return value to determine where to draw in screen space coordinates. The result will be pixel values for the current view.

The screen space coordinate system has its origin in the upper-left corner of the current view with the X vector pointing to the right and the Y vector pointing down.

If the SOLIDWORKS file is in view-only mode and is not displaying a shaded image, then you cannot perform any view rotations. In this situation, you should not call any of the view rotation APIs.

To determine if the file is in view-only mode and whether it is shaded or not, see [IModelDoc2::IsOpenedViewOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.md) and [IModelView::GetDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)

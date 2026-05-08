# ModelToViewTransform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform`

Gets the math transform to go from model to drawing view space.
Gets the math transform to go from model to drawing view space.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ModelToViewTransform As MathTransform
```

```

Dim instance As IView
Dim value As MathTransform
 
instance.ModelToViewTransform = value
 
value = instance.ModelToViewTransform
```

```

MathTransform ModelToViewTransform {get; set;}
```

```

property MathTransform^ ModelToViewTransform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

#### Property Value

[Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Example

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetViewXform.md)  
[IView::GetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md)  
[IView::IGetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.md)  
[IView::IGetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md)  
[IView::ISetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetXform.md)  
[IView::SetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetXform.md)

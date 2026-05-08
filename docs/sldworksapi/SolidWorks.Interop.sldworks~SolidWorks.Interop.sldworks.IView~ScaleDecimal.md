# ScaleDecimal Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal`

Gets or sets the scale of the drawing view, returning the results in decimal format.
Gets or sets the scale of the drawing view, returning the results in decimal format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleDecimal As System.Double
```

```

Dim instance As IView
Dim value As System.Double
 
instance.ScaleDecimal = value
 
value = instance.ScaleDecimal
```

```

System.double ScaleDecimal {get; set;}
```

```

property System.double ScaleDecimal {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Drawing view scale

Remarks

[IView::ScaleRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleRatio.md) or [IView::IScaleRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IScaleRatio.md) and this property contain the same information, but use the value in different ways:

- IView::ScaleRatio gets or sets the scale as a ratio of two numbers.
- IView::ScaleDecimal returns the scale as a decimal number.

For example, if View::ScaleRatio returns 3 2 or 3:2, then IView::ScaleDecimal would return 1.5.

Changing this property can cause changes to the graphics of the drawing. After making all the of the view-related changes, call the [IModelDoc2::EditRebuild2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) method to regenerate the drawing to see these changes.

Example

[Set View Scale (VBA)](Set_View_Scale_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::UseParentScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseParentScale.md)  
[IView::UseSheetScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseSheetScale.md)

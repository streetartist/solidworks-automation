# IScaleRatio Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IScaleRatio`

Gets or sets the scale of the drawing view, returning the results in ratio format (n:n).
Gets or sets the scale of the drawing view, returning the results in ratio format (n:n).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IScaleRatio As System.Double
```

```

Dim instance As IView
Dim value As System.Double
 
instance.IScaleRatio = value
 
value = instance.IScaleRatio
```

```

System.double IScaleRatio {get; set;}
```

```

property System.double IScaleRatio {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Array of 2 doubles (see **Remarks**)

Remarks

The two values represent the two numbers if the scale is described as a ratio. The first value is the numerator; the second value is the denominator. This is what the scale is when represented as n:n.

This property and [IView::ScaleDecimal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal.md) contain the same information, but use the value in a different form.

- IView::ScaleRatio returns the scale as a ratio of two numbers.
- IView::ScaleDecimal returns the scale as a decimal number.

For example, if View::ScaleRatio returns 3 2 or 3:2, then IView::ScaleDecimal would return 1.5.

Changing this property may cause changes to the graphics of the drawing. After making all of the view-related changes, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to regenerate the drawing to see these changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::UseParentScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseParentScale.md)  
[IView::UseSheetScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseSheetScale.md)  
[IView::ScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleRatio.md)

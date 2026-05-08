# UseSheetScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseSheetScale`

Gets or sets whether the scale of the drawing view is the same as the scale of the drawing sheet on which this view is located.
Gets or sets whether the scale of the drawing view is the same as the scale of the drawing sheet on which this view is located.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseSheetScale As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
instance.UseSheetScale = value
 
value = instance.UseSheetScale
```

```

System.int UseSheetScale {get; set;}
```

```

property System.int UseSheetScale {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

1 if the view scale is the same as the sheet scale, 0 if the view scale is independent of the sheet scale

Remarks

If the property is 0, then it is possible that the view scale is the same as the sheet scale.

Changing this property can cause changes to the graphics of the drawing. After making all of the view-related changes, call the [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) method to regenerate the drawing to see these changes.

To set the drawing view's scale to be the same as the parent's drawing sheet's scale, use [IView::UseParentScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseParentScale.md).

Example

[Set View Scale (VBA)](Set_View_Scale_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::ScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleRatio.md)  
[IView::ScaleDecimal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal.md)  
[IView::IScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IScaleRatio.md)

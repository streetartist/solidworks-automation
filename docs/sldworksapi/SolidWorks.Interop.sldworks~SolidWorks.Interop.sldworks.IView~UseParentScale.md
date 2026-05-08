# UseParentScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseParentScale`

Gets or sets the drawing view's scale to match the parent drawing view's scale.
Gets or sets the drawing view's scale to match the parent drawing view's scale.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseParentScale As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.UseParentScale = value
 
value = instance.UseParentScale
```

```

System.bool UseParentScale {get; set;}
```

```

property System.bool UseParentScale {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the drawing view's scale is set to be the same as the parent's drawing view scale, false if the drawing view scale is independent of the parent's drawing view scale

Remarks

Changing this property can cause changes to the graphics of the drawing. After making all of the view-related changes, call the [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) method to regenerate the drawing to see these changes.

To set the drawing view's scale to be the same as the drawing sheet's scale, use [IView::UseSheetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseSheetScale.md).

Example

[Set View Scale Opposite Parent View Scale (VBA)](Set_View_Scale_Opposite_Parent_View_Scale_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IScaleRatio.md)  
[IView::ScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleRatio.md)  
[IView::ScaleDecimal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal.md)

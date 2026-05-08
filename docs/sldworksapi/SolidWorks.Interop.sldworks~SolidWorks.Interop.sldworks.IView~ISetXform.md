# ISetXform Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetXform`

Sets the matrix used for display of this drawing view.
Sets the matrix used for display of this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetXform( _
   ByRef Transform As System.Double _
) As System.Boolean
```

```

Dim instance As IView
Dim Transform As System.Double
Dim value As System.Boolean
 
value = instance.ISetXform(Transform)
```

```

System.bool ISetXform( 
   ref System.double Transform
)
```

```

System.bool ISetXform( 
   System.double% Transform
) 
```

#### Parameters

*Transform*
:   Array of 3 doubles (see **Remarks**)

#### Return Value

True if transform successfully set, false if not

Remarks

The 3 doubles are the X and Y position of the view, relative to the sheet origin, and the scale of the view.

Any view alignments that might affect this view are handled the same way as if you were using the user interface to draw the view to move it. If it is aligned with another view, then it will only move along the alignment vector. If it has child views that are aligned with it, then those views will also be moved along with this view.

Calling this method is equivalent to setting the [IView::Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Position.md) or [IView::IPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IPosition.md) property (to set X and Y), and the [IView::ScaleDecimal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal.md) property (to set the scale).

To get the view matrix, use [IView::GetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) or [IView::IGetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md) method.

Using this method may cause changes to the graphics of the drawing. Once all the view-related changes have been made, the user should call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to regenerate the drawing, in order to see these changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::SetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetXform.md)  
[IView::GetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetViewXform.md)  
[IView::IGetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.md)  
[IView::ModelToViewTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform.md)

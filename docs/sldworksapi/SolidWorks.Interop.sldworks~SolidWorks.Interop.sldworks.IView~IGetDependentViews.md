# IGetDependentViews Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDependentViews`

Gets either all, or only the specified, dependent views in this view.
Gets either all, or only the specified, dependent views in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDependentViews( _
   ByVal AllViews As System.Boolean, _
   ByVal SpecificViewType As System.Integer, _
   ByVal DependentViewCount As System.Integer _
) As View
```

```

Dim instance As IView
Dim AllViews As System.Boolean
Dim SpecificViewType As System.Integer
Dim DependentViewCount As System.Integer
Dim value As View
 
value = instance.IGetDependentViews(AllViews, SpecificViewType, DependentViewCount)
```

```

View IGetDependentViews( 
   System.bool AllViews,
   System.int SpecificViewType,
   System.int DependentViewCount
)
```

```

View^ IGetDependentViews( 
   System.bool AllViews,
   System.int SpecificViewType,
   System.int DependentViewCount
) 
```

#### Parameters

*AllViews*
:   True to get all of the dependent views in this view, false to get only the SpecificViewType views in this view

*SpecificViewType*
:   Type of dependent view as defined in [swDrawingViewTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingViewTypes_e.html)

*DependentViewCount*
:   Number of dependent views

#### Return Value

Array of dependent [views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Remarks

Call [IView::GetDependentViewCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViewCount.md) before calling this method to get the value of DependentViewCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDependentViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViews.md)

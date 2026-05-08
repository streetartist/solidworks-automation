# GetDependentViewCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViewCount`

Gets the number of all, or only the specified, dependent views (i.e., alternate position, detail, section, etc.) in this view.
Gets the number of all, or only the specified, dependent views (i.e., alternate position, detail, section, etc.) in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDependentViewCount( _
   ByVal AllViews As System.Boolean, _
   ByVal SpecificViewType As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim AllViews As System.Boolean
Dim SpecificViewType As System.Integer
Dim value As System.Integer
 
value = instance.GetDependentViewCount(AllViews, SpecificViewType)
```

```

System.int GetDependentViewCount( 
   System.bool AllViews,
   System.int SpecificViewType
)
```

```

System.int GetDependentViewCount( 
   System.bool AllViews,
   System.int SpecificViewType
) 
```

#### Parameters

*AllViews*
:   True to get the number of all of the dependent views in this view, false to get the number of SpecificViewType views in this view

*SpecificViewType*
:   Type of dependent view as defined in [swDrawingViewTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingViewTypes_e.html)

#### Return Value

Number of dependent views

Remarks

Call this method before calling [IView::IGetDependentViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDependentViews.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDependentViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViews.md)

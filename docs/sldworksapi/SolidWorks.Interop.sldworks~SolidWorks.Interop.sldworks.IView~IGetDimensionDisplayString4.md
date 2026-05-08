# IGetDimensionDisplayString4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayString4`

Gets all of the dimension text in the current drawing sheet or the current drawing view.
Gets all of the dimension text in the current drawing sheet or the current drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDimensionDisplayString4() As System.String
```

```

Dim instance As IView
Dim value As System.String
 
value = instance.IGetDimensionDisplayString4()
```

```

System.string IGetDimensionDisplayString4()
```

```

System.String^ IGetDimensionDisplayString4(); 
```

#### Return Value

Array of strings containing the dimension text (see **Remarks**)

Remarks

For each dimension in the drawing sheet or drawing view, this method returns 10 strings. If any of the dimension strings are not used, then those strings are returned as empty strings.

[ value1, tolMax1 tolMin1, value2, tolMax2, tolMin2, prefix, suffix, callout1, callout2 ]

This set of data is returned for each dimension in the view. See [IView::GetDimensionCount4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.md) to determine the number of dimensions in the drawing sheet or drawing view.

NOTES:

- A previous version of this method, [IView::GetDimensionDisplayString2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString2.md) or [IView::IGetDimensionDisplayString2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayString2.md), detects and overlooks dangling dimensions. These method, IView::GetDimensionDisplayString4 and [IView::IGetDimensionDisplayString4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayString4.md), do not overlook nor do they indicate that any dimensions are dangling. Use IView::GetDimensionDisplayString2 if you need dangling dimensions detected and overlooked.
- This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDimensionCount4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.md)  
[IView::GetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.md)  
[IView::GetDimensionDisplayInfoSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.md)  
[IView::GetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString4.md)  
[IView::GetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.md)  
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.md)  
[IView::GetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.md)  
[IView::IGetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayInfo5.md)  
[IView::IGetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionIds4.md)  
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.md)  
[IView::IGetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionString4.md)  
[IView::ProjectedDimensions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.md)  
[IView::GetFirstDisplayDimension5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.md)

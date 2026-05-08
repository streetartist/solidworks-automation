# GetPolyLineCount5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLineCount5`

Gets the number of polylines in this view with an option to include or exclude crosshatch lines.
Gets the number of polylines in this view with an option to include or exclude crosshatch lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPolyLineCount5( _
   ByVal CrossHatchOption As System.Short, _
   ByRef PointCount As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim CrossHatchOption As System.Short
Dim PointCount As System.Integer
Dim value As System.Integer
 
value = instance.GetPolyLineCount5(CrossHatchOption, PointCount)
```

```

System.int GetPolyLineCount5( 
   System.short CrossHatchOption,
   out System.int PointCount
)
```

```

System.int GetPolyLineCount5( 
   System.short CrossHatchOption,
   [Out] System.int PointCount
) 
```

#### Parameters

*CrossHatchOption*
:   Crosshatch option as defined in [swCrossHatchFilter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)

*PointCount*
:   Size of array needed to allocate in doubles for [IView::IGetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.md)

#### Return Value

Number of polylines

Remarks

Call this method before calling [IView::IGetPolylines6.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.md)

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Drawing view is in any of these modes:   - Shaded mode - Shaded with edges mode - Draft quality | This method returns 0.  Use [IView::SetDisplayMode3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.md) to change Shaded or Shaded with edges mode to Wireframe, Hidden Lines Removed (HLR), or Hidden Lines Visible (HLV), and then get the number of polylines. |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call [IModelDoc2::ViewZoomtofit2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomtofit2.md). |

Example

[Get Number of Polylines in Shaded Mode Drawing View (VBA)](Get_Number_of_Polylines_in_Shaded_Mode_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.md)  
[IView::GetPolylines6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.md)  
[IView::GetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurves.md)  
[IView::GetPolyLinesAndCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurvesCount.md)  
[IView::IGetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolyLinesAndCurves.md)

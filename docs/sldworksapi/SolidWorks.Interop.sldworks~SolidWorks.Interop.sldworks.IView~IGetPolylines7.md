# IGetPolylines7 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines7`

Gets all of the polylines in the view with an option to include or exclude crosshatch lines
Gets all of the polylines in the view with an option to include or exclude crosshatch lines

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPolylines7( _
   ByVal CrossHatchOption As System.Short, _
   ByVal ArraySize As System.Integer, _
   ByRef Polylines As System.Double, _
   ByVal EdgeArraySize As System.Integer _
) As System.Object
```

```

Dim instance As IView
Dim CrossHatchOption As System.Short
Dim ArraySize As System.Integer
Dim Polylines As System.Double
Dim EdgeArraySize As System.Integer
Dim value As System.Object
 
value = instance.IGetPolylines7(CrossHatchOption, ArraySize, Polylines, EdgeArraySize)
```

```

System.object IGetPolylines7( 
   System.short CrossHatchOption,
   System.int ArraySize,
   out System.double Polylines,
   System.int EdgeArraySize
)
```

```

System.Object^ IGetPolylines7( 
   System.short CrossHatchOption,
   System.int ArraySize,
   [Out] System.double Polylines,
   System.int EdgeArraySize
) 
```

#### Parameters

*CrossHatchOption*
:   - 0 = include crosshatch lines

    1 = exclude crosshatch lines

    2 = include only crosshatch lines

*ArraySize*
:   Number of lines in the view

*Polylines*
:   Array of doubles of the lines in the view of size ArraySize

*EdgeArraySize*
:   Size of array of modeling edges

#### Return Value

- in-process, unmanaged C++: Pointer to an array of modeling [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) and [silhouette edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.md) corresponding to polylines in the view
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

The difference between this method and [IView::GetPolyLinesAndCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurves.md) and [IView::IGetPolyLinesAndCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolyLinesAndCurves.md) is that splines and ellipses returned by these methods are returned as equation parameters, which are more precise definitions.

This method returns data for all visible solid model edges in the drawing view. This includes these types of edges:

> - 1 = arcs: Returned using a center point, radius, and start and stop location.
> - 1 = circles: Returned using a center point, radius, and start and stop location.
> - 2 = ellipses: Returned as tessellated polylines.
> - 3 = splines: Returned as tessellated polylines.
>
> - 0 = straight lines: Returned as tessellated polylines, but because the edges are straight, there is no loss of data in the approximation.

For each arc:

- first double gives the type
- next double gives the number of doubles required to hold arc geometry ( center, startPt, endPt, normal ) == 12
- next three doubles give the coordinates of center
- next three doubles give the coordinates of startPt
- next three doubles give the coordinates of endPt
- next three doubles give the coordinates of the normal
- next six doubles are line attributes:

  - LineColor = polyline color. This value is determined either by the explicitly set value or by the layer that the polyline is on.
  - LineStyle = value combines polyline font and weight information. This value can be used as an input to GetLineFontInfo and GetLineFontName. If this value is -1, then the user has probably modified the line display manually in the drawing and you should use the LineFont and LineWeight return values to recreate the exact polyline style.
  - LineFont = value is used for polyline font information. This value can be used as an input to the GetLineFontInfo2 and GetLineFontName2 functions. This value will only be valid if LineStyle is -1.
  - LineWeight = polyline weight where Thin = 0.0, Normal = 1.0, Thick = 2.0. This value will only be valid if LineStyle is -1.
  - LayerID = integer value indicating which layer holds this polyline. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).
  - LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- next double is the number of points lying on the arc
- next ( numPoints \* 3 ) doubles are the coordinates of points lying on the arc

 For each ellipse:

- first double gives the type
- next double gives the number of doubles required to hold ellipse geometry ( center, unit vector along majorAxis, unit vector along minor axis, major radius, minor radius, startPt, endPt, normal ) == 17
- next three doubles give the coordinates of center
- next three doubles give the coordinates of unit vector along major axis
- next three doubles give the coordinates of unit vector along minor axis
- next doubles gives the major radius
- next double gives the minor radius
- next three doubles give the coordinates of startPt
- next three doubles give the coordinates of endPt
- next six doubles are line attributes (see description of line attributes in previous bulleted item)
- next double is the number of points lying on the ellipse
- next ( numPoints \* 3 ) doubles are the coordinates of points lying on the ellipse

For each spline

- first double gives the type
- next double gives the number of doubles required to hold the information about the spline geometry ( 5 + numCtrlPts\* numDims + numKnot ); if the spline is rational, numDims ==4 otherwise numDims ==3
- next double gives degree = order -1
- next double gives whether the spline is rational (1) or non-rational (0)
- next double gives numDims ( i.e., number of coordinates associated with each control point; if the spline is rational , these are four, else three)
- next double gives the number of control points of the spline
- next double gives the number of knots on the spline
- next ( numCtlPoints\*numDims ) number of doubles are the coordinates of control points; each control point has numDims number of coordinates
- next "numKnots" number of doubles; the knots on the spline
- next six doubles are line attributes (see description of line attributes in previous bulleted item)
- next double is the number of points lying on the spline
- next ( numPoints \* 3 ) doubles are the coordinates of points lying on the spline

- For each polyline
- first double gives the type
- next double holds value 0.0 as there is no geometry information for a polyline
- next six doubles are line attributes (see description of line attributes in previous bulleted item)
- next double is the number of points lying on the polyline
- next ( numPoints \* 3 ) doubles are the coordinates of points lying on the polyline

This method also lets you include or exclude crosshatch lines. This method does not return data for sketch segments added by a user in the drawing view.

|  |  |
| --- | --- |
| **To get...** | **Call...** |
| Size of array needed to hold this data in COM applications | [IView::GetPolyLinesandCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurvesCount.md) |
| Items that were sketched in this drawing view | [IView::IGetArcs4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetArcs4.md)  [IView::IGetLines4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.md)  [IView::IGetSplines3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSplines3.md)  [IView::IGetEllipses5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetEllipses5.md) |

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Display mode of the view is:   - Shaded - Shaded with Edges - Draft Quality - Fast HLR/HLV | A value is not returned.  Use [IView::SetDisplayMode3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.md) to change Shaded or Shaded with Edges mode to Wireframe, Hidden Lines Removed (HLR), or Hidden Lines Visible (HLV), and then get the polylines. |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call [IModelDoc2::ViewZoomtofit2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomtofit2.md). |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.md)  
[IView::GetPolyLinesAndCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurvesCount.md)  
[IView::GetPolylines7 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines7.md)

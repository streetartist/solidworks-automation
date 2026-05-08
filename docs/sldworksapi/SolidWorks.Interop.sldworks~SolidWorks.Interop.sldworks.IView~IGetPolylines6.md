# IGetPolylines6 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6`

Obsolete. Superseded by IView::IGetPolylines7.
Obsolete. Superseded by [IView::IGetPolylines7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines7.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPolylines6( _
   ByVal CrossHatchOption As System.Short, _
   ByVal ArraySize As System.Integer, _
   ByRef Polylines As System.Double, _
   ByVal EdgeArraySize As System.Integer _
) As Edge
```

```

Dim instance As IView
Dim CrossHatchOption As System.Short
Dim ArraySize As System.Integer
Dim Polylines As System.Double
Dim EdgeArraySize As System.Integer
Dim value As Edge
 
value = instance.IGetPolylines6(CrossHatchOption, ArraySize, Polylines, EdgeArraySize)
```

```

Edge IGetPolylines6( 
   System.short CrossHatchOption,
   System.int ArraySize,
   out System.double Polylines,
   System.int EdgeArraySize
)
```

```

Edge^ IGetPolylines6( 
   System.short CrossHatchOption,
   System.int ArraySize,
   [Out] System.double Polylines,
   System.int EdgeArraySize
) 
```

#### Parameters

*CrossHatchOption*
:   - 0 = include crosshatch lines
    - 1 = exclude crosshatch lines
    - 2 = include only crosshatch lines

*ArraySize*
:   Size of array of lines

*Polylines*
:   Array of doubles representing the lines in the view (see **Remarks**)

*EdgeArraySize*
:   Size of array of modeling edges

#### Return Value

Array of modeling [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) corresponding to the polylines in the view

Remarks

The difference between this method and [IView::GetPolyLinesAndCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurves.md) and [IView::IGetPolyLinesAndCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolyLinesAndCurves.md) is that splines and ellipses returned by these methods are returned as equation parameters, which are more precise definitions.

This method returns data for all visible solid model edges in the drawing view. This includes these types of edges:

- arcs: Returned using a center point, radius, and start and stop location.
- circles: Returned using a center point, radius, and start and stop location.
- ellipses: Returned as tessellated polylines.
- splines: Returned as tessellated polylines.
- straight lines: Returned as tessellated polylines, but because the edges are straight, there is no loss of data in the approximation.

NOTE: If the view contains silhouette edges, then the polylines that render them cannot correspond to an edge because an edge does not actually exist. For example, if the third and fourth polyline in the set of polylines returned describe a silhouette edge, then array positions 4 and 5 in the edge array will be null.

This method also lets you include or exclude crosshatch lines. This method does not return data for sketch segments added by a user in the drawing view.

|  |  |
| --- | --- |
| **To get...** | **Call...** |
| Size of array needed to hold this data | [IView::GetPolylineCount5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLineCount5.md) |
| Items that were sketched in this drawing view | [IView::GetArcs4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcs4.md) and [IView::IGetArcs4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetArcs4.md)  [IView::GetLines4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLines4.md) and [IView::IGetLines4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.md)  [IView::GetSplines3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSplines3.md) and [IView::IGetSplines3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSplines3.md)  [IView::GetEllipses5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetEllipses5.md) and [IView::IGetEllipses5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetEllipses5.md) |

Format of the return value is the following array of doubles:

[ Type, GeomDataSize, GeomData[ ], LineColor, LineStyle, LineFont, LineWeight, LayerID, LayerOverride, NumPolyPoints, [x,y,z] ]

where:

Type = underlying geometry type, possible values are:

- 0 Polyline type
- 1 Arc or Circle type

GeomDataSize = number of elements in the GeomData array, for Type = 0 this will be 0.

GeomData[ ] = geometric data that can be used to represent the underlying geometry type. The data returned in this array is based on the underlying geometry type:

- Type = 0. This array is empty
- Type = 1. [ centerPtX, centerPtY, centerPtZ, startPtX, startPtY, startPtZ, endPtX, endPtY, endPtZ, normalX, normalY, normalZ ]

LineColor = polyline color. This value is determined either by the explicitly set value or by the layer that the polyline is on.

LineStyle = value combines polyline font and weight information. This value can be used as an input to GetLineFontInfo and GetLineFontName. If this value is -1, then the user has probably modified the line display manually in the drawing and you should use the LineFont and LineWeight return values to recreate the exact polyline style.

LineFont = value is used for polyline font information. This value can be used as an input to the GetLineFontInfo2 and GetLineFontName2 functions. This value will only be valid if LineStyle is -1.

LineWeight = polyline weight where Thin = 0.0, Normal = 1.0, Thick = 2.0. This value will only be valid if LineStyle is -1.

LayerID = integer value indicating which layer holds this polyline. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) and [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

NumPolyPoints = number of XYZ points found in the [x,y,z] return value

[x,y,z] = array of points used to describe the polyline. This array has NumPolyPoints points. This data will be returned for every polyline regardless of Type.

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
[IView::GetPolylines6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.md)  
[IView::GetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurves.md)  
[IView::IGetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolyLinesAndCurves.md)

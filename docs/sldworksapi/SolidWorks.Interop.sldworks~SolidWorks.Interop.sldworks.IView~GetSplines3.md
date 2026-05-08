# GetSplines3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSplines3`

Gets all of the splines added by a user in the drawing view.
Gets all of the splines added by a user in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplines3() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetSplines3()
```

```

System.object GetSplines3()
```

```

System.Object^ GetSplines3(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

This method only returns splines that were sketched by a user in this drawing view. Use [IView::GetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.md) or [IView::IGetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.md) to access the solid model's projected display data in the drawing view.

Format of return values is an array of doubles with the format:

[ [ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, NumSplinePoints, [x,y,z] ] ]

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType = line type. Valid returns as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex = line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).

LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

LayerID = integer value indicating which layer holds this entity. Obtain the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

This complete set of data repeats itself for each spline found in the view. For each spline, the array returned contains the color, line type, number of spline points in the spline, and X,Y,Z value for each of those points. Therefore, the [x,y,z] parameter is an array of NumSplinePoints, which can vary in size from spline to spline.

The [x,y,z] points for each spline are not the same as the points used to generate the spline. This method tessellates the spline based on the display quality and place points along the spline appropriately.

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from [IView::GetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) or [IView::IGetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md).

To determine data size needed in this method, use [IView::GetSplineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSplineCount.md) or get the number of elements in the array returned by this method.

If you are using COM, then this method must be preceded by a call to IView::GetSplineCount to determine memory allocation and to perform the actual gathering of spline data.

The sheet must be visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetSplines3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSplines3.md)

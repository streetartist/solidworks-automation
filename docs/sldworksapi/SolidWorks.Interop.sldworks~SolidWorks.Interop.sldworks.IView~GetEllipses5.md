# GetEllipses5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetEllipses5`

Gets all of the ellipses added by a user in this drawing view.
Gets all of the ellipses added by a user in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEllipses5() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetEllipses5()
```

```

System.object GetEllipses5()
```

```

System.Object^ GetEllipses5(); 
```

#### Return Value

Array of doubles (**Remarks**)

Remarks

This method only returns ellipses that were sketched by a user in this drawing view. Use [IView::GetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.md) or [IView::GetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.md) to access the solid model's projected display data in the drawing view.

All part and assembly geometry shown in a drawing view is represented by polylines. To access the polylines, use View::GetPolylines3.

The return values are in an array of doubles:

[ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3], Direction ... ]

where:

Color = COLORREF returned as an integer. Return value can be 0 or -1 for default color.

LineType = line type. Valid returns as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex = line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).

LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

LayerID = integer value indicating that layer holds this entity. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

StartPt[3] = array of 3 doubles (X,Y,Z) describing the ellipse start point.

EndPt[3] = array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt.

CenterPt[3] = array of 3 doubles (X,Y,Z) describing the ellipse center point.

MajorPt[3] = array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the major axis.

MinorPt[3] = array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the minor axis.

Direction = -1 for clockwise, +1 for counterclockwise.

This set of data repeats for each ellipse in the view. The size of the array is (NumEllipses \* 22). To determine the number of ellipses, use [IView::GetEllipseCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetEllipseCount.md).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from [IView::GetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) or [IView::IGetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md).

The sheet must be visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetEllipses5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetEllipses5.md)

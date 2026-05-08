# GetArcs4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcs4`

Gets all of the information for all of the arcs added by a user in this drawing view. }}-->
Gets all of the information for all of the arcs added by a user in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcs4() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetArcs4()
```

```

System.object GetArcs4()
```

```

System.Object^ GetArcs4(); 
```

#### Return Value

Array of doubles (see Remarks)

Remarks

This method only returns arcs that were sketched by a user in a drawing view. Use [IView::GetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.md) or [IView::IGetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.md) to access the solid model's projected display data in the drawing view.

Return value is an array of doubles with the format:

[ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], CenterPt[3], RotDir, ... ]

where:

- Color - COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- LineType - Line type. Valid returns as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A *LineType* is a combination of a line style and line weight.
- LineStyleIndex - Line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration.
- LineWidth - Integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- LayerID - Integer value indicating which layer holds this entity. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).
- LayerOverride - Integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if *LayerOverride* was returned as 3, the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- StartPt[3] - An array of 3 doubles (X,Y,Z) describing the start point.
- EndPt[3] - An array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then EndPt[3] is the same point as the StartPt.
- CenterPt[3] - An array of 3 doubles (X,Y,Z) describing the center point.
- RotDir - Rotational direction (CW = -1, CCW = 1)

...

This set of data repeats for each arc in the view. The size of the array is (NumArcs \* 16). To determine the number of arcs, use [IView::GetArcCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcCount.md).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then you should combine this data with the three return values from [IView::GetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) or [IView::IGetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.md).

The sheet must be visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetArcs4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetArcs4.md)

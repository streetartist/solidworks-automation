# GetLines4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLines4`

Gets all of the lines in the view with an option to include or exclude crosshatch lines.
Gets all of the lines in the view with an option to include or exclude crosshatch lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLines4( _
   ByVal CrossHatchOption As System.Short _
) As System.Object
```

```

Dim instance As IView
Dim CrossHatchOption As System.Short
Dim value As System.Object
 
value = instance.GetLines4(CrossHatchOption)
```

```

System.object GetLines4( 
   System.short CrossHatchOption
)
```

```

System.Object^ GetLines4( 
   System.short CrossHatchOption
) 
```

#### Parameters

*CrossHatchOption*
:   Crosshatch option as defined in [swCrossHatchFilter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)

#### Return Value

Array of doubles (see **Remarks**)

Remarks

This method only returns lines that were sketched in this drawing view. Use [IView::GetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.md) or [IView::IGetPolylines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.md) to access the solid model's projected display data in this view.

The return value is the following array of doubles:

[ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], ... ]

where all data values are returned as doubles:

- Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- LineType = line type. Valid returns as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight.
- LineStyleIndex = line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).
- LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- LayerID = integer value indicating which layer holds this entity. Obtain the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).
- LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- StartPt[3] = array of 3 doubles (X,Y,Z) describing the line start point.
- EndPt[3] = array of 3 doubles (X,Y,Z) describing the line end point.

This set of data repeats for each line in the view. The number of doubles returned is (lineCount \* 12). To determine the number of lines in the view, use [IView::GetLineCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLineCount2.md).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (that is, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from [IView::GetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) or [IView::IGetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md).

The sheet must be visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md).

Example

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetLines4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.md)

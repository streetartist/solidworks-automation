# GetBreakLineInfo2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo2`

Gets information for all of the break lines in this view.
Gets information for all of the break lines in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBreakLineInfo2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetBreakLineInfo2()
```

```

System.object GetBreakLineInfo2()
```

```

System.Object^ GetBreakLineInfo2(); 
```

#### Return Value

Array of data for all break lines in the view (see **Remarks**)

Remarks

The return value is a one-dimensional array consisting of the following data:

[ breaklineStyle, color, lineType, lineStyleIndex, lineWeight, layerId,

    layerOverride, numLines, numArcs, numSplines, [break line data] ]

where:

|  |  |
| --- | --- |
| breaklineStyle | Break line style as defined in [swBreakLineStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineStyle_e.html) |
| color | COLORREF returned as an integer; 0 or -1 for default color |
| lineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html); lineType is a combination of a lineStyle and lineWeight |
| lineStyleIndex | Line style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) |
| lineWeight | Line width as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) |
| layerId | An integer value indicating which layer holds this entity; [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) and [ILayerMgr::IGetLayerId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md) |
| layerOverride | An integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. Valid bit values as defined in [swLayerOverride\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLayerOverride_e.html):   - color = 0x1 - style = 0x2 - width = 0x4   Therefore, if LayerOverride is returned as 3, then the color and style are specifically set for this item and may not match the default values associated with this item's layer. |
| *numLines* | Number of line segments if a straight or zig zag break |
| *numArcs* | Number of arc lines if a curve break |
| *numSplines* | Number of spline lines if a jagged break |

|  |  |
| --- | --- |
| **If the break line style is swBreakLineStyle\_e...** | **Then [ *break line data* ] is packed with...** |
| swBreakLine\_Straight | 12 doubles (2 lines \* 1 segment \* 2 points \* 3 coordinates) |
| swBreakLine\_ZigZag | 60 doubles (2 lines \* 5 segments \* 2 points \* 3 coordinates) |
| swBreakLine\_SmallZigZag | 60 doubles (2 lines \* 5 segments \* 2 points \* 3 coordinates) |
| swBreakLine\_Curve | for each arc line in the break:   - arc direction (1 double) - start point (3 doubles) - end point (3 doubles) - center point (3 doubles) |
| swBreakLine\_Jagged | for each spline line in the break:   - *n* (1 integer) - 3\**n* doubles (*n* points \* 3 coordinates)   where:  *n* is the number of spline points generated based on the jagged cut shape intensity selected by the user in the Break View Property Manager |

Example

[Get Break Line Data (VBA)](Get_Break_Line_Data_Example_VB.htm)  
[Get Break Line Data (VB.NET)](Get_Break_Line_Data_Example_VBNET.htm)  
[Get Break Line Data (C#)](Get_Break_Line_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetBreakLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo2.md)  
[IView::GetBreakLineCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount2.md)  
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.md)  
[IView::IGetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLines.md)  
[IView::IsBroken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.md)  
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.md)  
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.md)

# IGetBreakLineInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo`

Obsolete. Superseded by IView::IGetBreakLineInfo2.
Obsolete. Superseded by [IView::IGetBreakLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBreakLineInfo( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetBreakLineInfo(ArraySize)
```

```

System.double IGetBreakLineInfo( 
   System.int ArraySize
)
```

```

System.double IGetBreakLineInfo( 
   System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Number of break lines

#### Return Value

Array of break line information (see **Remarks**)

Remarks

Before calling this method, call [IView::GetBreakLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount.md) to get the value for ArraySize.

The return value is the following array of doubles:

[ breaklineStyle, [ color, lineType, lineStyleIndex, lineWeight, layerId,

  layerOverride, number of lines, number of arcs ], line data or arc data ]

|  |  |
| --- | --- |
| breaklineStyle | Valid returns are found in [swBreakLineStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineStyle_e.html) |
| color | COLORREF returned as an integer. Return value could be 0 or -1 for default color |
| lineType | Valid returns are found in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight. |
| LineStyleIndex | Valid line styles can be found in [swLineStyles\_e.](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) |
| lineWeight | An integer value defining the line width. Valid width values can be found in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html). |
| layerId | An integer value indicating which layer holds this entity. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) and [ILayerMgr::IGetLayerId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md). |
| layerOverride | An integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are:   - color = 0x1 - style = 0x2 - width = 0x4   Therefore, if LayerOverride is returned as 3, then the color and style were specifically set for this item and may not match the default values associated with this item's layer. |
| Number of lines | Number of pairs of lines in the break line. |
| Number of arcs | Number of pairs of arcs in the break line. |

Each break line is a pair of line segments:

|  |  |
| --- | --- |
| **For...** | **Then...** |
| swBreakLineStraight | Each has 1 line for a total of 4 points:   - LineStartPt[3] - Line1EngPt[3] - Line2StartPt[3] - Line2EndPt[3] |
| swBreakLineZigZag | Each has 5 lines |
| swBreakLine\_SmallZigZag | Each has 5 lines |
| swBreakLine\_Curve | Each has 2 arcs; data is packed as follows:   - arcDirection - startPoint - EndPoint - CenterPoint |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo.md)  
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.md)  
[IView::IGetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLines.md)  
[IView::IsBroken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.md)  
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.md)  
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.md)

# IGetDimensionDisplayInfo5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayInfo5`

Gets the display dimension information for the current drawing sheet or the current drawing view.
Gets the display dimension information for the current drawing sheet or the current drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDimensionDisplayInfo5( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetDimensionDisplayInfo5(ArraySize)
```

```

System.double IGetDimensionDisplayInfo5( 
   System.int ArraySize
)
```

```

System.double IGetDimensionDisplayInfo5( 
   System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Number of items in the array

#### Return Value

Array of doubles (see **Remarks**)

Remarks

Before calling this method, call [IView::GetDimensionDisplayInfoSize2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.md) to get the value for ArraySize.

The data returned is an array of doubles as follows:

  dimensionCount, [lineCount, [lineSegmentCount [StartPt[3], endPt[3] ] ], arcCount, [arcSegmentCount, [arcCenter[3], [StartPt[3], EndPt[3] ] ], arrowCount, [ arrowTipPt[3], arrowVector[3], arrowWidth, arrowHeight ], tolType, isDual, showParens, textAngle, value1Pos[3], tolmax1Pos[3], tolmin1Pos[3], value2Pos[3], tolmax2Pos[3], tolmin2Pos[3], prefixPos[3], suffixPos[3], tolbox1Corner1[3], tolbox1Corner2[3], tolbox2Corner1[3], tolbox2Corner2[3], parenArc1Start[3], parenArc1End[3], parenArc1Center[3], parenArc1Vector[3], parenArc2Start[3], parenArc2End[3], parenArc2Center[3], parenArc2Vector[3], callout1TextPos[3], callout2TextPos[3] ]

where:

dimensionCount  = number of dimensions found in the drawing sheet or drawing view

For each dimension:

lineCount = number of extension and leader lines for this dimension

For each line:

StartPt[3] = array of three doubles representing the line start point

EndPt[3] = array of three doubles representing the line end point

 Repeating the StartPt[3] and EndPt[3] pair up to lineSegmentCount

arcCount = number of leader lines which are arcs for this dimension

For each arc:

arcCenter[3] = array of three doubles representing the arc center point

StartPt[3] = array of three doubles representing the arc start point

EndPt[3] = array of three doubles representing the arc end point

 Repeating the arcCenter[3], StartPt[3], and EndPt[3] group up to arcSegmentCount

arrowCount = number of arrowheads for this dimension

arrowTipPt[3] = array of three doubles representing the arrowhead tip location

arrowVector[3] = array of three doubles representing the arrow direction

arrowWidth = arrowhead width

arrowHeight = arrowhead height

 Repeating the arrowTipPt[3], arrowVector[3], arrowWidth and arrowHeight group up to arrowCount arrowheads

tolType = tolerance type as defined in [swTolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html)

isDual = True if this dimension is a dual dimension, false otherwise

showParens = True if parenthesis are shown, false otherwise

The next 25 values represent text angle and positioning. All text positions are the upper-left corner of the string.

textAngle = text angle in radians (counter clockwise from +ve x-axis)

value1Pos[3] = XYZ position of text 1; the position is the upper-left corner of the actual string

tolmax1Pos[3] = XYZ position of maximum tolerance text 1

tolmin1Pos[3]  = XYZ position of minimum tolerance text 1

value2Pos[3] = XYZ position of text 2; data returned is only valid if isDual is true

tolmax2Pos[3]  = XYZ position of maximum tolerance text 2; data returned is valid when isDual is true

tolmin2Pos[3]  = XYZ position of minimum tolerance text 2; data returned is valid when isDual is true

prefixPos[3] = XYZ position of prefix text

suffixPos[3] = XYZ position of suffix text

The next 12 values represent the box corners for dimensions with swTolBASIC tolerance types:

tolbox1Corner1[3] = XYZ corner 1 of tolerance box 1

tolbox1Corner2[3] = XYZ corner 2 of tolerance box 1

tolbox2Corner1[3] = XYZ corner 1 of tolerance box 2; data returned is valid when isDual is true

tolbox2corner2[3]  = XYZ corner 2 of tolerance box 2; data returned is valid when isDual is true

The next 24 values are valid when showParens is True; for example, when this is a reference dimension.

parenArc1Start[3] = XYZ start point of the arc representing parenthesis 1

parenArc1End[3]  = XYZ end point of the arc representing parenthesis 1

parenArc1Center[3]  = XYZ center point of the arc representing parenthesis 1

parenArc1Vector[3]  = XYZ reference direction for the arc representing parenthesis 1

parenArc2Start[3]  = XYZ start point of the arc representing parenthesis 2

parenArc2End[3]  = XYZ end point of the arc representing parenthesis 2

parenArc2Center[3]  = XYZ center point of the arc representing parenthesis 2

parenArc2Vector[3]  = XYZ reference direction for the arc representing parenthesis 2

callout1TextPos[3] = XYZ position of first callout text (text above)

callout2TextPos[3] = XYZ position of second callout text (text below)

Repeating the entire lineCount callout2TextPos group up to dimensionCount dimensions

For example, if a particular sheet or view had two dimensions, and the first dimension had three lines, zero arcs, and two arrows, and the second dimension had two lines, one arc, and two arrows, then array returned would be as follows:

[ 2, 3, line1StartPtx, y, z, line1EndPtx, y, z, line2StartPtx, y, z, line2EndPtx, y, z, line3StartPtx, y, z, line3EndPtx, y, z, 0, 2, arrow1TipPtx, y, z, arrow1Vectorx, y, z, arrow1Width, arrow1Height, arrow2TipPtx, y, z, arrow2Vectorx, y, z, arrow2Width, arrow2Height, tolType, isDual, showParens, textAngle, value1Posx, y, z, tolmax1Posx, y, z, tolmin1Posx, y, z, value2Posx, y, z, tolmax2Posx, y, z, tolmin2Posx, y, z, prefixPosx, y, z, suffixPosx, y, z, tolbox1Corner1x, y, z, tolbox1Corner2x, y, z, tolbox2Corner1x, y, z, tolbox2Corner2x, y, z, parenArc1Startx, y, z, parenArc1Endx, y, z, parenArc1Centerx, y, z, parenArc1Vectorx, y, z, parenArc2Startx, y, z, parenArc2Endx, y, z, parenArc2Centerx, y, z, parenArc2Vectorx, y, z, callout1TextPosx, y, z, callout2TextPosx, y, z, 2, line1StartPtx, y, z, line1EndPtx, y, z, line2StartPtx, y, z, line2EndPtx, y, z, 1, arc1Vertexx, y, z, arc1StartPtx, y, z, arc1EndPtx, y, z, 2, arrow1TipPtx, y, z, arrow1Vectorx, y, z, arrow1Width, arrow1Height, arrow2TipPtx, y, z, arrow2Vectorx, y, z, arrow2Width, arrow2Height, tolType, isDual, showParens, textAngle, value1Posx, y, z, tolmax1Posx, y, z, tolmin1Posx, y, z, value2Posx, y, z, tolmax2Posx, y, z, tolmin2Posx, y, z, prefixPosx, y, z, suffixPosx, y, z, tolbox1Corner1x, y, z, tolbox1Corner2x, y, z 

where the 3, 0, 2 and 2, 1, 2 represent the number of lines, arcs and arrows for each of the two dimensions. The information for the second dimension is underlined to distinguish it from information returned for the first dimension.

This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDimensionCount4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.md)  
[IView::GetDimensionDisplayInfoSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.md)  
[IView::GetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString4.md)  
[IView::GetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.md)  
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.md)  
[IView::GetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.md)  
[IView::IGetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayString4.md)  
[IView::IGetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionIds4.md)  
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.md)  
[IView::IGetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionString4.md)  
[IView::ProjectedDimensions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.md)

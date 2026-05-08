# GetDetailCircleInfo2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2`

Gets all of the information about each detail circle in the view.
Gets all of the information about each detail circle in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDetailCircleInfo2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDetailCircleInfo2()
```

```

System.object GetDetailCircleInfo2()
```

```

System.Object^ GetDetailCircleInfo2(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

[ numDetailCircles, [ layer, centerPt[3], startPt[3], endPt[3], lineType, textPt[3], textHeight, numArrows, [ arrowTip[3], arrowComponent[3], arrowWidth, arrowHeight, arrowStyle ] ] ]

where:

numDetailCircles = the number of detail circles in this view. See also [IView::GetDetailCircleCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleCount2.md).

The following set of data repeats itself for each detail circle in the view. The number of times the following information is given is numDetailCircles:

layer = integer value indicating which layer holds this entity. Obtain the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).

centerPt[3] = X,Y,Z center point for this detail circle

startPt[3] = X,Y,Z start point for this detail circle

endPt[3] = X,Y,Z end point for this detail circle

lineType  = line type for this detail circle as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html)

textPt[3] = X,Y,Z point for the text location.

textHeight  = text height in meters

numArrows = number of arrows for this detail circle.

The following set of data repeats itself for each arrow in the current detail circle. The number of times the following information is given is numArrows:

arrowTip[3]  = X,Y,Z start point for this arrow head

arrowComponent[3]  = X,Y,Z component for this arrow head

arrowWidth = width of this arrow head

arrowHeight = height of this arrow head

arrowStyle = style of this arrow head as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

To get the actual text value, see [IView::GetDetailCircleStrings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleStrings.md) or [IView::IGetDetailCircleStrings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleStrings.md).

The number of line segments, line segment geometry, and line type returned depend on the drawing's display standard.

Example

[Get Detail Circle Information (VBA)](Get_Detail_Circle_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetail.md)  
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.md)  
[IView::IGetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.md)  
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.md)  
[IView::IGetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircles.md)

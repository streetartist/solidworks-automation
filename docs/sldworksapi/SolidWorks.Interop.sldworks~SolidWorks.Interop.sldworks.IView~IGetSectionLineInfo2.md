# IGetSectionLineInfo2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2`

Gets all of the information about the section lines in the view.
Gets all of the information about the section lines in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSectionLineInfo2( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetSectionLineInfo2(ArraySize)
```

```

System.double IGetSectionLineInfo2( 
   System.int ArraySize
)
```

```

System.double IGetSectionLineInfo2( 
   System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Number of section lines

#### Return Value

Array of doubles (see **Remarks**)

Remarks

This method gets all of the information on section lines in the view. Before using this method, call [IView::GetSectionLineCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.md) to get the value for ArraySize.

The return value is the following array of doubles:

[ numSectionLines, layer, [ numSegments, [ lineType, startPt[3], endPt[3] ], arrowStart1[3], arrowEnd1[3], arrowWidth1, arrowHeight1, arrowStyle1, arrowStart2[3], arrowEnd2[3], arrowWidth2, arrowHeight2, arrowStyle2, textPt1[3], textPt2[3], textHeight ] ]

where:

numSectionLines  = number of section lines in this view. See also [IView::GetSectionLineCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.md).

layer = layer information.

The following set of data repeats itself for each section line in the view. The number of times the information is given is numSectionLines:

numSegments = number of line segments in this section line

The following three variables repeat themselves for each segment in the current section line. The number of times the information is given is numSegments:

lineType  = linetype for this line segment. See [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).

startPt[3]  = X,Y,Z start point for the current segment of this section line.

endPt[3]  = X,Y,Z end point for the current segment of this section line.

arrowStart1[3]  = X,Y,Z start point for arrow head 1 on this section line.

arrowEnd1[3]  = X,Y,Z end point for arrow head 1 on this section line.

arrowWidth1  = width of arrow 1 on this section line.

arrowHeight1  = height of arrow 1 on this section line.

arrowStyle1  = style of arrow 1 on this section line.

arrowStart2[3]  = X,Y,Z start point for arrow head 2 on this section line.

arrowEnd2[3]  = X,Y,Z end point for arrow head 2 on this section line.

arrowWidth2  = width of arrow 2 on this section line.

arrowHeight2  = height of arrow 2 on this section line.

arrowStyle2  = style of arrow 2 on this section line.

textPt1[3]  = X,Y,Z point for the text location near arrow 1.

textPt2[3]  = X,Y,Z point for the text location near arrow 2.

textHeight  = text height in meters.

To get the actual text value, use [IView::GetSectionLineStrings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.md) or [IView::IGetSectionLineStrings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineStrings.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSection.md)  
[IView::GetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.md)  
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.md)  
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.md)  
[IView::IGetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSection.md)  
[IView::IGetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLines.md)

# GetCenterMarkInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo`

Gets information about each center mark that is a feature in the view.
Gets information about each center mark that is a feature in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCenterMarkInfo() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetCenterMarkInfo()
```

```

System.object GetCenterMarkInfo()
```

```

System.Object^ GetCenterMarkInfo(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

Center marks are now annotations. Previously, center marks were features. This method is only valid for center marks that are features.

The return value is the following array of doubles:

[ numCenterMarks, [ numCenterMarkLines, lineType1, plus1StartPt[3], plus1EndPt[3], lineType2, plus2StartPt[3], plus2EndPt[3], [ lineType, lineStartPt[3], lineEndPt[3] ] ] ]

where:

numCenterMarks = is the number of center marks in this view. See also [IView::GetCenterMarkCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.md).

The following set of data repeats itself for each center mark in the view. The number of times the information is given is numCenterMarks:

numCenterMarkLines = number of centermark lines in the current center mark. Every center mark has at least two lines. These two lines represent the plus at the center of the circle.

lineType1 = line type associated with the first plus-sign line. See the [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) enumeration.

plus1StartPt[3] = X,Y,Z start point of the first line in the plus sign.

plus1EndPt[3] = X,Y,Z end point of the first line in the plus sign.

lineType2 = line type associated with the second plus-sign line. See the [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) enumeration.

plus2StartPt[3] = X,Y,Z start point of the second line in the plus sign.

plus2EndPt[3] = X,Y,Z end point of the second line in the plus sign.

This set of data also repeats itself for the remaining centermark lines in this particular center mark. The number of times this information is given is (numCenterMarkLines - 2):

LineType = line type associated with the second plus-sign line. See the [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) enumeration.

lineStartPt[3] = X,Y,Z start point for this centermark line.

lineEndPt[3] = X,Y,Z end point for this centermark line.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.md)  
[IView::GetFirstCenterMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark.md)  
[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.md)  
[IView::IGetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks.md)  
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.md)

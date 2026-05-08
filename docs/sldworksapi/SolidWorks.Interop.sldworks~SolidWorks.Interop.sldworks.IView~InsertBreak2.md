# InsertBreak2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak2`

Obsolete. Superseded by IView::InsertBreak3.
Obsolete. Superseded by [IView::InsertBreak3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBreak2( _
   ByVal Orientation As System.Integer, _
   ByVal Position1 As System.Double, _
   ByVal Position2 As System.Double, _
   ByVal Style As System.Integer, _
   ByVal ShapeIntensity As System.Integer _
) As BreakLine
```

```

Dim instance As IView
Dim Orientation As System.Integer
Dim Position1 As System.Double
Dim Position2 As System.Double
Dim Style As System.Integer
Dim ShapeIntensity As System.Integer
Dim value As BreakLine
 
value = instance.InsertBreak2(Orientation, Position1, Position2, Style, ShapeIntensity)
```

```

BreakLine InsertBreak2( 
   System.int Orientation,
   System.double Position1,
   System.double Position2,
   System.int Style,
   System.int ShapeIntensity
)
```

```

BreakLine^ InsertBreak2( 
   System.int Orientation,
   System.double Position1,
   System.double Position2,
   System.int Style,
   System.int ShapeIntensity
) 
```

#### Parameters

*Orientation*
:   Horizontal or vertical cut as defined in [swBreakLineOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineOrientation_e.html)

*Position1*
:   Location of the first line in the break (see Remarks)

*Position2*
:   Location of the second line in the break (see Remarks)

*Style*
:   Break line style as defined in [swBreakLineStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineStyle_e.html)

*ShapeIntensity*
:   Shape intensity for jagged cut break lines only; valid range is 1 (most) through 5 (least)

#### Return Value

[Break line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)

Remarks

A break in a drawing view consists of a pair of break lines. This method inserts the break lines at the locations indicated by Position1 and Position2.

| If the orientation of the break is... | Then Position1 and Position2 are... |
| --- | --- |
| Horizontal | Y values relative to the drawing view origin, indicating where along the Y axis to place the breaks |
| Vertical | X values relative to the drawing view origin, indicating where along the X axis to place the breaks |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBreakLineCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount2.md)  
[IView::GetBreakLineInfo2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo2.md)  
[IView::GetBreakLines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.md)  
[IView::IsBroken Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.md)  
[IView::BreakLineGap Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.md)  
[IDrawingDoc::BreakView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.md)

# AutoInsertCenterMarks Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks`

Obsolete. Superseded by IView::AutoInsertCenterMarks2.
Obsolete. Superseded by [IView::AutoInsertCenterMarks2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoInsertCenterMarks( _
   ByVal InsertType As System.Integer, _
   ByVal InsertOption As System.Integer, _
   ByVal LinearSlotCenter As System.Boolean, _
   ByVal ArcSlotCenter As System.Boolean, _
   ByVal UseDocumentDefaults As System.Boolean, _
   ByVal Size As System.Double, _
   ByVal ExtendedLines As System.Boolean, _
   ByVal CenterLineFont As System.Boolean, _
   ByVal Angle As System.Double _
) As System.Boolean
```

```

Dim instance As IView
Dim InsertType As System.Integer
Dim InsertOption As System.Integer
Dim LinearSlotCenter As System.Boolean
Dim ArcSlotCenter As System.Boolean
Dim UseDocumentDefaults As System.Boolean
Dim Size As System.Double
Dim ExtendedLines As System.Boolean
Dim CenterLineFont As System.Boolean
Dim Angle As System.Double
Dim value As System.Boolean
 
value = instance.AutoInsertCenterMarks(InsertType, InsertOption, LinearSlotCenter, ArcSlotCenter, UseDocumentDefaults, Size, ExtendedLines, CenterLineFont, Angle)
```

```

System.bool AutoInsertCenterMarks( 
   System.int InsertType,
   System.int InsertOption,
   System.bool LinearSlotCenter,
   System.bool ArcSlotCenter,
   System.bool UseDocumentDefaults,
   System.double Size,
   System.bool ExtendedLines,
   System.bool CenterLineFont,
   System.double Angle
)
```

```

System.bool AutoInsertCenterMarks( 
   System.int InsertType,
   System.int InsertOption,
   System.bool LinearSlotCenter,
   System.bool ArcSlotCenter,
   System.bool UseDocumentDefaults,
   System.double Size,
   System.bool ExtendedLines,
   System.bool CenterLineFont,
   System.double Angle
) 
```

#### Parameters

*InsertType*
:   Features for which to insert center marks as defined in [swAutoInsertCenterMarkTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutoInsertCenterMarkTypes_e.html)

*InsertOption*
:   Center mark options as defined in [swCenterMarkConnectionLine\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkConnectionLine_e.html)

*LinearSlotCenter*
:   True to add center marks to slot centers, false to add them to slot ends

*ArcSlotCenter*
:   True to add center marks to arc centers, false to add them to arc ends

*UseDocumentDefaults*
:   True to use the display attribute defaults specified in [Document Properties > Centerlines/Center Marks](ms-help://SolidWorks.Interop.swconst/SolidWorks/DP_CenterlinesCenterMarks.htm), false to use the display attributes set by this method

*Size*
:   Size of center mark; valid only if UseDocumentDefaults is false

*ExtendedLines*
:   True to extend lines from center mark points, false to not; valid only if UseDocumentDefaults is false

*CenterLineFont*
:   True to use the centerline font, false to not; valid only if UseDocumentDefaults is false

*Angle*
:   Rotation angle for the center mark; a positive angle rotates the center mark counterclockwise

#### Return Value

True if successful, false if not

Remarks

Call this method on each active view in which you want to insert center marks.

Before calling this method:

1. Call [IDrawingDoc::ActivateView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.md) with the name of the view to activate.
2. Call [IDrawingDoc::ActiveDrawingView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.md) to get a handle on the activated view.

Call [IDrawingDoc::InsertCenterMark3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark3.md) if you want to insert one center mark in one view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterMarkCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.md)  
[IView::GetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.md)  
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.md)

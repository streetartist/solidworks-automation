# IGetBreakLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLines`

Gets the all of the breaks in this view.
Gets the all of the breaks in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBreakLines( _
   ByVal Count As System.Integer _
) As BreakLine
```

```

Dim instance As IView
Dim Count As System.Integer
Dim value As BreakLine
 
value = instance.IGetBreakLines(Count)
```

```

BreakLine IGetBreakLines( 
   System.int Count
)
```

```

BreakLine^ IGetBreakLines( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of breaks in the view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [breaks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IView::GetBreakLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount.md) to get the value for Count.

This method gets all of the breaks in the view, regardless if the view is broken. A drawing view can have break lines that are not applied. To determine whether a view is broken, use [IView::IsBroken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo.md)  
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.md)  
[IView::IGetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo.md)  
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.md)  
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.md)

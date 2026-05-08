# GetBreakLineCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount2`

Gets the number of breaks lines and breaks in this view.
Gets the number of breaks lines and breaks in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBreakLineCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer
 
value = instance.GetBreakLineCount2(Size)
```

```

System.int GetBreakLineCount2( 
   out System.int Size
)
```

```

System.int GetBreakLineCount2( 
   [Out] System.int Size
) 
```

#### Parameters

*Size*
:   Size of an array of doubles to allocate in [IView::GetBreakLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo2.md) and [IView::IGetBreakLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo2.md)

#### Return Value

Number of breaks

Remarks

A drawing view can have break lines without the break being applied. To determine whether a view is broken, use [IView::IsBroken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.md).

A break in a drawing view consists of a pair of lines. This method returns the number of breaks in the view. For example, this method returns 3 for a view that has three breaks in it, even though there are six lines on the display.

Call this method before calling [IView::IGetBreakLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLines.md) to determine the size of the array for that method.

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
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.md)  
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.md)  
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.md)

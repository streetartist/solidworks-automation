# BreakView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView`

Breaks the drawing view along the existing break lines.
Breaks the drawing view along the existing break lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub BreakView() 
```

```

Dim instance As IDrawingDoc
 
instance.BreakView()
```

```

void BreakView()
```

```

void BreakView(); 
```

Remarks

Use [IDrawingDoc::InsertBreakHorizontal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakHorizontal.md) or [IDrawingDoc::InsertBreakVertical](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakVertical.md) to insert break lines to a drawing view. Customize the break by dragging and repositioning the break lines. Then, call this method to create the break view.

You can set the font of the break lines using [IBreakLine::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Style.md).

Example

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)  
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)  
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::InsertBreakHorizontal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakHorizontal.md)  
[IDrawingDoc::InsertBreakVertical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakVertical.md)  
[IDrawingDoc::UnBreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnBreakView.md)

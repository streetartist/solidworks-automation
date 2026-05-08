# InsertBreakHorizontal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakHorizontal`

Inserts a horizontal break in the drawing view.
Inserts a horizontal break in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertBreakHorizontal() 
```

```

Dim instance As IDrawingDoc
 
instance.InsertBreakHorizontal()
```

```

void InsertBreakHorizontal()
```

```

void InsertBreakHorizontal(); 
```

Remarks

To create the break view, use [IDrawingDoc::BreakView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.md).

You can:

- Customize the break by dragging and repositioning the break lines.
- Set the font of the break lines using [IBreakLine::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Style.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::UnInsertBreakVertical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakVertical.md)  
[IDrawingDoc::UnBreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnBreakView.md)  
[IDrawingDoc::BreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.md)

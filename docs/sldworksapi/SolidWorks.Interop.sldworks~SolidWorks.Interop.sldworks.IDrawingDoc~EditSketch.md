# EditSketch Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSketch`

Allows editing of a sketch in the selected drawing view or sheet.
Allows editing of a sketch in the selected drawing view or sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditSketch() 
```

```

Dim instance As IDrawingDoc
 
instance.EditSketch()
```

```

void EditSketch()
```

```

void EditSketch(); 
```

Remarks

Creating subsequent geometry resides in this drawing view or sheet.

If you selected a drawing view and called IDrawingDoc::EditSketch, then you can resume editing the drawing sheet by calling [IDrawingDoc::EditSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md) or by selecting the sheet and calling IDrawingDoc::EditSketch again.

To determine the current state, use [IDrawingDoc::GetEditSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

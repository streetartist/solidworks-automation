# IGetFirstView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView`

Gets the first drawing view on the current sheet.
Gets the first drawing [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) on the current sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstView() As View
```

```

Dim instance As IDrawingDoc
Dim value As View
 
value = instance.IGetFirstView()
```

```

View IGetFirstView()
```

```

View^ IGetFirstView(); 
```

#### Return Value

Pointer to the first drawing [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) in this drawing document

Remarks

This method might be useful for starting an iteration through all the drawing views on the current sheet.

Because the drawing sheet also has sketch geometry, notes, GTols, and so on, this method returns the current drawing sheet. The next view returned by [IView::GetNextView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.md) is the first drawing view in the current sheet.

Example

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.md)  
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.md)  
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.md)  
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.md)  
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.md)  
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.md)

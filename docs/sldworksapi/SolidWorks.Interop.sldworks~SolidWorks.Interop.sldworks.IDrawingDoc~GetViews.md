# GetViews Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViews`

Gets the all of the views, including the sheets, in this drawing document.
Gets the all of the views, including the sheets, in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetViews() As System.Object
```

```

Dim instance As IDrawingDoc
Dim value As System.Object
 
value = instance.GetViews()
```

```

System.object GetViews()
```

```

System.Object^ GetViews(); 
```

#### Return Value

An array of arrays (see **Remarks**)

Remarks

The return value is an array of arrays with a length equal to the number of sheets in the drawing document. Each of those arrays is a list of views with the first view in the list being the sheet itself.

If there are multiple sheets in the drawing document, then the order in which the sheets are returned is undetermined. So, the active sheet and its views might not be returned in the first array.

For example, when there are three sheets in the drawing document:

|  |  |
| --- | --- |
| One sheet contains 6 views, so first array has this number of elements | = 7 (sheet + 6 views) |
| Another sheet contains 2 views, so second array has this number of elements | = 3 (sheet + 2 views) |
| Another sheet contains no views, so third array has this number of elements | = 1 (sheet + 0 views) |

Example

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViewCount.md)  
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.md)  
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.md)  
[ISheet::GetViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetViews.md)  
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.md)  
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.md)

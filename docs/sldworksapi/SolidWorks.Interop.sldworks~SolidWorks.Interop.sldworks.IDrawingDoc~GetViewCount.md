# GetViewCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViewCount`

Gets all of the number of all of views, including the number of sheets, in this drawing document.
Gets all of the number of all of views, including the number of sheets, in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetViewCount() As System.Integer
```

```

Dim instance As IDrawingDoc
Dim value As System.Integer
 
value = instance.GetViewCount()
```

```

System.int GetViewCount()
```

```

System.int GetViewCount(); 
```

#### Return Value

Number of views, including the number of sheets, in this drawing document (see **Remarks**)

Remarks

For example, when:

|  |  |
| --- | --- |
| Number of sheets in drawing document | =  2 |
| Number of views on Sheet1 | =  6 |
| Number of views on Sheet2 | =  2 |
| Return value | = 10 |

The active sheet might not be the first sheet in the return value.

Example

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViews.md)  
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.md)  
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.md)  
[ISheet::GetViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetViews.md)  
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.md)  
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.md)

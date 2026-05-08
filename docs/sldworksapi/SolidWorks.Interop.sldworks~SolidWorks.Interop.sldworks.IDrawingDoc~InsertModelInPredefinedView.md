# InsertModelInPredefinedView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelInPredefinedView`

Inserts the model into the predefined drawing views in the active drawing sheet.
Inserts the model into the predefined drawing views in the active drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertModelInPredefinedView( _
   ByVal ModelName As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim value As System.Boolean
 
value = instance.InsertModelInPredefinedView(ModelName)
```

```

System.bool InsertModelInPredefinedView( 
   System.string ModelName
)
```

```

System.bool InsertModelInPredefinedView( 
   System.String^ ModelName
) 
```

#### Parameters

*ModelName*
:   Name of the model to insert into the predefined drawing views in the active drawing sheet

#### Return Value

True if the model is inserted, false if not

Remarks

|  |  |
| --- | --- |
| **If you...** | **Then...** |
| Preselect drawing views | This method inserts the model in those predefined drawing views. |
| Do not preselect any drawing views | This method inserts the model in all predefined views in the drawing. |
| Specify an empty filename | SOLIDWORKS prompts the user for the desired model's  filename. |
| Specify a filename | SOLIDWORKS inserts that model into the predefined drawing views, without displaying any dialogs. |

If the model is not already open, SOLIDWORKS attempts to open it hidden.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.md)  
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)  
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.md)  
[IDrawingDoc::HideShowDrawingViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDrawingViews.md)  
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.md)  
[IDrawingDoc::SuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.md)  
[IDrawingDoc::UnsuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnsuppressView.md)  
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.md)  
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.md)  
[IDrawingDoc::ReplaceViewModel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReplaceViewModel.md)

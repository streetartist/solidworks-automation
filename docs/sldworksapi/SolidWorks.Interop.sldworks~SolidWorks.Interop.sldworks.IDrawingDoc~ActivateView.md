# ActivateView Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView`

Activates the specified drawing view.
Activates the specified drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateView( _
   ByVal ViewName As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim ViewName As System.String
Dim value As System.Boolean
 
value = instance.ActivateView(ViewName)
```

```

System.bool ActivateView( 
   System.string ViewName
)
```

```

System.bool ActivateView( 
   System.String^ ViewName
) 
```

#### Parameters

*ViewName*
:   Name of the drawing view

#### Return Value

True if successful, false if not

Remarks

This method returns false when trying to activate a drawing sheet. To activate a drawing sheet, use [IDrawingDoc::ActivateSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md).

Example

[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)  
[Create Detail View (VBA)](Create_Detail_View_Example_VB.htm)  
[Insert Autoballoons Using IDrawingDoc::AutoBalloon2 (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)  
[Undo Deleted Note and Fire Undo Post-Notify Event (VB.NET)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)  
[Undo Deleted Note and Fire Undo Post-Notify Event (C#)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)  
[Undo Deleted Note and Fire Undo Post-Notify Event (VBA)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)  
[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)  
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)  
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.md)  
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.md)  
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.md)  
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.md)

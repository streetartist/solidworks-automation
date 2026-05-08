# ActivateSheet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet`

Activates the specified drawing sheet.
Activates the specified drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateSheet( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.ActivateSheet(Name)
```

```

System.bool ActivateSheet( 
   System.string Name
)
```

```

System.bool ActivateSheet( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of the sheet

#### Return Value

True if the sheet was activated, false if SOLIDWORKS generated an error

Remarks

This command makes the specified sheet the active or current sheet, similar to [IDrawingDoc::SheetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.md) or [IDrawingDoc::SheetPrevious](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.md). You can use [IDrawingDoc::GetCurrentSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.md) or [IDrawing::IGetCurrentSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.md) with an active sheet to gain access to the ISheet interface.

To activate a drawing view, you can use [IDrawingView::ActivateView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.md).

Example

[Copy and Paste Drawing Sheet (C#)](Copy_and_Paste_Drawing_Sheet_Example_CSharp.htm)  
[Copy and Paste Drawing Sheet (VB.NET)](Copy_and_Paste_Drawing_Sheet_Example_VBNET.htm)  
[Copy and Paste Drawing Sheet (VBA)](Copy_and_Paste_Drawing_Sheet_Example_VB.htm)  
[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)  
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)  
[Get Loaded Sheets (C#)](Get_Loaded_Sheets_Example_CSharp.htm)  
[Get Loaded Sheets (VB.NET)](Get_Loaded_Sheets_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.md)  
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.md)  
[IDrawingDoc::IGetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.md)  
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)

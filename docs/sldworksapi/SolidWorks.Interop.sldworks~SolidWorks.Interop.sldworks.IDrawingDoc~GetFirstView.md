# GetFirstView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView`

Gets the first drawing view on the current sheet.
Gets the first drawing [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) on the current sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstView() As System.Object
```

```

Dim instance As IDrawingDoc
Dim value As System.Object
 
value = instance.GetFirstView()
```

```

System.object GetFirstView()
```

```

System.Object^ GetFirstView(); 
```

#### Return Value

First drawing [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) in this drawing document

Remarks

This method might be useful for starting an iteration through all the drawing views on the current sheet.

Because the drawing sheet also has sketch geometry, notes, GTols, and so on, this method returns the current drawing sheet. The next view returned by [IView::GetNextView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.md) is the first drawing view in the current sheet.

Example

[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)  
[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)  
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)  
[Get Crosshatches on View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)  
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)  
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)  
[Traverse Drawing FeatureManager Design Tree (VBA)](Traverse_Drawing_FeatureManager_Design_Tree_Example_VB.htm)  
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)  
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)  
[Get View Bounding Box and Position (VB.NET)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)  
[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md)  
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.md)  
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.md)  
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.md)  
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.md)  
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.md)  
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.md)

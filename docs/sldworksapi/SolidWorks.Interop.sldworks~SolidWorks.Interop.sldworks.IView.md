# IView Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView`

Represents drawing views found in a drawing document.
Represents drawing views found in a drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IView 
```

```

Dim instance As IView
```

```

public interface IView 
```

```

public interface class IView 
```

Remarks

A drawing document can consist of one or more drawing sheets. Each drawing sheet typically contains one or more drawing views. Each drawing view is an oriented snapshot of a particular SOLIDWORKS model and a particular configuration of the model.

The IView object lets you determine the particular model and configuration being viewed and to get information about all the objects in a drawing sheet or drawing view, as well as the drawing view bounds, and transforms.

Example

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)  
[Set View Display Mode (C++)](Set_View_Display_Mode_Example_CPlusPlus_COM.htm)  
[Autodimension Selected Drawing View (VBA)](Autodimension_Selected_Drawing_View_Example_VB.htm)  
[Get Base Views (VBA)](Get_Base_Views_Example_VB.htm)  
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)  
[Insert Alternate Position View (VBA)](Insert_Alternate_Position_View_Example_VB.htm)  
[Reposition Drawing Views to Avoid Overlap (VBA)](Reposition_Drawing_Views_to_Avoid_Overlap_Example_VB.htm)  
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)  
[Insert Weldment Cut List Table (VBA)](Insert_Weldment_Cut_List_Table_Example_VB.htm)  
[Insert Weldment Cut List Table (VB.NET)](Insert_Weldment_Cut_List_Table_Example_VBNET.htm)  
[Insert Weldment Cut List Table (C#)](Insert_Weldment_Cut_List_Table_Example_CSharp.htm)  
[Insert Weld Table (VBA)](Insert_Weld_Table_Example_VB.htm)  
[Insert Weld Table (VB.NET)](Insert_Weld_Table_Example_VBNET.htm)  
[Insert Weld Table (C#)](Insert_Weld_Table_Example_CSharp.htm)  
[Get Break Line Data (VBA)](Get_Break_Line_Data_Example_VB.htm)  
[Get Break Line Data (VB.NET)](Get_Break_Line_Data_Example_VBNET.htm)  
[Get Break Line Data (C#)](Get_Break_Line_Data_Example_CSharp.htm)  
[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)  
[Insert Hole Table (VB.NET)](Insert_Hole_Table_Example_VBNET.htm)  
[Insert Hole Table (C#)](Insert_Hole_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)

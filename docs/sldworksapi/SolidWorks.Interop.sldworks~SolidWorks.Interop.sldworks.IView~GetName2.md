# GetName2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetName2`

Gets the name of this drawing view displayed in the FeatureManager design tree.
Gets the name of this drawing view displayed in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetName2() As System.String
```

```

Dim instance As IView
Dim value As System.String
 
value = instance.GetName2()
```

```

System.string GetName2()
```

```

System.String^ GetName2(); 
```

#### Return Value

Name of the drawing view

Remarks

This method does not return unique names for section views. Call [IView::GetUniqueName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUniqueName.md) to get the unique name of a section view.

Example

[Activate Each View On Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)  
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)  
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)  
[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)  
[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)  
[Get the Number of Lines of Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)  
[Get the Number of Lines of Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)  
[Get the Number of Lines of Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)  
[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)  
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)  
[Get Centerlines In Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::SetName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetName2.md)

# ShowNamedView2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2`

Shows the specified view.
Shows the specified view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowNamedView2( _
   ByVal VName As System.String, _
   ByVal ViewId As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim VName As System.String
Dim ViewId As System.Integer
 
instance.ShowNamedView2(VName, ViewId)
```

```

void ShowNamedView2( 
   System.string VName,
   System.int ViewId
)
```

```

void ShowNamedView2( 
   System.String^ VName,
   System.int ViewId
) 
```

#### Parameters

*VName*
:   Name of the view to display or an empty string to use ViewId instead

*ViewId*
:   ID of the view to display as defined by [swStandardViews\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html) or -1 to use the VName argument instead; if you specify both VName and ViewId, then ViewId takes precedence if the two arguments do not resolve to the same view

Remarks

To set a named view to the active view in a drawing, the drawing view that contains the named view must be selected.

To orient the selected face to its Normal To view, specify **\*Normal To** for VName and **-1** for ViewId.

Example

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)  
[Change to Isometric and Zoom to Fit View Mode (VBA)](Change_to_Isometric_and_Zoom_to_Fit_View_Mode_Example_VB.htm)  
[Create Revolve Features (VBA)](Create_Revolve_Features_Example_VB.htm)  
[Get Sketch Points in Wizard Hole (VBA)](Get_Sketch_Points_in_Wizard_Hole_Example_VB.htm)  
[Show Named View (VBA)](Show_Named_View_Example_VB.htm)  
[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)  
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)  
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::NameView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.md)  
[IModelDoc2::DeleteNamedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView.md)  
[IModelDocExtension::GetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.md)  
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.md)  
[IModelDocExtension::ResetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ResetStandardViews.md)  
[IModelDocExtension::UpdateStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateStandardViews.md)

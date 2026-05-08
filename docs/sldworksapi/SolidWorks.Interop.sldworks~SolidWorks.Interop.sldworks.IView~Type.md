# Type Property (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Type`

Gets the drawing view type.
Gets the drawing view type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Type As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.Type
```

```

System.int Type {get;}
```

```

property System.int Type {
   System.int get();
}
```

#### Property Value

Type of drawing view as defined by [swDrawingViewTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingViewTypes_e.html)

Example

[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)  
[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)  
[Get Components Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)  
[Get Section View (VBA)](Get_Section_View_Data_Example_VB.htm)  
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)  
[Put Assembly Components in Drawing View on Different Layers (VBA)](Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm)  
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)  
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)  
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)  
[Get Drawing View Names and Types (VB.NET)](Get_Drawing_View_Names_and_Types_Example_VBNET.htm)  
[Get Drawing View Names and Types (C#)](Get_Drawing_View_Names_and_Types_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)

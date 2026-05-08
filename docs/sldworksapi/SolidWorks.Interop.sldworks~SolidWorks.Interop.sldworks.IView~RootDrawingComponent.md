# RootDrawingComponent Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RootDrawingComponent`

Gets the root component for this drawing view.
Gets the root component for this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property RootDrawingComponent As DrawingComponent
```

```

Dim instance As IView
Dim value As DrawingComponent
 
value = instance.RootDrawingComponent
```

```

DrawingComponent RootDrawingComponent {get;}
```

```

property DrawingComponent^ RootDrawingComponent {
   DrawingComponent^ get();
}
```

#### Property Value

[Drawing component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)

Example

[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)  
[Get Components Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)  
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)  
[Put Assembly Components in Drawing View on Different Layers (VBA)](Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm)  
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)  
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)  
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)

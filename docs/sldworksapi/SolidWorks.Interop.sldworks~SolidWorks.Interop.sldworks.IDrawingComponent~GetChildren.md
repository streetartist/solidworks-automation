# GetChildren Method (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildren`

Gets the child components for this drawing component.
Gets the child components for this drawing component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetChildren() As System.Object
```

```

Dim instance As IDrawingComponent
Dim value As System.Object
 
value = instance.GetChildren()
```

```

System.object GetChildren()
```

```

System.Object^ GetChildren(); 
```

#### Return Value

Array of [IDrawingComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md) objects that are child components of the drawing component

Remarks

This method traverses the referenced component tree in a given view. Use [IDrawingComponent::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Visible.md) to get or set the visibility of individual components in the given view.

Example

[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)  
[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)  
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)  
[Put Assembly Components in Drawing View on Different Layers (VBA)](Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm)  
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)  
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)  
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[IDrawingComponent::GetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildrenCount.md)  
[IDrawingComponent::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~IGetChildren.md)

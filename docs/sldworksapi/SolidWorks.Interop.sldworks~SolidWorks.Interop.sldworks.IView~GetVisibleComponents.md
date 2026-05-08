# GetVisibleComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents`

Gets the visible components in this drawing view.
Gets the visible components in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleComponents() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetVisibleComponents()
```

```

System.object GetVisibleComponents()
```

```

System.Object^ GetVisibleComponents(); 
```

#### Return Value

Visible [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in this drawing view

Remarks

Visible components are components not completely obscured by other components in the view.

NOTE: This method does not retrieve a complete component object. For example, the component returned by this method does not support [IComponent2::GetBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.md) (returns null). To retrieve a visible component that fully supports [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) methods and properties, call:

1. [IView::GetVisibleDrawingComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents.md)
2. [IDrawingComponent::Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Component.md)

Example

[Get All Edges in Visible Component in Drawing View (VBA)](Get_All_Edges_in_Visible_Component_in_Drawing_View_Example_VB.htm)  
[Get All Visible Components in Drawing View (VBA)](Get_All_Visible_Components_in_Drawing_View_Example_VB.htm)  
[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.md)  
[IView::GetVisibleEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.md)  
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)  
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.md)  
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)

# LayerOverride Property (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~LayerOverride`

Gets or sets whether the drawing component has properties that override the default properties of the layer.
Gets or sets whether the drawing component has properties that override the default properties of the layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LayerOverride As System.Integer
```

```

Dim instance As IDrawingComponent
Dim value As System.Integer
 
instance.LayerOverride = value
 
value = instance.LayerOverride
```

```

System.int LayerOverride {get; set;}
```

```

property System.int LayerOverride {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Properties that have been overridden or should be overridden as defined in  [swLayerOverride\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLayerOverride_e.html) (see Remarks)

Remarks

Currently, only SOLIDWORKS drawing documents support layers.

You should set this property only when you want to reset specific visual properties to the default visual properties of the owning layer. If you want to change or set specific values for the visual property of this component, use [IDrawingComponent::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Style.md) or [IDrawingComponent::Width](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Width.md).

In drawing documents, components can be created on a layer that has specific visual properties. By default, the component takes on the visual properties defined by the layer. However, for a specific component, you can override these visual properties (style or width).

When the component is not on any layer, this property returns an undefined value. You can use [IDrawingComponent::Layer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Layer.md) to determine the name of the layer that this component is on. If an empty string is returned by this property, then this property is not used.

When you get this property, the returned bit value indicates which properties have been overridden. The bit indicators are:

- color = 0x1
- style = 0x2
- width = 0x4

Therefore, if the return value is returned as 2, then you know style has been specifically set for this component and might not match the default value associated with this component's layer.

When you set this property, the input bit value indicates which properties should maintain their current override values. Therefore, if the return value is passed as 0x4, you know width should keep its current override value and style should be reset to use the style settings for the component's layer. If you pass 0, all visual properties are reset to use the default settings of the component's layer.

Example

[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)

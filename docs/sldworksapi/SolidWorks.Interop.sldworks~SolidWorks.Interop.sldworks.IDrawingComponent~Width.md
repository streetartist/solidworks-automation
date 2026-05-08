# Width Property (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Width`

Gets or sets the width of the line for this component for this drawing view.
Gets or sets the width of the line for this component for this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Width As System.Integer
```

```

Dim instance As IDrawingComponent
Dim value As System.Integer
 
instance.Width = value
 
value = instance.Width
```

```

System.int Width {get; set;}
```

```

property System.int Width {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Line width as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

Remarks

Use [IDrawingComponent::LayerOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~LayerOverride.md) to determine if this component is using its default  
layer line width.

Example

[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[IDrawingComponent::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Style.md)  
[IDrawingComponent::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Layer.md)

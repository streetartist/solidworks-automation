# Layer Property (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Layer`

Gets or sets the name of the layer on which the component resides in the view.
Gets or sets the name of the layer on which the component resides in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layer As System.String
```

```

Dim instance As IDrawingComponent
Dim value As System.String
 
instance.Layer = value
 
value = instance.Layer
```

```

System.string Layer {get; set;}
```

```

property System.String^ Layer {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the layer on which this component resides

Remarks

|  |  |
| --- | --- |
| **If you specify...** | **Then...** |
| Empty string | Name of the component's layer is set to None or to the name of the default layer. |
| Name of an existing layer | Component is placed on that layer. |
| Name of a non-existent layer | Layer does not change. |

If the drawing component is an assembly:

- you can set the layer, and the layers of child drawing components will also be set.
- the query returns an empty string because the layer is uniquely defined in case child  
  drawing components reside on different layers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[IDrawingComponent::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Layer.md)

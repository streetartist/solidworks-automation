# Color Property (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Color`

Gets or sets the color of this sketch point.
Gets or sets the color of this sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Color As System.Integer
```

```

Dim instance As ISketchPoint
Dim value As System.Integer
 
instance.Color = value
 
value = instance.Color
```

```

System.int Color {get; set;}
```

```

property System.int Color {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

COLORREF value for this sketch point

Remarks

Only drawing documents support layers.

Sketch points can be created on a layer that has specific visual properties. The color value specified with this property overrides the layer color.

Use the [ISketchPoint::LayerOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~LayerOverride.md) to determine if this sketch point is currently using its default layer color.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Layer.md)

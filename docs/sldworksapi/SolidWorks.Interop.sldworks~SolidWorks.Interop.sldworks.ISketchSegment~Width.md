# Width Property (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Width`

Gets or sets the line width for this sketch segment.
Gets or sets the line width for this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Width As System.Integer
```

```

Dim instance As ISketchSegment
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

Line width used for this sketch segment as defined in  [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

Remarks

This property is only supported in drawing documents.

Sketch segments can be created on a layer that has specific visual properties. By default, the sketch segment takes on the visual properties defined by the layer. The line width value specified with this property overrides the default layer width.

Use the [ISketchSegment::LayerOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~LayerOverride.md) to determine if this sketch segment is currently using its default layer line width.

Example

[Get Sketch Entities with Visual Properties (VBA)](Create_Sketch_Line_with_Visual_Properties_Example_VB.htm)  
[Get Temporary Axes in Each Drawing View (VBA)](Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::Color Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Color.md)  
[ISketchSegment::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Layer.md)  
[ISketchSegment::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Style.md)

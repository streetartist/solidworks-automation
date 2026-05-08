# Layer Property (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Layer`

gets or sets the layer used by this sketch segment.
gets or sets the layer used by this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layer As System.String
```

```

Dim instance As ISketchSegment
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

Name of the layer used for this sketch segment

Remarks

Layers are only supported in drawing documents.

Sketch segments can be created on a specific layer. This property gets or sets the layer used by this sketch segment.

The return value may be an empty string because an old document may not contain layers. This also occurs if sketch segments have been generated in a new document that has no layers defined.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~LayerOverride.md)  
[ISketchSegment::Color Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Color.md)  
[ISketchSegment::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Style.md)  
[ISketchSegment::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Width.md)

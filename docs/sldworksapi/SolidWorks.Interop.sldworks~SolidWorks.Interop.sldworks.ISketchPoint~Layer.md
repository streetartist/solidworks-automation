# Layer Property (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Layer`

Gets or sets the layer for this sketch point.
Gets or sets the layer for this sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layer As System.String
```

```

Dim instance As ISketchPoint
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

Name of the layer for this sketch point

Remarks

Layers are only supported in drawing documents.

Every sketch point is on a layer. Sketch points can be created on a specific layer in drawings.

The return value may be an empty string because an older document may not contain layers. Also, this can occur if sketch points were generated in a new document that has no layers defined.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~LayerOverride.md)

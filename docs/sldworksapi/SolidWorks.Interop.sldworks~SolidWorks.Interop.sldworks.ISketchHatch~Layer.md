# Layer Property (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Layer`

Gets or sets the layer used by this sketch hatch.
Gets or sets the layer used by this sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layer As System.String
```

```

Dim instance As ISketchHatch
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

Name of the layer for this sketch hatch

Remarks

In drawing documents, sketch hatches can be created on a specific layer. Only drawing documents support layers.

The return value can be an empty string because an old document may not contain layers. This can also occur if sketch hatches have been generated in a new document  in which layers have not been defined.

Example

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md) examples.

Example

[Override Layer Color for Area Hatch (VBA)](Override_Layer_Color_for_Area_Hatch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~LayerOverride.md)

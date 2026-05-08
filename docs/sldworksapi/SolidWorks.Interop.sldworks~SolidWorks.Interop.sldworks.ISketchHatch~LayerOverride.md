# LayerOverride Property (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~LayerOverride`

Gets or sets whether the sketch hatch has properties that override the default properties of the layer.
Gets or sets whether the sketch hatch has properties that override the default properties of the layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LayerOverride As System.Integer
```

```

Dim instance As ISketchHatch
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

Properties that have been overridden or should be overridden as defined in [swLayerOverride\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLayerOverride_e.html) (see Remarks)

Remarks

Only drawing documents support layers.

Sketch hatches can be created on a layer that has specific visual properties. By default, the sketch hatches take on the visual properties defined by the layer. However, for specific sketch hatches, these visual properties can be overridden (see [ISketchHatch::Color](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Color.md)). This property gets or sets whether the default visual properties of the layer should be used by this sketch hatch.

When the sketch hatch is not on any layer, the value this property returns is undefined. You can use the [ISketchHatch::Layer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Layer.md) property to determine the name of the layer, if any, that this sketch hatch is on. If an empty string is returned by the ISketchHatch::Layer property, then this property is not used.

Sketch hatches currently support only the color visual property. Therefore, the only bit value that will currently be used by this function would be 0x1 which indicates a color override. If this property returns 0x1, this indicates that the color of this sketch hatch has been specifically set by the user and may not match the default color value associated with this sketch hatch's layer. If you pass 0 to this property, then you are indicating that the color should be reset to use the default color associated with this item's layer.

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

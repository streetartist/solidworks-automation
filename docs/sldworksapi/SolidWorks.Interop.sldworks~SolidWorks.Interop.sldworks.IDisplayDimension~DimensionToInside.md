# DimensionToInside Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DimensionToInside`

Gets or sets whether dimensions to arcs are always to the inside of the arc.
Gets or sets whether dimensions to arcs are always to the inside of the arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DimensionToInside As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.DimensionToInside = value
 
value = instance.DimensionToInside
```

```

System.bool DimensionToInside {get; set;}
```

```

property System.bool DimensionToInside {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True dimension to the inside of arc, false does not dimension to the inside of the arc

Remarks

This property applies only to radius dimensions. This property does not affect other types of dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)

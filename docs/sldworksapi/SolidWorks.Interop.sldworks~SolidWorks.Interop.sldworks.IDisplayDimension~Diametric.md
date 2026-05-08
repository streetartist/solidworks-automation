# Diametric Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Diametric`

Gets or sets whether this display dimension is radial/single distance or diameter/doubled distance.
Gets or sets whether this display dimension is radial/single distance or diameter/doubled distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Diametric As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.Diametric = value
 
value = instance.Diametric
```

```

System.bool Diametric {get; set;}
```

```

property System.bool Diametric {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the diameter/doubled distance dimension, false to display the radial/single distance dimension

Remarks

Depending on the [type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionType_e.html) of this display dimension, this property toggles between:

- radial and diameter display dimensions
- radial linear and diametric linear display dimensions

This property does not affect other types of dimensions.

Use [IModelDocExtension::AddSpecificDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.md) to create single or doubled distance display dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Example

[Change Radial to Diametric Style (VBA)](Change_Radial_to_Diametric_Style_Example_VB.htm)  
[Create Non-associative Diameter Dimension (VBA)](Create_Non-associative_Diameter_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetType.md)  
[IDisplayDimension::Type2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.md)  
[IDisplayDimension::DisplayAsLinear Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsLinear.md)

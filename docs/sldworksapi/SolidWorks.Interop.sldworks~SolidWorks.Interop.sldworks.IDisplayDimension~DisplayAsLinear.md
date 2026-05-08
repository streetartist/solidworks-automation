# DisplayAsLinear Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsLinear`

Gets or sets whether this diameter dimension is displayed as a linear dimension.
Gets or sets whether this diameter dimension is displayed as a linear dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayAsLinear As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.DisplayAsLinear = value
 
value = instance.DisplayAsLinear
```

```

System.bool DisplayAsLinear {get; set;}
```

```

property System.bool DisplayAsLinear {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays a linear dimension, false displays a diameter dimension

Remarks

This property applies only to diameter dimensions. It does not affect other types of dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::Type2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.md)  
[IDisplayDimension::Foreshortened Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Foreshortened.md)

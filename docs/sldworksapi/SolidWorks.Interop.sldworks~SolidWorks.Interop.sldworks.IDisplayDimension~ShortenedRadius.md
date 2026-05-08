# ShortenedRadius Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShortenedRadius`

Gets or sets whether to display this radius display dimension with a foreshortened radius.
Gets or sets whether to display this radius display dimension with a foreshortened radius.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShortenedRadius As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.ShortenedRadius = value
 
value = instance.ShortenedRadius
```

```

System.bool ShortenedRadius {get; set;}
```

```

property System.bool ShortenedRadius {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays a foreshortened radius, false does not display a foreshortened radius

Remarks

In certain instances, you might want to show a radius dimension where the leader goes towards the center of the arc, but stops just before reaching the center. This is commonly used when the center of the arc is beyond the bounds of a drawing, or interferes with another view. This method controls that display characteristic.

This property applies only to radius dimensions. It does not affect other types of dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)

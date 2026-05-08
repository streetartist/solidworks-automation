# Color Property (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Color`

Gets or sets the color of this annotation. Annotation color is supported only in SOLIDWORKS drawings.
Gets or sets the color of this annotation. Annotation color is supported only in SOLIDWORKS drawings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Color As System.Integer
```

```

Dim instance As IAnnotation
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

COLORREF value for the color of this annotation

Remarks

In Drawing documents, you can create annotations on a layer that has specific visual properties. The color value specified with this property overrides the layer color.

Use [IAnnotation::LayerOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LayerOverride.md) to determine whether this annotation is using its default layer color.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)

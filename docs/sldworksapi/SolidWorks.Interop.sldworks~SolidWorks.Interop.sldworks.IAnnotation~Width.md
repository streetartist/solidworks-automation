# Width Property (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Width`

Gets or sets the line width enumeration value for this annotation.
Gets or sets the line width enumeration value for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Width As System.Integer
```

```

Dim instance As IAnnotation
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

Line style as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

Remarks

Annotation width is currently supported only in SOLIDWORKS drawings.

In drawing documents, you can create annotations on a layer that has specific visual properties. By default, the annotation takes on the visual properties defined by the layer. The line width value specified with this property allows you to override the default layer width.

Use the [IAnnotation::LayerOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LayerOverride.md) to determine if this annotation is using its default layer line width.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)

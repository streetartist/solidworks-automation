# Specular Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Specular`

Gets or sets the intensity of the light surface for illuminating the appearance.
Gets or sets the intensity of the light surface for illuminating the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Specular As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Specular = value
 
value = instance.Specular
```

```

System.double Specular {get; set;}
```

```

property System.double Specular {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Intensity of the light surface

Remarks

This property depends on the position of the light source and the position of the viewer. Increasing Specular makes the material appear shinier.

[IRenderMaterial::SpecularColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SpecularColor.md) must not be black, and at least one light other than an ambient light must be illuminating the model.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

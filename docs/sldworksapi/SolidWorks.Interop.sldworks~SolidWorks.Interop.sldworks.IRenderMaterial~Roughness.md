# Roughness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Roughness`

Gets or sets the specular spread (roughness) of the appearance.
Gets or sets the specular spread (roughness) of the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Roughness As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Roughness = value
 
value = instance.Roughness
```

```

System.double Roughness {get; set;}
```

```

property System.double Roughness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Specular spread

Remarks

This property controls the size of any highlights on a surface. It is also known as the specular exponent. Increasing Roughness makes highlights larger and softer.

The [specular](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Specular.md) value must not be zero, the [specular color](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SpecularColor.md) must not be black, and at least one light other than an ambient light must be illuminating the model.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

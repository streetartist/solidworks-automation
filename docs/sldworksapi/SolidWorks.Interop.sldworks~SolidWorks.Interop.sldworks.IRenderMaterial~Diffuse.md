# Diffuse Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Diffuse`

Gets or sets the intensity of a light source illuminating a surface from all directions without attenuation or shadowing for this appearance.
Gets or sets the intensity of a light source illuminating a surface from all directions without attenuation or shadowing for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Diffuse As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Diffuse = value
 
value = instance.Diffuse
```

```

System.double Diffuse {get; set;}
```

```

property System.double Diffuse {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Intensity of a light source illuminating a surface from all directions without attenuation or shadowing

Remarks

The appearance should contain an ambient light.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

# Translucency Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Translucency`

Gets or sets the degree to which the material is able to filter and diffuse light for illuminating the appearance.
Gets or sets the degree to which the material is able to filter and diffuse light for illuminating the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Translucency As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Translucency = value
 
value = instance.Translucency
```

```

System.double Translucency {get; set;}
```

```

property System.double Translucency {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Degree to which the material is able to filter and diffuse light

Remarks

Increasing Translucency gives the material more backlighting.

A light must be behind the model relative to the position of the viewer.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

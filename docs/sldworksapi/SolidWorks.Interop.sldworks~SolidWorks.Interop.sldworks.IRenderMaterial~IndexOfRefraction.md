# IndexOfRefraction Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IndexOfRefraction`

Gets or sets the index of refraction for illuminating this appearance.
Gets or sets the index of refraction for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IndexOfRefraction As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.IndexOfRefraction = value
 
value = instance.IndexOfRefraction
```

```

System.double IndexOfRefraction {get; set;}
```

```

property System.double IndexOfRefraction {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Index of refraction

Remarks

This property controls the bending of light as it passes through a transparent object. Although actually dependent on the ratio of indices between the transparent material entered and the material exited, in practice, the higher the index of refraction, the more the light is bent. Typical values are 1.0 for air, 1.33 for water, and 1.44 for glass.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

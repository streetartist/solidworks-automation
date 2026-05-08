# BumpScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpScale`

Gets or sets the scale for the surface-finish pattern incidence for this appearance.
Gets or sets the scale for the surface-finish pattern incidence for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpScale As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.BumpScale = value
 
value = instance.BumpScale
```

```

System.double BumpScale {get; set;}
```

```

property System.double BumpScale {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Scale

Remarks

Scale controls the pattern of surface finish elements. A higher scale decreases the pattern incidence, and a lower scale increases the incidence of pattern elements.

Scale if more pronounced for low [amplitude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpAmplitude.md) values. [Radius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpRadius.md) also affects the pattern incidence for dimpled surface finishes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

# AnisotropicCylinderDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AnisotropicCylinderDistance`

Gets or sets the anisotropic cylinder distance for illuminating this appearance.
Gets or sets the anisotropic cylinder distance for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AnisotropicCylinderDistance As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.AnisotropicCylinderDistance = value
 
value = instance.AnisotropicCylinderDistance
```

```

System.double AnisotropicCylinderDistance {get; set;}
```

```

property System.double AnisotropicCylinderDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Anisotropic cylinder distance

Remarks

The anisotropic reflection is modeled by laying (virtual) cylinders along the surface. This property controls the distance between the cylinders. For stronger anisotropic effect, increase the cylinder distance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

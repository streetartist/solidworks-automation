# AnisotropicFloorHeight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AnisotropicFloorHeight`

Gets or sets the anisotropic floor height for illuminating this appearance.
Gets or sets the anisotropic floor height for illuminating this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AnisotropicFloorHeight As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.AnisotropicFloorHeight = value
 
value = instance.AnisotropicFloorHeight
```

```

System.double AnisotropicFloorHeight {get; set;}
```

```

property System.double AnisotropicFloorHeight {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Anisotropic floor height

Remarks

Anisotropic reflection is modeled by laying (virtual) cylinders along the surface. This property controls the height difference between neighboring cylinders. For a stronger anisotropic effect, decease the floor height.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

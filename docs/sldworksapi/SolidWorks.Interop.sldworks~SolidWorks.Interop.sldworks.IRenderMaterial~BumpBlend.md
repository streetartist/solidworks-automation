# BumpBlend Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpBlend`

Gets or sets the blend, which is the extent of the boundary between each bump and the surface, of the surface finish for this appearance.
Gets or sets the blend, which is the extent of the boundary between each bump and the surface, of the surface finish for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpBlend As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.BumpBlend = value
 
value = instance.BumpBlend
```

```

System.double BumpBlend {get; set;}
```

```

property System.double BumpBlend {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Extent of the boundary between each bump and the surface

Remarks

This property supports dimpled, tread plate, and knurled styles of surface finishes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

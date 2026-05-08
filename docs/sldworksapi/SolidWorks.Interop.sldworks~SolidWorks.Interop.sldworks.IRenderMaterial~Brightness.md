# Brightness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Brightness`

Gets or sets how emissive the material is for the Constant illumination type for this appearance.
Gets or sets how emissive the material is for the Constant illumination type for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Brightness As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Brightness = value
 
value = instance.Brightness
```

```

System.double Brightness {get; set;}
```

```

property System.double Brightness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Brightness

Remarks

This property corresponds to the Brightness control on the Illumination tab of the Appearances PropertyManager page when Illumination is Constant.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

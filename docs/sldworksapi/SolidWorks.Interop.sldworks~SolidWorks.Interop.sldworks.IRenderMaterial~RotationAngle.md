# RotationAngle Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RotationAngle`

Gets or sets the angle by which to rotate the texture relative to the axes for mapping this appearance.
Gets or sets the angle by which to rotate the texture relative to the axes for mapping this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationAngle As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.RotationAngle = value
 
value = instance.RotationAngle
```

```

System.double RotationAngle {get; set;}
```

```

property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle by which to rotate the texture relative to the axes

Remarks

This property is only valid when either a spherical or cylindrical [mapping type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MappingType.md) is selected.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

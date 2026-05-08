# Direction1RotationAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Direction1RotationAngle`

Gets or sets the angle at which to rotate the texture relative to the horizontal axis for mapping this appearance.
Gets or sets the angle at which to rotate the texture relative to the horizontal axis for mapping this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Direction1RotationAngle As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Direction1RotationAngle = value
 
value = instance.Direction1RotationAngle
```

```

System.double Direction1RotationAngle {get; set;}
```

```

property System.double Direction1RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle at which to rotate the texture to the horizontal axis

Remarks

This property affects spheres only.

Call [IRenderMaterial::Direction2RotationAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Direction2RotationAngle.md) to get or set the angle to rotate the texture to the vertical axis.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)

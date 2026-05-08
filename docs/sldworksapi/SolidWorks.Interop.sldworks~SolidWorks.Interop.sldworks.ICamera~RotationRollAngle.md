# RotationRollAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle`

Gets or sets the camera's roll angle.
Gets or sets the camera's roll angle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationRollAngle As System.Double
```

```

Dim instance As ICamera
Dim value As System.Double
 
instance.RotationRollAngle = value
 
value = instance.RotationRollAngle
```

```

System.double RotationRollAngle {get; set;}
```

```

property System.double RotationRollAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Roll angle for camera

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::RotationRollBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.md)  
[ICamera::RotationRollEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.md)  
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.md)

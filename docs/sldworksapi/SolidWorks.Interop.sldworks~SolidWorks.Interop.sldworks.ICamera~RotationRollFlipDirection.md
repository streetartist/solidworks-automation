# RotationRollFlipDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection`

Gets or sets whether to flip the direction of the camera 180.
Gets or sets whether to flip the direction of the camera 180.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationRollFlipDirection As System.Boolean
```

```

Dim instance As ICamera
Dim value As System.Boolean
 
instance.RotationRollFlipDirection = value
 
value = instance.RotationRollFlipDirection
```

```

System.bool RotationRollFlipDirection {get; set;}
```

```

property System.bool RotationRollFlipDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the direction of the camera 180, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::RotationRollAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.md)  
[ICamera::RotationRollBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.md)  
[ICamera::RotationRollEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.md)

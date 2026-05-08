# RotationRollBySelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection`

Gets or sets whether you can select the camera's rotation roll direction.
Gets or sets whether you can select the camera's rotation roll direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationRollBySelection As System.Boolean
```

```

Dim instance As ICamera
Dim value As System.Boolean
 
instance.RotationRollBySelection = value
 
value = instance.RotationRollBySelection
```

```

System.bool RotationRollBySelection {get; set;}
```

```

property System.bool RotationRollBySelection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if you can select the camera's rotation roll, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::RotationRollAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.md)  
[ICamera::RotationRollEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.md)  
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.md)

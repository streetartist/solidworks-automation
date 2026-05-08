# RotationRollEntity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity`

Gets or sets the entity (line, edge, face, or plane) that defines the camera's rotation up direction.
Gets or sets the entity (line, edge, face, or plane) that defines the camera's rotation up direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationRollEntity As System.Object
```

```

Dim instance As ICamera
Dim value As System.Object
 
instance.RotationRollEntity = value
 
value = instance.RotationRollEntity
```

```

System.object RotationRollEntity {get; set;}
```

```

property System.Object^ RotationRollEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pointer to the entity (line, edge, face, or plane) that defines the camera's rotation up direction

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::RotationRollAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.md)  
[ICamera::RotationRollBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.md)  
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.md)

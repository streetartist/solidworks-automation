# LockCameraPosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition`

Gets or sets whether the camera position is locked.
Gets or sets whether the camera position is locked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LockCameraPosition As System.Boolean
```

```

Dim instance As ICamera
Dim value As System.Boolean
 
instance.LockCameraPosition = value
 
value = instance.LockCameraPosition
```

```

System.bool LockCameraPosition {get; set;}
```

```

property System.bool LockCameraPosition {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if camera position is locked, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.md)  
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.md)  
[ICamera::GetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.md)  
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.md)  
[ICamera::SetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.md)  
[ICamera::SetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.md)  
[ICamera::SetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.md)  
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.md)

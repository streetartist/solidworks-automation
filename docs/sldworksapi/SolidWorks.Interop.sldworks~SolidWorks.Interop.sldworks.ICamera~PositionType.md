# PositionType Property (ICamera)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType`

Gets or sets the camera position type.
Gets or sets the camera position type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PositionType As System.Integer
```

```

Dim instance As ICamera
Dim value As System.Integer
 
instance.PositionType = value
 
value = instance.PositionType
```

```

System.int PositionType {get; set;}
```

```

property System.int PositionType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Camera position type as defined in [swCameraPositionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCameraPositionType_e.html).

Example

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

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
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.md)

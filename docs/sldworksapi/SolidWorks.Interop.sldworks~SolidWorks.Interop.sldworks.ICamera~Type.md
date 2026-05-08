# Type Property (ICamera)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Type`

Gets or sets the type of camera.
Gets or sets the type of camera.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Type As System.Integer
```

```

Dim instance As ICamera
Dim value As System.Integer
 
instance.Type = value
 
value = instance.Type
```

```

System.int Type {get; set;}
```

```

property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of camera as defined in [swCameraType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCameraType_e.html)

Example

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)  
[Turn Cameras On and Off (VB.NET)](Turn_Cameras_On_and_Off_Example_VBNET.htm)  
[Turn Cameras On and Off (C#)](Turn_Cameras_On_and_Off_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::TargetPointPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.md)  
[ICamera::TargetPointBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.md)  
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.md)  
[ICamera::SetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.md)  
[ICamera::GetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.md)

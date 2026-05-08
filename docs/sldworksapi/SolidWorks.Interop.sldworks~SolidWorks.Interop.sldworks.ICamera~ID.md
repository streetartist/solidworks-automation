# ID Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~ID`

Gets the ID for this camera.
Gets the ID for this camera.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ID As System.Integer
```

```

Dim instance As ICamera
Dim value As System.Integer
 
value = instance.ID
```

```

System.int ID {get;}
```

```

property System.int ID {
   System.int get();
}
```

#### Property Value

ID for camera

Example

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)  
[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)  
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)  
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[IModelDocExtension::GetCameraById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraById.md)

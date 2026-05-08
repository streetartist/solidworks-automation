# GetCameraById Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraById`

Gets a camera using the specified camera ID.
Gets a camera using the specified camera ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCameraById( _
   ByVal CameraId As System.Integer _
) As Camera
```

```

Dim instance As IModelDocExtension
Dim CameraId As System.Integer
Dim value As Camera
 
value = instance.GetCameraById(CameraId)
```

```

Camera GetCameraById( 
   System.int CameraId
)
```

```

Camera^ GetCameraById( 
   System.int CameraId
) 
```

#### Parameters

*CameraId*
:   Camera ID (see **Remarks**)

#### Return Value

[Camera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)

Remarks

A valid ID is 0 <= ID <= ([IModelDocExtension::GetCameraCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraCount.md) -1).

CameraId is reassigned if there are multiple cameras and one of those cameras is deleted. For example:

|  |  |
| --- | --- |
| If... | And Camera2 is deleted, then... |
| CameraId = 1 for Camera1 | CameraId = 1 for Camera1 |
| CameraId = 2 for Camera2 | Deleted |
| CameraId = 3 for Camera3 | CameraId = 2 for Camera3 |

Example

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ICamera::GetCameraDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraDefinition.md)  
[IModelDocExtension::InsertCamera Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertCamera.md)

# SetCameraByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetCameraByName`

Sets the model view to that of the specified camera, if in camera view mode.
Sets the model view to that of the specified camera, if in camera view mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCameraByName( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IModelView
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SetCameraByName(Name)
```

```

System.bool SetCameraByName( 
   System.string Name
)
```

```

System.bool SetCameraByName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Feature name of the camera to use to set the model view, if in camera view mode

#### Return Value

True if the camera is set, false if not

Remarks

|  |  |
| --- | --- |
| If you specify ... | Then... |
| A nonexistent camera when another camera view is active | Return value is false and the other camera view remains active |
| An empty string when another camera view is active | Return value is True and the camera view is turned off for this model view |

Example

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::Camera Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Camera.md)

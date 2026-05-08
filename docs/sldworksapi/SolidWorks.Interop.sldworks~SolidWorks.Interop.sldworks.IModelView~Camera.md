# Camera Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Camera`

Gets or sets the camera.
Gets or sets the camera.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Camera As Camera
```

```

Dim instance As IModelView
Dim value As Camera
 
instance.Camera = value
 
value = instance.Camera
```

```

Camera Camera {get; set;}
```

```

property Camera^ Camera {
   Camera^ get();
   void set (    Camera^ value);
}
```

#### Property Value

[Camera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)

Remarks

If the return value is Nothing or NULL, then the camera view for this model is turned off.

Example

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::SetCameraByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetCameraByName.md)

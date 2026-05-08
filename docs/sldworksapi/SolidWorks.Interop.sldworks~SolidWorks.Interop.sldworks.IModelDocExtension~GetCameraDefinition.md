# GetCameraDefinition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraDefinition`

Gets a camera, but does not add the newly created camera to the model.
Gets a camera, but does not add the newly created camera to the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCameraDefinition() As Camera
```

```

Dim instance As IModelDocExtension
Dim value As Camera
 
value = instance.GetCameraDefinition()
```

```

Camera GetCameraDefinition()
```

```

Camera^ GetCameraDefinition(); 
```

Remarks

The model is unchanged.

You should find this method helpful when developing a renderer add-in.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::InsertCamera Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertCamera.md)  
[IModelDocExtension::GetCameraById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraById.md)  
[IModelDocExtension::GetCameraCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraCount.md)

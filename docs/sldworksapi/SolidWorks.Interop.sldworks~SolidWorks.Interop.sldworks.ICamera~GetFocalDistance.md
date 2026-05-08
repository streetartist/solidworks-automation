# GetFocalDistance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetFocalDistance`

Gets the camera's focal distance.
Gets the camera's focal distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFocalDistance() As System.Double
```

```

Dim instance As ICamera
Dim value As System.Double
 
value = instance.GetFocalDistance()
```

```

System.double GetFocalDistance()
```

```

System.double GetFocalDistance(); 
```

#### Return Value

Camera's focal distance

Remarks

If the camera is locked to a reference, then the return value might be different than the numeric value shown in the Camera PropertyManager.

Example

[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)  
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)  
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)

# GetUpVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetUpVector`

Gets the camera's up direction.
Gets the camera's up direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUpVector() As MathVector
```

```

Dim instance As ICamera
Dim value As MathVector
 
value = instance.GetUpVector()
```

```

MathVector GetUpVector()
```

```

MathVector^ GetUpVector(); 
```

#### Return Value

Point to [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::GetViewVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetViewVector.md)

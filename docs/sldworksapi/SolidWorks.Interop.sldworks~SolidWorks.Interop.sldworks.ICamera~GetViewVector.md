# GetViewVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetViewVector`

Gets the direction in which the camera is looking.
Gets the direction in which the camera is looking.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetViewVector() As MathVector
```

```

Dim instance As ICamera
Dim value As MathVector
 
value = instance.GetViewVector()
```

```

MathVector GetViewVector()
```

```

MathVector^ GetViewVector(); 
```

#### Return Value

Pointer to [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object

Remarks

Most of the time, the return value is the vector from the camera position to the target, normalized.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::GetUpVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetUpVector.md)

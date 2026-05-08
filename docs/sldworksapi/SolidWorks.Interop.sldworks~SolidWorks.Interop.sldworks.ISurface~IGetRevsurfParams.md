# IGetRevsurfParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetRevsurfParams`

Gets the parameters for the surface.
Gets the parameters for the surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRevsurfParams() As System.Double
```

```

Dim instance As ISurface
Dim value As System.Double
 
value = instance.IGetRevsurfParams()
```

```

System.double IGetRevsurfParams()
```

```

System.double IGetRevsurfParams(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

A surface of revolution is constructed by revolving a profile curve (line or arc or b-spline) about an axis. The profile curve for the surface of revolution can be retrieved with [ISurface::GetProfileCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProfileCurve.md) or [ISurface::IGetProfileCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetProfileCurve.md).

Eight doubles of parameters returned.

- Point [3] -  X, Y, Z coordinates of the start point of the axis of rotation.
- AxisDir[3] -  Vector showing the direction of the axis of rotation.
- Params[2] -  Parameter range of the part of the profile curve that was used to create the surface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::GetRevsurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetRevsurfParams.md)

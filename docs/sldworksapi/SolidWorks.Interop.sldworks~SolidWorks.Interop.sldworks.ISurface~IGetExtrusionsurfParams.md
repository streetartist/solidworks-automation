# IGetExtrusionsurfParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetExtrusionsurfParams`

Gets the parameters for the extrusion surface.
Gets the parameters for the extrusion surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetExtrusionsurfParams() As System.Double
```

```

Dim instance As ISurface
Dim value As System.Double
 
value = instance.IGetExtrusionsurfParams()
```

```

System.double IGetExtrusionsurfParams()
```

```

System.double IGetExtrusionsurfParams(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles giving extrusion surface parameters

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

An extrusion surface is constructed by extruding a profile curve (line or arc or b-spline) along a direction vector. You can retrieve the profile curve for the extrusion using [ISurface::GetProfileCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProfileCurve.md) or [ISurface::IGetProfileCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetProfileCurve.md).

Three doubles of parameters returned, *DirectionVector[3]*, which is the direction vector along which the profile curve is extruded.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::GetExtrusionsurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetExtrusionsurfParams.md)

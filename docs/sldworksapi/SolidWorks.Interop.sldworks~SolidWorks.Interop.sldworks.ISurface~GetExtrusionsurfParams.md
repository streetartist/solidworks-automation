# GetExtrusionsurfParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetExtrusionsurfParams`

Gets the parameters for the extrusion surface.
Gets the parameters for the extrusion surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExtrusionsurfParams() As System.Object
```

```

Dim instance As ISurface
Dim value As System.Object
 
value = instance.GetExtrusionsurfParams()
```

```

System.object GetExtrusionsurfParams()
```

```

System.Object^ GetExtrusionsurfParams(); 
```

#### Return Value

Array of doubles giving extrusion surface parameters

Remarks

An extrusion surface is constructed by extruding a profile curve (line or arc or b-spline) along a direction vector. You can retrieve the profile curve for the extrusion using [ISurface::GetProfileCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProfileCurve.md) or [ISurface::IGetProfileCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetProfileCurve.md).

Three doubles of parameters returned, *DirectionVector[3]*, which is the direction vector along which the profile curve is extruded.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IGetExtrusionsurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetExtrusionsurfParams.md)

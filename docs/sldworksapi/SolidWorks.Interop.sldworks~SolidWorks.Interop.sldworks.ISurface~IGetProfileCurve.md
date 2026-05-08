# IGetProfileCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetProfileCurve`

Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface.
Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetProfileCurve() As Curve
```

```

Dim instance As ISurface
Dim value As Curve
 
value = instance.IGetProfileCurve()
```

```

Curve IGetProfileCurve()
```

```

Curve^ IGetProfileCurve(); 
```

#### Return Value

Profile [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) used to create the surface of revolution or extrusion surface

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::GetProfileCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProfileCurve.md)

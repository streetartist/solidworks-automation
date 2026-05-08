# ICreateNewCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateNewCurve`

Creates a new empty curve for the part.
Creates a new empty curve for the part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateNewCurve() As Curve
```

```

Dim instance As ISurface
Dim value As Curve
 
value = instance.ICreateNewCurve()
```

```

Curve ICreateNewCurve()
```

```

Curve^ ICreateNewCurve(); 
```

#### Return Value

Newly created [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

The intention is that with a handle on such (initially empty) curves, appropriate construction can be called that eventually amounts to non-trivial objects.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::CreateNewCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateNewCurve.md)  
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.md)  
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md)  
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.md)  
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md)  
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md)

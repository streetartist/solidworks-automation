# IMakeIsoCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve`

Creates a curve that represents the ISO line of a given surface.
Creates a curve that represents the ISO line of a given surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMakeIsoCurve( _
   ByVal UorV As System.Boolean, _
   ByVal UvValue As System.Double _
) As Curve
```

```

Dim instance As ISurface
Dim UorV As System.Boolean
Dim UvValue As System.Double
Dim value As Curve
 
value = instance.IMakeIsoCurve(UorV, UvValue)
```

```

Curve IMakeIsoCurve( 
   System.bool UorV,
   System.double UvValue
)
```

```

Curve^ IMakeIsoCurve( 
   System.bool UorV,
   System.double UvValue
) 
```

#### Parameters

*UorV*
:   True to specify V, false to specify U

*UvValue*
:   U or V vertex or point that specifies the intersection of two curves

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.md)  
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.md)  
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md)  
[ISurface::IGetMakeIsoCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.md)

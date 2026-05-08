# ProjectCurveOnSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ProjectCurveOnSurface`

Projects a curve on a surface.
Projects a curve on a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ProjectCurveOnSurface( _
   ByVal CurveIn As Curve, _
   ByVal SurfaceIn As Surface, _
   ByVal ProjDir As MathVector _
) As Curve
```

```

Dim instance As IModeler
Dim CurveIn As Curve
Dim SurfaceIn As Surface
Dim ProjDir As MathVector
Dim value As Curve
 
value = instance.ProjectCurveOnSurface(CurveIn, SurfaceIn, ProjDir)
```

```

Curve ProjectCurveOnSurface( 
   Curve CurveIn,
   Surface SurfaceIn,
   MathVector ProjDir
)
```

```

Curve^ ProjectCurveOnSurface( 
   Curve^ CurveIn,
   Surface^ SurfaceIn,
   MathVector^ ProjDir
) 
```

#### Parameters

*CurveIn*
:   [Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) to project

*SurfaceIn*
:   [Surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) on which to project curve

*ProjDir*
:   [Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) which to project curve

#### Return Value

Projected [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

This method does not support non-spline curves. You must convert any non-spline input curves to splines before using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.md)  
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md)  
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.md)

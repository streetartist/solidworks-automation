# IMakeIsoCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves`

Creates curves on a surface.
Creates curves on a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMakeIsoCurves( _
   ByRef UvRange As System.Double, _
   ByRef Dir As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Tol As System.Double, _
   ByVal CurveCount As System.Integer, _
   ByRef Curves As Curve, _
   ByRef CurveBounds As System.Double _
) As System.Boolean
```

```

Dim instance As ISurface
Dim UvRange As System.Double
Dim Dir As System.Double
Dim Angle As System.Double
Dim Tol As System.Double
Dim CurveCount As System.Integer
Dim Curves As Curve
Dim CurveBounds As System.Double
Dim value As System.Boolean
 
value = instance.IMakeIsoCurves(UvRange, Dir, Angle, Tol, CurveCount, Curves, CurveBounds)
```

```

System.bool IMakeIsoCurves( 
   ref System.double UvRange,
   ref System.double Dir,
   System.double Angle,
   System.double Tol,
   System.int CurveCount,
   out Curve Curves,
   out System.double CurveBounds
)
```

```

System.bool IMakeIsoCurves( 
   System.double% UvRange,
   System.double% Dir,
   System.double Angle,
   System.double Tol,
   System.int CurveCount,
   [Out] Curve^ Curves,
   [Out] System.double CurveBounds
) 
```

#### Parameters

*UvRange*
:   Array of 4 doubles indicating the range of the surface to use (see **Remarks**)

*Dir*
:   Array of 3 doubles indicating the direction of projection on the surface (see Remarks)

*Angle*
:   Angle relative to dir where to create the curves

*Tol*
:   Tolerance of the curves

*CurveCount*
:   Number of curves to create (see Remarks)

*Curves*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) of size CurveCount

*CurveBounds*
:   Array of doubles of size 2\*Curves indicating the parametric bounds of the curve

#### Return Value

True if curves are created on the surface, false if not

Remarks

The UvRange argument is an array of 4 doubles indicating the minimum and maximum U and V values:

[ u\_min, u\_max, v\_min, v\_max ]

The dir argument is an array of 3 doubles representing the unit vector:

[ x, y, z ]

Before calling this method, call [ISurface::IGetMakeIsoCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.md)  
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.md)  
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.md)

# MakeIsoCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves`

Creates curves on a surface.
Creates curves on a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeIsoCurves( _
   ByVal UvRange As System.Object, _
   ByVal Dir As System.Object, _
   ByVal Angle As System.Double, _
   ByVal Tol As System.Double, _
   ByRef Curves As System.Object, _
   ByRef CurveBounds As System.Object _
) As System.Boolean
```

```

Dim instance As ISurface
Dim UvRange As System.Object
Dim Dir As System.Object
Dim Angle As System.Double
Dim Tol As System.Double
Dim Curves As System.Object
Dim CurveBounds As System.Object
Dim value As System.Boolean
 
value = instance.MakeIsoCurves(UvRange, Dir, Angle, Tol, Curves, CurveBounds)
```

```

System.bool MakeIsoCurves( 
   System.object UvRange,
   System.object Dir,
   System.double Angle,
   System.double Tol,
   out System.object Curves,
   out System.object CurveBounds
)
```

```

System.bool MakeIsoCurves( 
   System.Object^ UvRange,
   System.Object^ Dir,
   System.double Angle,
   System.double Tol,
   [Out] System.Object^ Curves,
   [Out] System.Object^ CurveBounds
) 
```

#### Parameters

*UvRange*
:   Array of 4 doubles indicating the range of the surface to use (see Remarks)

*Dir*
:   Array of 3 doubles indicating the direction of projection on the surface (see Remarks)

*Angle*
:   Angle relative to Dir where to create the curves

*Tol*
:   Tolerance of the curves

*Curves*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*CurveBounds*
:   Array of doubles of size 2\*Curves indicating the parametric bounds of the curve

#### Return Value

True if the curves are created on the surface, false if not

Remarks

The uvRange argument is an array of 4 doubles indicating the minimum and maximum U and V values:

[ u\_min, u\_max, v\_min, v\_max ]

The dir argument is an array of 3 doubles representing the unit vector:

[ x, y, z ]

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md)  
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.md)  
[ISurface::IGetMakeIsoCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.md)  
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.md)

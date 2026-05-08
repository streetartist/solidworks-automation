# IGetMakeIsoCurvesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount`

Gets the number of curves that represent the ISO line of a given direction.
Gets the number of curves that represent the ISO line of a given direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMakeIsoCurvesCount( _
   ByRef UvRange As System.Double, _
   ByRef Dir As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Tol As System.Double _
) As System.Integer
```

```

Dim instance As ISurface
Dim UvRange As System.Double
Dim Dir As System.Double
Dim Angle As System.Double
Dim Tol As System.Double
Dim value As System.Integer
 
value = instance.IGetMakeIsoCurvesCount(UvRange, Dir, Angle, Tol)
```

```

System.int IGetMakeIsoCurvesCount( 
   ref System.double UvRange,
   ref System.double Dir,
   System.double Angle,
   System.double Tol
)
```

```

System.int IGetMakeIsoCurvesCount( 
   System.double% UvRange,
   System.double% Dir,
   System.double Angle,
   System.double Tol
) 
```

#### Parameters

*UvRange*
:   Array of 4 doubles indicating the range of surface to use (see **Remarks**)

*Dir*
:   Array of 3 doubles indicating the direction of the projection on the surface (see  
    Remarks)

*Angle*
:   Angle relative to Dir where to create the curves

*Tol*
:   Tolerance of the curves to create

#### Return Value

Number of curves to create

Remarks

The uvRange argument is an array of 4 doubles indicating the minimum and maximum U and V values:

> [ u\_min, u\_max, v\_min, v\_max ]

The dir argument is an array of 3 doubles representing the unit vector:

> [ x, y, z ]

Call this method before calling [ISurface::IMakeIsoCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.md)  
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.md)  
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.md)

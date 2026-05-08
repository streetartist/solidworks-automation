# GetIntersectCurveCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount2`

Gets the number of points for a surface-curve intersection.
Gets the number of points for a surface-curve intersection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersectCurveCount2( _
   ByVal OtherCurve As Curve, _
   ByRef CurveBound As System.Double _
) As System.Integer
```

```

Dim instance As ISurface
Dim OtherCurve As Curve
Dim CurveBound As System.Double
Dim value As System.Integer
 
value = instance.GetIntersectCurveCount2(OtherCurve, CurveBound)
```

```

System.int GetIntersectCurveCount2( 
   Curve OtherCurve,
   ref System.double CurveBound
)
```

```

System.int GetIntersectCurveCount2( 
   Curve^ OtherCurve,
   System.double% CurveBound
) 
```

#### Parameters

*OtherCurve*
:   [Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*CurveBound*
:   Array of 6 doubles representing the start and end points of the curve

#### Return Value

Number of points

Remarks

Visual Basic and C++ Dispatch applications should use [ISurface::IntersectCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.md) instead of this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IIntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.md)

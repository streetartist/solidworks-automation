# IIntersectCurve2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2`

Gets a surface-curve intersection.
Gets a surface-curve intersection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IIntersectCurve2( _
   ByVal OtherCurve As Curve, _
   ByRef CurveBound As System.Double, _
   ByVal PointCount As System.Integer, _
   ByRef PointArray As System.Double, _
   ByRef TArray As System.Double, _
   ByRef UvArray As System.Double _
) As System.Boolean
```

```

Dim instance As ISurface
Dim OtherCurve As Curve
Dim CurveBound As System.Double
Dim PointCount As System.Integer
Dim PointArray As System.Double
Dim TArray As System.Double
Dim UvArray As System.Double
Dim value As System.Boolean
 
value = instance.IIntersectCurve2(OtherCurve, CurveBound, PointCount, PointArray, TArray, UvArray)
```

```

System.bool IIntersectCurve2( 
   Curve OtherCurve,
   ref System.double CurveBound,
   System.int PointCount,
   out System.double PointArray,
   out System.double TArray,
   out System.double UvArray
)
```

```

System.bool IIntersectCurve2( 
   Curve^ OtherCurve,
   System.double% CurveBound,
   System.int PointCount,
   [Out] System.double PointArray,
   [Out] System.double TArray,
   [Out] System.double UvArray
) 
```

#### Parameters

*OtherCurve*
:   [Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*CurveBound*
:   Array of 6 doubles representing the start and end points of the curve

*PointCount*
:   Number of points

*PointArray*
:   Array of points of size PointCount\*3

*TArray*
:   Array of parameters on curve  of size PointCount

*UvArray*
:   Array of parameters on surface of size PointCount\*2

#### Return Value

True if getting the intersection succeeded, false if not

Remarks

The curves must be bounded.

Before calling this method, call [ISurface::GetIntersectCurveCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount2.md) to get the number of points for this surface-curve intersection.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectCurve2.md)

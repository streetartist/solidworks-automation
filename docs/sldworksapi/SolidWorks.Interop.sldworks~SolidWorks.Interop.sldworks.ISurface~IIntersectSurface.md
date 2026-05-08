# IIntersectSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectSurface`

Gets a surface-surface intersection.
Gets a surface-surface intersection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IIntersectSurface( _
   ByVal OtherSurf As Surface, _
   ByVal CurveCount As System.Integer, _
   ByRef CurveArray As Curve, _
   ByRef BoundsArray As System.Double _
) As System.Boolean
```

```

Dim instance As ISurface
Dim OtherSurf As Surface
Dim CurveCount As System.Integer
Dim CurveArray As Curve
Dim BoundsArray As System.Double
Dim value As System.Boolean
 
value = instance.IIntersectSurface(OtherSurf, CurveCount, CurveArray, BoundsArray)
```

```

System.bool IIntersectSurface( 
   Surface OtherSurf,
   System.int CurveCount,
   out Curve CurveArray,
   out System.double BoundsArray
)
```

```

System.bool IIntersectSurface( 
   Surface^ OtherSurf,
   System.int CurveCount,
   [Out] Curve^ CurveArray,
   [Out] System.double BoundsArray
) 
```

#### Parameters

*OtherSurf*
:   Intersecting [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

*CurveCount*
:   Number of curves

*CurveArray*
:   Array of curves of size CurveCount

*BoundsArray*
:   Array of [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) bounds of size CurveCount\*2

#### Return Value

True if successful, false if not

Remarks

Before calling this method, call [ISurface::GetIntersectSurfaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectSurfaceCount.md) to get the curve count for this surface-surface intersection.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectSurface.md)

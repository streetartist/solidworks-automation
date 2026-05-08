# GetBSurfParams2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams2`

Obsolete. Superseded by ISurface::GetBSurfParams3.
Obsolete. Superseded by [ISurface::GetBSurfParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBSurfParams2( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNonRational As System.Boolean, _
   ByVal VP0 As System.Object, _
   ByVal Tolerance As System.Double, _
   ByRef Sense As System.Boolean _
) As System.Object
```

```

Dim instance As ISurface
Dim WantCubic As System.Boolean
Dim WantNonRational As System.Boolean
Dim VP0 As System.Object
Dim Tolerance As System.Double
Dim Sense As System.Boolean
Dim value As System.Object
 
value = instance.GetBSurfParams2(WantCubic, WantNonRational, VP0, Tolerance, Sense)
```

```

System.object GetBSurfParams2( 
   System.bool WantCubic,
   System.bool WantNonRational,
   System.object VP0,
   System.double Tolerance,
   out System.bool Sense
)
```

```

System.Object^ GetBSurfParams2( 
   System.bool WantCubic,
   System.bool WantNonRational,
   System.Object^ VP0,
   System.double Tolerance,
   [Out] System.bool Sense
) 
```

#### Parameters

*WantCubic*
:   True if cubic is needed, false if not; specifying true converts any surface type to a cubic Bsurface

*WantNonRational*
:   True if non-rational is needed, false if not; specifying true converts any surface type to a non-rational Bsurface; if you specify true, then you should only use this method for surfaces that are Bsurface or blend surface; otherwise, the underlying call is not made and the values returned from this are not initialized or contain the values from the last call

*VP0*
:   Array of values describing the UV range of the surface to be output; you can obtain these values by using [ISurface::Parameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md) or [ISurface::IParameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md)

*Tolerance*
:   Tolerance, in meters, between the approximated b-spline surface and the underlying surface; the default value is 0.01 and should generally be reduced to the tolerance desired

*Sense*
:   Approximated b-spline surface is not always in the same direction as the original surface; if sense is true, then the underlying surface and the b-spline surface are in the same direction

#### Return Value

Array of values giving the b-spline surface parameters

Remarks

The VP0 parameter contains the following values, which you can obtain by using [ISurface::Parameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md) or [ISurface::IParameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md):

- vP0[0] & vP0[2] are the lower bounds of the U & V surface parameters, respectively
- vP0[1] & vP0[3] are the upper bounds of the U & V surface parameters, respectively

If you want to use the Bsurface in combination with its trim curves, you should use the [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md) method to extract the trim curves and the Bsurface. The IFace2::GetTrimCurves2 method provides much better alignment of the trim curves with the Bsurface because they are both generated at the same time.

Evaluation is as follows:

Number of returned double elements is (4 + NumUKnots + NumVKnots + NumControlPointDoubles), where NumUKnots = (NumColumnsControlPoints + Uorder) and NumVKnots = (NumRowsControlPoints + Vorder).

The returned data are arranged in this order:

- Uorder, Vorder - These are two ints packed into a double

  - Uorder - Order of surface in U direction
  - Vorder - Order of surface in V direction
- NumColumnsControlPoints, NumRowsControlPoints - These are two integers packed into a double

  - NumColumnsControlPoints - Number of columns for the control points
  - NumRowsControlPoints - Number of rows for the control points
- Uperiodicity, Vperiodicity - These are two integers packed into a double. Since you may be generating a Bsurface with this function, the U,V periodicity values may be opposite from the original surface. Refer to ISurface::Parameterization or ISurface::IParameterization.

  - Uperiodicity - True if surface is periodic in U direction
  - Vperiodicity - True if surface is periodic in V direction
- DimensionControlPoints, dummy - These are two integers packed into a double

  - DimensionControlPoints - Dimension for control points.

    - DimensionControlPoints = 3 for non-rational surfaces and control point coordinates are output as [x0,y0,z0,x1,y1,z1,.........].
    - DimensionControlPoints = 4 for rational surfaces and control point coordinates and the weight are output as [x0,y0,z0,w0,x1,y1,z1,w1,........].
  - dummy - a system-used filler.
- UKnots - Knot vector in the u direction.

There will be (NumColumnsControlPoints + Uorder) knot values. If the surface is periodic in the U direction, then data is converted and returned in a non-periodic form with additional knots added to the surface ends.

- VKnots - Knot vector in the v direction.

There will be (NumRowsControlPoints + Vorder) knot values. If the surface is periodic in the V direction, then data is converted and returned in a non-periodic form with additional knots added to the surface ends.

- ControlPoints - This is a list of control points output in (NumColumnsControlPoints\*NumRowsControlPoints) vectors of dimension DimensionControlPoints. The vectors are output row by row. The U direction of surface is in the row direction. The V direction of surface is in the column direction.

  - For non-rational surfaces, control point coordinates are output as [x0,y0,z0,x1,y1,z1,.........].
  - For rational surfaces, control point coordinates and the weight are output as [x0,y0,z0,w0,x1,y1,z1,w1,........].
  - For example:

|  |  |  |
| --- | --- | --- |
| Row1, Column1 | Row1, Column2 |  |
| x0, y0, z0 | x1, y1, z1 | = 6 |
|  |  |  |
| Row2, Column1 | Row2, Column2 |  |
| x2, y2, z2 | x3, y3, z3 | = 6 |
|  |  |  |
| Row3, Column1 | Row3, Column2 |  |
| x4, y4, z4 | x5, y5, z5 | = 6 |
|  |  |  |
|  |  | = 18 |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IGetBSurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParams.md)  
[ISurface::IGetBSurfParamsSize3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize3.md)

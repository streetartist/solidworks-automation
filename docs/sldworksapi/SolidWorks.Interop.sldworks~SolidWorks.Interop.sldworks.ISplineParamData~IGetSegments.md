# IGetSegments Method (ISplineParamData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetSegments`

Gets the coefficients of all of the piecewise polynomials of a spline.
Gets the coefficients of all of the piecewise polynomials of a spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSegments( _
   ByVal Count As System.Integer, _
   ByRef Segments As System.Double _
) As System.Boolean
```

```

Dim instance As ISplineParamData
Dim Count As System.Integer
Dim Segments As System.Double
Dim value As System.Boolean
 
value = instance.IGetSegments(Count, Segments)
```

```

System.bool IGetSegments( 
   System.int Count,
   out System.double Segments
)
```

```

System.bool IGetSegments( 
   System.int Count,
   [Out] System.double Segments
) 
```

#### Parameters

*Count*
:   Size of Segments array

*Segments*
:   - in-process, unmanaged C++: Pointer to an array of doubles

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if successful, false if not

Remarks

This method works only with P-spline parameterization data. Before calling this method, call [ICurve::GetPCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.md) to obtain the P-spline parameterization data object for the curve.

Before calling this method, call [ISplineParamData::SegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SegmentCount.md) to populate the Count parameter.

Each pair of spline control points defines one segment of a curve. Each segment is typically represented by a cubic polynomial. This method returns a one-dimensional array containing doubles that are the coefficients of all of the piecewise cubic polynomials of the spline.

The segment coefficients are stored in the Segments array in order of increasing variable exponent:

(constants)(first degree coefficients)(second degree coefficients)(third degree coefficients) etc.

For example, if the spline segments are represented by cubic rational (dim=4) polynomials in parametric form,

        (w0\*a0 + w1\*a1\*t + w2\*a2\*t\*\*2 + w3\*a3\*t\*\*3)

p(t) = --------------------------------------------

            (w0 + w1\*t + w2\*t\*\*2 + w3\*t\*\*3)

where w0, w1, w2, w3 are weighting coefficients and a0, a1, a2, a3 are vector coefficients, then the Segments array stores (dimension(4) X order(4)) = 16 coefficients:

(a0x,a0y,a0z,w0)(a1x,a1y,a1z,w1)(a2x,a2y,a2z,w2)(a3x,a3y,a3z,w3).

If the spline segments are represented by cubic non-rational (dim=3) polynomials, then the Segments array stores (dimension(3) X order(4)) = 12 coefficients:

> (a0x,a0y,a0z)(a1x,a1y,a1z)(a2x,a2y,a2z)(a3x,a3y,a3z0).

The total number of coefficients returned by this method is:

([segment count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SegmentCount.md)) x ([order](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Order.md)) x ([dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md))

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)  
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.md)  
[ISplineParamData::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetSegments.md)

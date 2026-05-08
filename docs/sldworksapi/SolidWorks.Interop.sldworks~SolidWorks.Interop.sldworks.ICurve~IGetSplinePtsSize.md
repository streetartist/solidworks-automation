# IGetSplinePtsSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePtsSize`

Gets the size of the array required by ICurve::IGetSplinePts.
Gets the size of the array required by [ICurve::IGetSplinePts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSplinePtsSize( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As System.Integer
```

```

Dim instance As ICurve
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As System.Integer
 
value = instance.IGetSplinePtsSize(PropArray, KnotsArray, CntrlPntCoordArray)
```

```

System.int IGetSplinePtsSize( 
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

```

System.int IGetSplinePtsSize( 
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray
) 
```

#### Parameters

*PropArray*
:   Array that includes dimension, order, number of control points, and periodicity

*KnotsArray*
:   knot1, knot2, ..., knot*n*

*CntrlPntCoordArray*
:   controlpoint1[dimension], controlpoint2[dimension], ...,  controlpoint*n*[dimension]

#### Return Value

Size of the data set returned by [ICurve::IGetSplinePts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.md)

Remarks

PropArray contains 4 integers:

- Dimension
- Order
- Number of control points
- Periodicity ( True or false )

KnotsArray is an array of doubles with (Number of control points + Order) elements.

The size of the CntrlPntCoordArray array is based on the curve dimension.

- Dimension = 2 then each control point is an array of 2 doubles ( u, v )
- Dimension = 3 then each control point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each control point is an array of 4 doubles ( x, y, z, w ) where w = weight

Data passed into this method must satisfy the following requirements:

- If the curve is periodic, it must not have any repeated knots.
- If the curve is non-periodic, it must only have repeated knots at its ends.
- The curve must be cubic or lower degree, non-rational and have continuous first and second derivatives.

**NOTE:** For a linear or quadratic curve to satisfy these continuity requirements, it  
must consist of a single segment.

Example

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetSplinePts.md)

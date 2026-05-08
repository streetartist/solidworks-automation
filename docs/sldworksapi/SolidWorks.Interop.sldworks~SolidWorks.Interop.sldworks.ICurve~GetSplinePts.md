# GetSplinePts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetSplinePts`

Gets the spline points for this curve.
Gets the spline points for this curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplinePts( _
   ByVal ParamsArrayIn As System.Object _
) As System.Object
```

```

Dim instance As ICurve
Dim ParamsArrayIn As System.Object
Dim value As System.Object
 
value = instance.GetSplinePts(ParamsArrayIn)
```

```

System.object GetSplinePts( 
   System.object ParamsArrayIn
)
```

```

System.Object^ GetSplinePts( 
   System.Object^ ParamsArrayIn
) 
```

#### Parameters

*ParamsArrayIn*
:   Array containing the definition of the spline

#### Return Value

Array containing the spline points

Remarks

For OLE Automation applications, the ParamsIn argument contains an array defining the spline. This array contains the values for propArray, knotsArray and cntrlPntCoordArray, all packed into a single array (propArray is packed as four integers into the first two elements of the array.) The contents of these arrays is described in [ICurve::IGetSplinePtsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePtsSize.md).

The array returned contains the x, y, z location of the spline points:

> **[** *x1, y1, z1, x2, y2, z2*,....**]**

Data passed into this method must satisfy the following requirements:

- If the curve is periodic, it must not have any repeated knots.
- If the curve is non-periodic, it must only have repeated knots at its ends.
- The curve must be cubic or lower degree, non-rational, and have continuous first  
  and second derivatives.

**NOTE:** For a linear or quadratic curve to satisfy these continuity requirements, it must consist of a single segment.

Example

[Get Curve Spline Points (VBA)](Get_Curve_Spline_Points_Example_VB.htm)  
[Get Length of Spline or Elliptical Edge (VBA)](Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm)  
[Get Parameters and Spline Points for Curve (VBA)](Get_Parameters_and_Spline_Points_for_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IGetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.md)

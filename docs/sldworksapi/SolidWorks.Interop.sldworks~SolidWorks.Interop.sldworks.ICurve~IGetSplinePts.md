# IGetSplinePts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts`

Gets the spline points for this curve.
Gets the spline points for this curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSplinePts() As System.Double
```

```

Dim instance As ICurve
Dim value As System.Double
 
value = instance.IGetSplinePts()
```

```

System.double IGetSplinePts()
```

```

System.double IGetSplinePts(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing the spline points

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

[ICurve::IGetSplinePtsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePtsSize.md) defines the spline and determines the size of the array returned.

The array returned contains the x, y, z location of the spline points:

> **[** *x1, y1, z1, x2, y2, z2*,....**]**

Data passed into ICurve::IGetSplinePtsSize must satisfy the following requirements:

- If the curve is periodic, it must not have any repeated knots.
- If the curve is non-periodic, it must only have repeated knots at its ends.
- The curve must be cubic or lower degree, non-rational, and have continuous first  
  and second derivatives.

**NOTE:** For a linear or quadratic curve to satisfy these continuity requirements, it must consist of a single segment.

Example

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetSplinePts.md)

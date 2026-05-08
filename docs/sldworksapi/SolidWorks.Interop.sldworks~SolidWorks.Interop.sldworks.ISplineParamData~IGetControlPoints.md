# IGetControlPoints Method (ISplineParamData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetControlPoints`

Gets the coordinates of all of the control points of the spline.
Gets the coordinates of all of the control points of the spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetControlPoints( _
   ByVal Count As System.Integer, _
   ByRef ControlPoints As System.Double _
) As System.Boolean
```

```

Dim instance As ISplineParamData
Dim Count As System.Integer
Dim ControlPoints As System.Double
Dim value As System.Boolean
 
value = instance.IGetControlPoints(Count, ControlPoints)
```

```

System.bool IGetControlPoints( 
   System.int Count,
   out System.double ControlPoints
)
```

```

System.bool IGetControlPoints( 
   System.int Count,
   [Out] System.double ControlPoints
) 
```

#### Parameters

*Count*
:   Size of ControlPoints array

*ControlPoints*
:   - in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if successful, false if not

Remarks

Before calling this method, call [ISplineParamData::ControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount.md) to populate the Count parameter.

Control points determine the shape of a spline or curve. Starting with a set of control points, all other points of a spline can be calculated. A given point on the spline is calculated using the polynomial basis functions of its nearest control points. The [knot vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.md) determines which control point basis functions are in force for calculating each point along a curve.

The size of the ControlPoints array is based on the curve dimension:

- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 2 then each control point has 2 doubles ( x, y )
- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 3 then each control point has 3 doubles ( x, y, z )
- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 4, and the curve is closed or periodic, then each control point has 4 doubles ( x, y, z, w ), where w = weight
- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 4, and the curve is open or non-periodic, then each control point has 4 doubles ( w\*x, w\*y, w\*z, w ), where w = weight
- Size of ControlPoints array = [control points count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount.md) \* [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)  
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.md)  
[ISplineParamData::GetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.md)

# SetControlPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetControlPoints`

Sets the coordinates of all of the control points of a spline.
Sets the coordinates of all of the control points of a spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetControlPoints( _
   ByVal ControlPoints As System.Object _
) As System.Boolean
```

```

Dim instance As ISplineParamData
Dim ControlPoints As System.Object
Dim value As System.Boolean
 
value = instance.SetControlPoints(ControlPoints)
```

```

System.bool SetControlPoints( 
   System.object ControlPoints
)
```

```

System.bool SetControlPoints( 
   System.Object^ ControlPoints
) 
```

#### Parameters

*ControlPoints*
:   One-dimensional array of doubles (see **Remarks**)

#### Return Value

True if successful, false if not

Remarks

Control points determine the shape of a spline or curve. Starting with a set of control points, all other points of a spline can be calculated. A given point on the spline is calculated using the polynomial basis functions of its nearest control points. The [knot vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.md) determines which control point basis functions are in force for calculating each point along a curve.

The size of the ControlPoints array is based on the curve dimension:

- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 2 then each control point has 2 doubles ( x, y )
- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 3 then each control point has 3 doubles ( x, y, z )
- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 4, and the curve is closed or periodic, then each control point has 4 doubles ( x, y, z, w ), where w = weight
- if [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md) = 4, and the curve is open or non-periodic, then each control point has 4 doubles ( w\*x, w\*y, w\*z, w ), where w = weight
- Size of ControlPoints array = [control points count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount.md) \* [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Dimension.md)

Example

[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)  
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)  
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)  
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.md)  
[ISplineParamData::GetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.md)  
[ISplineParamData::IGetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetControlPoints.md)  
[ISketchSpline::ModifyControlPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyControlPoint.md)

# ConvertLineToBcurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve`

Converts the specified line into a b-spline curve.
Converts the specified line into a b-spline curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertLineToBcurve( _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As System.Object
```

```

Dim instance As ICurve
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As System.Object
 
value = instance.ConvertLineToBcurve(StartPoint, EndPoint)
```

```

System.object ConvertLineToBcurve( 
   System.object StartPoint,
   System.object EndPoint
)
```

```

System.Object^ ConvertLineToBcurve( 
   System.Object^ StartPoint,
   System.Object^ EndPoint
) 
```

#### Parameters

*StartPoint*
:   Array values for the coordinates of the start point of the line

*EndPoint*
:   Array values for the coordinates of the end point of the line

#### Return Value

Array values giving the b-spline representation of the line

Remarks

Given coordinates of two end points of a line, this method returns the b-spline representation of the line. The returned data are doubles arranged in the following order:

|  |  |  |
| --- | --- | --- |
| - dim, order | | Two integers packed into a double. |
|  | - dim | Dimension of the control point data.  If dim=3 (non-rational), control point coordinates are returned as [x0,y0,z0,x1,y1,z1,.....].  If dim=4 (rational), control point coordinates are returned as [x0,y0,z0,w0,x1,y1,z1,w1,.....], where w is the weight for the point. |
|  | - order | Order of the b-spline returned. |
| - NumControlPoints, Periodic | | Two integers packed into a double. |
|  | - NumControlPoints | Number of control points for the b-spline. |
|  | - Periodic | True if the b-spline is periodic. |
| - Knots | | Knot vectors. The Knot array contains (NumControlPoints + order) knot values. If the original curve is periodic, then the data is  returned in a non-periodic form with extra knots inserted at the curve ends. |
| - ControlPoints | | List of control points output in (NumControlPoints) vectors of dimension dim.  For non-rational b-spline, control point coordinates are output as [x0,y0,z0,x1,y1,z1,.........].  For rational b-spline, control point coordinates and the weight are output as [x0,y0,z0,w0,x1,y1,z1,w1,........], where w is the weight for the point. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)  
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.md)  
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.md)  
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.md)  
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.md)

# ConvertArcToBcurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve`

Gets the b-spline value representation of the arc.
Gets the b-spline value representation of the arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertArcToBcurve( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal Start As System.Object, _
   ByVal End As System.Object _
) As System.Object
```

```

Dim instance As ICurve
Dim Center As System.Object
Dim Axis As System.Object
Dim Start As System.Object
Dim End As System.Object
Dim value As System.Object
 
value = instance.ConvertArcToBcurve(Center, Axis, Start, End)
```

```

System.object ConvertArcToBcurve( 
   System.object Center,
   System.object Axis,
   System.object Start,
   System.object End
)
```

```

System.Object^ ConvertArcToBcurve( 
   System.Object^ Center,
   System.Object^ Axis,
   System.Object^ Start,
   System.Object^ End
) 
```

#### Parameters

*Center*
:   Array for the x, y, z coordinates of the center point of the  
    arc

*Axis*
:   Array for the normal vector of the arc

*Start*
:   Array for the x, y, z coordinates of the start point of the arc

*End*
:   Array for the x, y, z coordinates of the end point of the arc

#### Return Value

Array for the b-spline representation of the arc

Remarks

Given coordinates of the center, start, end points and the normal vector of an arc, this method returns the b-spline representation of the arc.

The returned data are doubles arranged in the following order:

|  |  |  |
| --- | --- | --- |
| - dim, order | | Two integers packed into a double. |
|  | - dim | Dimension of the control point data.  If dim=3 (non-rational), control point coordinates are returned as [x0,y0,z0,x1,y1,z1,.....].  If dim=4 (rational), control point coordinates are returned as [x0,y0,z0,w0,x1,y1,z1,w1,.....], where w is the weight for the point. |
|  | - order | Order of the b-spline returned. |
| - NumControlPoints, Periodic | | Two integers packed into a double. |
|  | - NumControlPoints | Number of control points for the b-spline. |
|  | - Periodic | True if the b-spline is periodic. |
| - Knots | | Knot vectors. The Knot array contains (NumControlPoints + order) knot values. If the original curve is periodic, then the data is returned in a non-periodic form with extra knots inserted at the curve ends. |
| - ControlPoints | | List of control points output in (NumControlPoints) vectors of dimension dim.  For non-rational b-spline, control point coordinates are output as [x0,y0,z0,x1,y1,z1,.........].  For rational b-spline, control point coordinates and the weight are output as [x0,y0,z0,w0,x1,y1,z1,w1,........], where w is the weight for the point. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)  
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.md)  
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.md)  
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.md)

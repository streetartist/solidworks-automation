# IntersectCurve Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IntersectCurve`

Gets a set of points that represent the intersection of two trimmed curves.
Gets a set of points that represent the intersection of two trimmed curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IntersectCurve( _
   ByVal OtherCurve As System.Object, _
   ByVal ThisStartPoint As System.Object, _
   ByVal ThisEndPoint As System.Object, _
   ByVal OtherStartPoint As System.Object, _
   ByVal OtherEndPoint As System.Object _
) As System.Object
```

```

Dim instance As ICurve
Dim OtherCurve As System.Object
Dim ThisStartPoint As System.Object
Dim ThisEndPoint As System.Object
Dim OtherStartPoint As System.Object
Dim OtherEndPoint As System.Object
Dim value As System.Object
 
value = instance.IntersectCurve(OtherCurve, ThisStartPoint, ThisEndPoint, OtherStartPoint, OtherEndPoint)
```

```

System.object IntersectCurve( 
   System.object OtherCurve,
   System.object ThisStartPoint,
   System.object ThisEndPoint,
   System.object OtherStartPoint,
   System.object OtherEndPoint
)
```

```

System.Object^ IntersectCurve( 
   System.Object^ OtherCurve,
   System.Object^ ThisStartPoint,
   System.Object^ ThisEndPoint,
   System.Object^ OtherStartPoint,
   System.Object^ OtherEndPoint
) 
```

#### Parameters

*OtherCurve*
:   Curve to intersect with this [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*ThisStartPoint*
:   Array containing the start point of this curve

*ThisEndPoint*
:   Array containing the end point of this curve

*OtherStartPoint*
:   Array containing the start point of otherCurve

*OtherEndPoint*
:   Array containing the end point of otherCurve

#### Return Value

Array containing the intersection points (see **Remarks**)

Remarks

The array of doubles returned contains the x, y, z location of the tessellation points and a code for each point that indicates the intersection class:

[ x1, y1, z1, k1, x2, y2, z2, k2.... ]

Return codes are defined in [swIntersectionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swIntersectionType_e.html).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IIntersectCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve.md)  
[ICurve::IIntersectCurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurveSize.md)

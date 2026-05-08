# IIntersectCurve Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve`

Gets a set of points that represent the intersection of two trimmed curves.
Gets a set of points that represent the intersection of two trimmed curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IIntersectCurve( _
   ByVal OtherCurve As Curve, _
   ByRef ThisStartPoint As System.Double, _
   ByRef ThisEndPoint As System.Double, _
   ByRef OtherStartPoint As System.Double, _
   ByRef OtherEndPoint As System.Double _
) As System.Double
```

```

Dim instance As ICurve
Dim OtherCurve As Curve
Dim ThisStartPoint As System.Double
Dim ThisEndPoint As System.Double
Dim OtherStartPoint As System.Double
Dim OtherEndPoint As System.Double
Dim value As System.Double
 
value = instance.IIntersectCurve(OtherCurve, ThisStartPoint, ThisEndPoint, OtherStartPoint, OtherEndPoint)
```

```

System.double IIntersectCurve( 
   Curve OtherCurve,
   ref System.double ThisStartPoint,
   ref System.double ThisEndPoint,
   ref System.double OtherStartPoint,
   ref System.double OtherEndPoint
)
```

```

System.double IIntersectCurve( 
   Curve^ OtherCurve,
   System.double% ThisStartPoint,
   System.double% ThisEndPoint,
   System.double% OtherStartPoint,
   System.double% OtherEndPoint
) 
```

#### Parameters

*OtherCurve*
:   Curve to intersect with this [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*ThisStartPoint*
:   Start point of this curve

*ThisEndPoint*
:   End point of this curve

*OtherStartPoint*
:   Start point of otherCurve

*OtherEndPoint*
:   End point of otherCurve

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles of the intersection points (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The array of doubles returned contains the x, y, z location of the tessellation points and a code for each point that indicates the intersection class:

[ x1, y1, z1, k1, x2, y2, z2, k2.... ]

Return codes are defined in [swIntersectionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swIntersectionType_e.html).

Before calling this method, call [ICurve::IIntersectCurveSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurveSize.md) to determine the size of the array needed for the return values from this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IntersectCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IntersectCurve.md)

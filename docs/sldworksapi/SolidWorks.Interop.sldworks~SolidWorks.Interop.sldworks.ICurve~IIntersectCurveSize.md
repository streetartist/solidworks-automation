# IIntersectCurveSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurveSize`

Gets the size of the array required by ICurve::IIntersectCurve.
Gets the size of the array required by [ICurve::IIntersectCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IIntersectCurveSize( _
   ByVal OtherCurve As Curve, _
   ByRef ThisStartPoint As System.Double, _
   ByRef ThisEndPoint As System.Double, _
   ByRef OtherStartPoint As System.Double, _
   ByRef OtherEndPoint As System.Double _
) As System.Integer
```

```

Dim instance As ICurve
Dim OtherCurve As Curve
Dim ThisStartPoint As System.Double
Dim ThisEndPoint As System.Double
Dim OtherStartPoint As System.Double
Dim OtherEndPoint As System.Double
Dim value As System.Integer
 
value = instance.IIntersectCurveSize(OtherCurve, ThisStartPoint, ThisEndPoint, OtherStartPoint, OtherEndPoint)
```

```

System.int IIntersectCurveSize( 
   Curve OtherCurve,
   ref System.double ThisStartPoint,
   ref System.double ThisEndPoint,
   ref System.double OtherStartPoint,
   ref System.double OtherEndPoint
)
```

```

System.int IIntersectCurveSize( 
   Curve^ OtherCurve,
   System.double% ThisStartPoint,
   System.double% ThisEndPoint,
   System.double% OtherStartPoint,
   System.double% OtherEndPoint
) 
```

#### Parameters

*OtherCurve*
:   Curve to intersect with this curve

*ThisStartPoint*
:   Start point of this curve

*ThisEndPoint*
:   End point of this curve

*OtherStartPoint*
:   Start point of otherCurve

*OtherEndPoint*
:   End point of otherCurve

#### Return Value

Size of the array needed to contain the return values of [ICurve::IIntersectCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve.md)

Remarks

To get the actual intersection points, call [ICurve::IIntersectCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IntersectCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IntersectCurve.md)

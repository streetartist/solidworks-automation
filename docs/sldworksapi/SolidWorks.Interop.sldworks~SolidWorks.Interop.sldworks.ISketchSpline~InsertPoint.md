# InsertPoint Method (ISketchSpline)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~InsertPoint`

Inserts a point at the specified coordinates of this spline.
Inserts a point at the specified coordinates of this spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchSpline
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.InsertPoint(X, Y, Z)
```

```

System.bool InsertPoint( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool InsertPoint( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X coordinate on this spline

*Y*
:   Y coordinate on this spline

*Z*
:   Z coordinate on this spline

#### Return Value

True if a point is added to the spline, false if not

Remarks

This method works only if X, Y, and Z specify a location on this spline. You cannot add a new point that is not on this spline.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::DeletePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DeletePoint.md)  
[ISketchSpline::GetPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPointCount.md)  
[ISketchSpline::GetPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.md)  
[ISketchSpline::IEnumPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.md)  
[ISplineHandle::SplinePointNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~SplinePointNumber.md)  
[ISketchSpline::ShowInflectionPoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowInflectionPoints.md)

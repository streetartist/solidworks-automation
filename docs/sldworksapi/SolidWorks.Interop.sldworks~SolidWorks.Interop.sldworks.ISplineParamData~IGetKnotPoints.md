# IGetKnotPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetKnotPoints`

Gets all of the knot points of the spline.
Gets all of the knot points of the spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetKnotPoints( _
   ByVal Count As System.Integer, _
   ByRef KnotPoints As System.Double _
) As System.Boolean
```

```

Dim instance As ISplineParamData
Dim Count As System.Integer
Dim KnotPoints As System.Double
Dim value As System.Boolean
 
value = instance.IGetKnotPoints(Count, KnotPoints)
```

```

System.bool IGetKnotPoints( 
   System.int Count,
   out System.double KnotPoints
)
```

```

System.bool IGetKnotPoints( 
   System.int Count,
   [Out] System.double KnotPoints
) 
```

#### Parameters

*Count*
:   Size of KnotPoints array

*KnotPoints*
:   - in-process, unmanaged C++: Pointer to an array of double values between 0 and 1, inclusive

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if successful, false if not

Remarks

Before calling this method, call [ISplineParamData::KnotPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~KnotPointsCount.md) to populate the Count parameter.

Together with [control points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.md), knots determine the shape and smoothness of a spline. The knot vector divides the parametric space into intervals or knot spans. These intervals may be uniform or non-uniform. Each interval governs a different control point.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)  
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.md)  
[ISplineParamData::GetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.md)

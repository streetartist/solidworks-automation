# ModifyKnot Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyKnot`

Modifies the specified interior knot of this sketch spline.
Modifies the specified interior knot of this sketch spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ModifyKnot( _
   ByVal Index As System.Integer, _
   ByVal DKnot As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchSpline
Dim Index As System.Integer
Dim DKnot As System.Double
Dim value As System.Boolean
 
value = instance.ModifyKnot(Index, DKnot)
```

```

System.bool ModifyKnot( 
   System.int Index,
   System.double DKnot
)
```

```

System.bool ModifyKnot( 
   System.int Index,
   System.double DKnot
) 
```

#### Parameters

*Index*
:   1-based index of the interior knot to modify (see **Remarks**)

*DKnot*
:   Knot value

#### Return Value

True if knot successfully modifed, false if not

Remarks

Interior knots occur after the first set of 0s and before the last set of 1s in the knot array. If the knot array is [ 0 0 0 0 0.279240779943874 0.55 0.720759220056126 1 1 1 1 ], then the interior knots are 0.279240779943874, 0.55, and 0.720759220056126.

Before calling this method, call [ISplineParamData::GetKnotPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.md) and [ISplineParamData::KnotPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~KnotPointsCount.md) to help specify Index and the new knot value.

After calling this method, you must call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md) to update the sketch.

Example

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::ModifyControlPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyControlPoint.md)  
[ISplineParamData::SetKnotPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetKnotPoints.md)

# ModifyControlPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyControlPoint`

Specifies new coordinates for the specified control point of this sketch spline.
Specifies new coordinates for the specified control point of this sketch spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ModifyControlPoint( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchSpline
Dim Index As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.ModifyControlPoint(Index, X, Y, Z)
```

```

System.bool ModifyControlPoint( 
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool ModifyControlPoint( 
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Index*
:   1-based index of the control point to modify

*X*
:   X coordinate

*Y*
:   Y coordinate

*Z*
:   Z coordinate

#### Return Value

True if control point successfully modified, false if not

Remarks

Before calling this method, call [ISplineParamData::GetControlPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.md) and [ISplineParamData::ControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount.md) to help specify Index and the new coordinates.

After calling this method, you must call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md) to update the sketch.

Example

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::ModifyKnot Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyKnot.md)  
[ISplineParamData::SetControlPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetControlPoints.md)

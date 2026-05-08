# ISketchSpline Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members`

Provides access to sketched spline entities.
The following tables list the members exposed by [ISketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CurveDegree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveDegree.md) | Gets or sets the degree of curve for this Bezier curve style spline. |
| Property | [CurveType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveType.md) | Gets or sets the type of curve for this style spline. |
| Property | [DisplayControlPolygon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DisplayControlPolygon.md) | Gets or sets whether to add a control polygon to this spline. |
| Property | [IsRationalCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.md) | Gets whether this spline is rational or non-rational. |
| Property | [IsStyleSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsStyleSpline.md) | Gets whether this spline is a style spline. |
| Property | [Proportional](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~Proportional.md) | Gets or sets whether the spline resizes proportionally when you drag an endpoint the spline. |
| Property | [ShowCurvatureCombs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.md) | Gets or sets whether to show curvature combs. |
| Property | [ShowInflectionPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowInflectionPoints.md) | Gets or sets whether show the inflection points of this spline. |
| Property | [ShowMinimumRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowMinimumRadius.md) | Gets or sets the minimum radius of a curve for this spline. |
| Property | [ShowSplineHandles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.md) | Gets or sets whether to show the [handles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md) for this spline. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddCurvatureControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddCurvatureControl.md) | Adds a curvature control pointer to this spline. |
| Method | [AddTangencyControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddTangencyControl.md) | Adds a new handle to help control the tangency of this spline. |
| Method | [DeletePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DeletePoint.md) | Deletes a point on this spline. |
| Method | [GetControlVertexWeights](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetControlVertexWeights.md) | Gets the weights of the control vetexes of this rational spline. |
| Method | [GetEquationParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters.md) | Obsolete. Superseded by [ISketchSpline::GetEquationParameters2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters2.md). |
| Method | [GetEquationParameters2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters2.md) | Gets an equation-driven curve's parameters. |
| Method | [GetPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPointCount.md) | Gets the number of points in this sketch spline segment. |
| Method | [GetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints.md) | Obsolete. Superseded by [ISketchSpline::GetPoints2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.md) and [ISketchSpline::IEnumPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.md). |
| Method | [GetPoints2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.md) | Gets an array of sketch points for the spline. |
| Method | [GetSplineHandleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.md) | Gets the number of [handles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md) in this spline. |
| Method | [GetSplineHandles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.md) | Gets the handles of this spline. |
| Method | [IEnumPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.md) | Gets an enumeration of sketch points for the spline. |
| Method | [IGetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetPoints.md) | Obsolete. Superseded by [ISketchSpline::GetPoints2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.md) and [ISketchSpline::IEnumPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.md). |
| Method | [IGetSplineHandles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.md) | Gets the handles of this spline. |
| Method | [InsertPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~InsertPoint.md) | Inserts a point at the specified coordinates of this spline. |
| Method | [MakeRational](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~MakeRational.md) | Sets whether this spline is rational or non-rational. |
| Method | [ModifyControlPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyControlPoint.md) | Specifies new coordinates for the specified control point of this sketch spline. |
| Method | [ModifyKnot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyKnot.md) | Modifies the specified interior knot of this sketch spline. |
| Method | [RelaxSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~RelaxSpline.md) | Smoothens the shape of a spline that was changed by dragging a node on a [control polygon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DisplayControlPolygon.md). |
| Method | [ResetAllHandles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.md) | Resets all [handles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md) to their initial state. |
| Method | [SetControlVertexWeights](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetControlVertexWeights.md) | Sets the weights of the control vetexes of this rational spline. |
| Method | [SetEquationParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters.md) | Obsolete. Superseded by [ISketchSpline::SetEquationParameters2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters2.md). |
| Method | [SetEquationParameters2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters2.md) | Sets an equation-driven curve's parameters. |
| Method | [Simplify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~Simplify.md) | Reduces the number of points in a spline to increase system performance in models with complex spline curves. |

[Top](#top)

 

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)

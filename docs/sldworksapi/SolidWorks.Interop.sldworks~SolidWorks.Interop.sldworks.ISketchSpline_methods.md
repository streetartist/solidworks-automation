# ISketchSpline Interface Methods

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_methods`

Provides access to sketched spline entities.
For a list of all members of this type, see [ISketchSpline members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md).

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

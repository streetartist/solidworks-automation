# ICurve Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members`

Allows access to a curve and its parameters in their native form or in terms of b-curve data.
The following tables list the members exposed by [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CircleParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CircleParams.md) | Gets the parameters of a curve that is a circle. |
| Property | [ICircleParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICircleParams.md) | Gets the parameters of a curve that is a circle. |
| Property | [ILineParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.md) | Gets the parameters of a curve that is a line. |
| Property | [LineParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.md) | Gets the parameters of a curve that is a line. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ApplyTransform.md) | Applies the transform to a curve. |
| Method | [ConvertArcToBcurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md) | Gets the b-spline value representation of the arc. |
| Method | [ConvertLineToBcurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md) | Converts the specified line into a b-spline curve. |
| Method | [Copy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Copy.md) | Gets a copy of this curve. |
| Method | [CreateTrimmedCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve.md) | Obsolete. Superseded by [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md). |
| Method | [CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md) | Creates a trimmed curve. |
| Method | [CreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateWireBody.md) | Creates a wire body from this curve. |
| Method | [Evaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate.md) | Obsolete. Superseded by [ICurve::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate2.md). |
| Method | [Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate2.md) | Evaluates the curve at the specified parameter of the curve. |
| Method | [ExtentCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.md) | Extends a b-spline curve by the specified length. |
| Method | [FindMinimumRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.md) | Finds the minimum radius of curvature of the selected curve and its position and u-v parameters. |
| Method | [GetBaseCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBaseCurve.md) | Gets the base curve for this trimmed curve. |
| Method | [GetBCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.md) | Obsolete. Superseded by [ICurve::GetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md). |
| Method | [GetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams3.md) | Obsolete. Superseded by [ICurve::GetBCurveParams4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams4.md) |
| Method | [GetBCurveParams4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams4.md) | Obsolete. Superseded by [ICurve::GetBCurveParams5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams5.md). |
| Method | [GetBCurveParams5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams5.md) | Gets a data object containing the parameters of a Bézier curve. |
| Method | [GetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetClosestPointOn.md) | Determines the closest point on the curve using the x,y,z input point. |
| Method | [GetEllipseParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.md) | Gets the parameters for this elliptical curve. |
| Method | [GetEndParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.md) | Gets the end conditions of this curve. |
| Method | [GetLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength.md) | Obsolete. Superseded by [ICurve::GetLength2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength2.md). |
| Method | [GetLength2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength2.md) | Obsolete. Superseded by [ICurve::GetLength3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength3.md). |
| Method | [GetLength3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength3.md) | Gets the length of a curve between the specified parameters. |
| Method | [GetPCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.md) | Obsolete. Superseded by [ICurve::GetPCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.md). |
| Method | [GetPCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.md) | Gets the piecewise polynomial parameterization data for this curve. |
| Method | [GetSplinePts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetSplinePts.md) | Gets the spline points for this curve. |
| Method | [GetTessPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetTessPts.md) | Gets a set of points that represent the tessellation of this curve. |
| Method | [IConvertArcToBcurveSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize.md) | Gets the b-curve size for the arc's conversion given the coordinates of the two end points of a line. |
| Method | [IConvertLineToBcurveSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.md) | Converts the specified line into a b-spline curve. |
| Method | [IConvertPcurveToBcurveSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.md) | Creates a b-curve from piecewise data. |
| Method | [ICopy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICopy.md) | Gets a copy of this curve. |
| Method | [ICreateTrimmedCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICreateTrimmedCurve.md) | Obsolete. Superseded by [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md). |
| Method | [Identity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md) | Gets the type of curve. |
| Method | [IEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IEvaluate.md) | Obsolete. Superseded by [ICurve::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate2.md). |
| Method | [IEvaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IEvaluate2.md) | Evaluates the curve at the specified parameter of the curve. |
| Method | [IFindMinimumRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.md) | Finds the minimum radius of curvature of the selected curve and its position and u-v parameters. |
| Method | [IGetBCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.md) | Obsolete. Superseded by [ICurve::IGetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md). |
| Method | [IGetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md) | Obsolete. Superseded by [ICurve::GetBCurveParams4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams4.md). |
| Method | [IGetBCurveParamsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize.md) | Obsolete. Superseded by [ICurve::IGetBCuvreParamsSize2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.md). |
| Method | [IGetBCurveParamsSize2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.md) | Obsolete. Superseded by [ICurve::IGetBCurveParamsSize3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3.md). |
| Method | [IGetBCurveParamsSize3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3.md) | Gets the b-curve size. |
| Method | [IGetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetClosestPointOn.md) | Determines the closest point on the curve using the x,y,z input point. |
| Method | [IGetEllipseParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.md) | Gets the parameters for this elliptical curve. |
| Method | [IGetPCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.md) | Converts a curve to a piecewise rational cubic polynomial form. |
| Method | [IGetPCurveParamsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParamsSize.md) | Gets the p-curve size. |
| Method | [IGetSplinePts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.md) | Gets the spline points for this curve. |
| Method | [IGetSplinePtsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePtsSize.md) | Gets the size of the array required by [ICurve::IGetSplinePts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.md). |
| Method | [IGetTessPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPts.md) | Gets a set of points that represent the tessellation of this curve. |
| Method | [IGetTessPtsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPtsSize.md) | Gets the size of the array required by [ICurve::IGetTessPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPts.md). |
| Method | [IIntersectCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve.md) | Gets a set of points that represent the intersection of two trimmed curves. |
| Method | [IIntersectCurveSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurveSize.md) | Gets the size of the array required by [ICurve::IIntersectCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve.md). |
| Method | [IJoinCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.md) | Joins the specified curves. |
| Method | [IntersectCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IntersectCurve.md) | Gets a set of points that represent the intersection of two trimmed curves. |
| Method | [IReverseCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IReverseCurve.md) | Gets the reversed copy of this curve. |
| Method | [IsBcurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md) | Gets whether the curve is a b-spline curve. |
| Method | [IsCircle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.md) | Gets whether the curve is a circle. |
| Method | [IsEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.md) | Gets whether the curve is an ellipse. |
| Method | [IsLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.md) | Gets whether the curve is a line. |
| Method | [IsTrimmedCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve.md) | Gets whether the curve is trimmed. |
| Method | [JoinCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.md) | Joins the specified curves. |
| Method | [MakeBsplineCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.md) | Obsolete. Superseded by [ICurve::MakeBsplineCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2.md). |
| Method | [MakeBsplineCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2.md) | Creates a b-spline curve. |
| Method | [ReverseCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.md) | Gets the reversed copy of this curve. |
| Method | [ReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseEvaluate.md) | Gets the U parameter for the given XYZ location on this curve. |
| Method | [SimplifyBCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md) | Simplifies a b-curve. |

[Top](#top)

 

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

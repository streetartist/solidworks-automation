# IEdge Interface Methods

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_methods`

Allows access to its defining coedge, and adjacent faces, and its underlying curve and vertices as well as edge data.
For a list of all members of this type, see [IEdge members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [CreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~CreateWireBody.md) | Creates a wire body from this edge. |
| Method | [Display](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Display.md) | Highlights this edge with the specified color. |
| Method | [EdgeInFaceSense](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EdgeInFaceSense.md) | Checks whether the edge and the loop lying on the specified face have the same direction (sense). |
| Method | [EnumCoEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EnumCoEdges.md) | Lists the coedges that reference this edge. |
| Method | [Evaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate.md) | Obsolete. Superseded by [IEdge::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate2.md). |
| Method | [Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate2.md) | Evaluates the edge for the specified U parameter. |
| Method | [GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetBody.md) | Gets the body for this edge. |
| Method | [GetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetClosestPointOn.md) | Uses the X,Y,Z input point and returns the closest point on the edge. |
| Method | [GetCoEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCoEdges.md) | Gets the coedges that reference this edge. |
| Method | [GetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.md) | Gets the underlying curve for this edge. |
| Method | [GetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams.md) | Obsolete. Superseded by [IEdge::GetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md). |
| Method | [GetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md) | Obsolete. Superseded by [IEdge::GetCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.md). |
| Method | [GetCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.md) | Gets a data object containing the curve parameters for this edge. |
| Method | [GetEndVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.md) | Gets the ending vertex for this edge. |
| Method | [GetID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetID.md) | Gets the edge ID of this edge in an imported body. |
| Method | [GetParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetParameter.md) | Gets the parameterization of the edge. |
| Method | [GetStartVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.md) | Gets the starting vertex for this edge. |
| Method | [GetTangentEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdges.md) | Gets all of the edges tangent to this edge. |
| Method | [GetTangentEdgesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdgesCount.md) | Gets the number of edges tangent to this edge. |
| Method | [GetTrackingIDs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDs.md) | Gets the [tracking IDs assigned to this edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.md). |
| Method | [GetTrackingIDsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDsCount.md) | Gets the number of tracking IDs on this edge. |
| Method | [GetTwoAdjacentFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTwoAdjacentFaces.md) | Obsolete. Superseded by [IEdge::GetTwoAdjacentFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTwoAdjacentFaces2.md). |
| Method | [GetTwoAdjacentFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTwoAdjacentFaces2.md) | Gets the two faces adjacent to an edge. |
| Method | [Highlight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.md) | Add highlights or removes highlights from this edge. |
| Method | [IEdgeInFaceSense](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense.md) | Obsolete. Superseded by [IEdge::IEdgeInFaceSense2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2.md). |
| Method | [IEdgeInFaceSense2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2.md) | Checks whether the edge and the loop lying on the specified face have the same direction (sense). |
| Method | [IEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate.md) | Obsolete. Superseded by [IEdge::IEvaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate2.md). |
| Method | [IEvaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate2.md) | Evaluates the edge for the specified U parameter. |
| Method | [IGetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetClosestPointOn.md) | Uses the X,Y,Z input point and returns the closest point on the edge. |
| Method | [IGetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurve.md) | Gets the underlying curve for this edge. |
| Method | [IGetCurveParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams.md) | Obsolete. Superseded by [IEdge::IGetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md). |
| Method | [IGetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md) | Returns the curve parameters for this edge, including the edge and curve direction (sense). |
| Method | [IGetEndVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.md) | Gets the ending vertex for this edge. |
| Method | [IGetParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetParameter.md) | Gets the parameterization of the edge. |
| Method | [IGetStartVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.md) | Gets the starting vertex for this edge. |
| Method | [IGetTangentEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTangentEdges.md) | Gets all of the edges tangent to this edge. |
| Method | [IGetTrackingIDs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTrackingIDs.md) | Gets the [tracking IDs assigned to this edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.md). |
| Method | [IGetTwoAdjacentFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces.md) | Obsolete. Superseded by [IEdge::IGetTwoAdjacentFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2.md). |
| Method | [IGetTwoAdjacentFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2.md) | Gets the two faces adjacent to an edge. |
| Method | [IsParamReversed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsParamReversed.md) | Gets whether the edge and its underlying curve have the same parameterization or if the direction is reversed. |
| Method | [IsTolerant](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsTolerant.md) | Gets whether an edge is tolerant and its tolerance value. |
| Method | [RemoveId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveId.md) | Removes the edge ID assigned to this edge of an imported body. |
| Method | [RemoveRedundantTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveRedundantTopology.md) | Removes redundant topology from the edge. |
| Method | [RemoveTrackingID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveTrackingID.md) | Removes a [tracking ID assigned to this edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.md). |
| Method | [SetId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.md) | Sets the edge ID of this edge of an imported body. |
| Method | [SetTrackingID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.md) | Assigns a tracking ID to this edge. |

[Top](#top)

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

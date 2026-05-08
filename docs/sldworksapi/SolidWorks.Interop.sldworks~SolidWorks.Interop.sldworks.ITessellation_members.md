# ITessellation Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members`

Used to gather tessellation information from a SOLIDWORKS body.
The following tables list the members exposed by [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CurveChordAngleTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~CurveChordAngleTolerance.md) | Gets or sets the maximum angle, in radians, that is allowed between a chord and its originating curve. |
| Property | [CurveChordTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~CurveChordTolerance.md) | Gets or sets the maximum permitted distance from a chord (facet fin) to the curve (edge entity). |
| Property | [ImprovedQuality](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~ImprovedQuality.md) | Gets or sets whether to return higher-quality data. |
| Property | [MatchType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MatchType.md) | Gets or sets the type of Parasolid facet match for the tessellation. |
| Property | [MaxFacetWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MaxFacetWidth.md) | Gets or sets the maximum width of any side of a facet. |
| Property | [MinFacetWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MinFacetWidth.md) | Gets or sets the minimum facet width for this tessellation. |
| Property | [NeedEdgeFinMap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedEdgeFinMap.md) | Gets or sets the need edge fin map option. |
| Property | [NeedErrorList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.md) | Gets or sets the need error list option. |
| Property | [NeedFaceFacetMap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedFaceFacetMap.md) | Gets or sets the need face facet map option. |
| Property | [NeedVertexNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedVertexNormal.md) | Gets or sets the need vertex normal option. |
| Property | [NeedVertexParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedVertexParams.md) | Gets or sets the need vertex params option. |
| Property | [SurfacePlaneAngleTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneAngleTolerance.md) | Gets or sets the surface plane angle tolerance. |
| Property | [SurfacePlaneTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneTolerance.md) | Gets or sets the surface plane tolerance. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetEdgeFins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetEdgeFins.md) | Gets all of the fin IDs corresponding to a edge. |
| Method | [GetErrorList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.md) | Gets the tessellation error list. |
| Method | [GetFaceFacets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFaceFacets.md) | Gets the facets IDs that correspond to a SOLIDWORKS face. |
| Method | [GetFacetCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetCount.md) | Gets the number of facets used to create this tessellation. |
| Method | [GetFacetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFace.md) | Gets a face that corresponds to a facet. |
| Method | [GetFacetFins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFins.md) | Gets all of the fin IDs of the fins that border this facet. |
| Method | [GetFinCoFin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinCoFin.md) | Gets the ID of the CoFin that is shared by a fin. |
| Method | [GetFinCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinCount.md) | Gets the number of fins for this tessellation. |
| Method | [GetFinEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinEdge.md) | Gets the edge corresponding to a fin. |
| Method | [GetFinVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinVertices.md) | Gets the IDs of the two vertices that correspond to a fin. |
| Method | [GetVertexCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexCount.md) | Gets the number of vertices for this tessellation. |
| Method | [GetVertexNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexNormal.md) | Gets the information that describes the normal direction corresponding to vertex. |
| Method | [GetVertexParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexParams.md) | Gets the parameters corresponding to a tessellation vertex. |
| Method | [GetVertexPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexPoint.md) | Gets the X, Y and Z values that describe a tessellation vertex. |
| Method | [IGetEdgeFins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFins.md) | Gets all of the fin IDs corresponding to a edge. |
| Method | [IGetEdgeFinsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFinsCount.md) | Gets the number of fins corresponding to an edge. |
| Method | [IGetErrorList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList.md) | Obsolete. Superseded by [ITessellation::IGetErrorList2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.md). |
| Method | [IGetErrorList2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.md) | Gets the tessellation error list. |
| Method | [IGetErrorListCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.md) | Gets number of tessellation errors by error type. |
| Method | [IGetFaceFacets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets.md) | Obsolete. Superseded by [ITessellation::IGetFaceFacets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2.md). |
| Method | [IGetFaceFacets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2.md) | Gets the facets IDs that correspond to a face. |
| Method | [IGetFaceFacetsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount.md) | Obsolete. Superseded by [ITessellation::IGetFaceFacetsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.md). |
| Method | [IGetFaceFacetsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.md) | Gets the number of facets corresponding to a face. |
| Method | [IGetFacetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace.md) | Obsolete. Superseded by [ITessellation::IGetFacetFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace2.md). |
| Method | [IGetFacetFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace2.md) | Gets a face that corresponds to a facet. |
| Method | [IGetFacetFins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFins.md) | Gets all of the fin IDs of the fins that border this facet. |
| Method | [IGetFacetFinsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFinsCount.md) | Gets the number of fins corresponding to a facet. |
| Method | [IGetFinEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinEdge.md) | Gets the edge corresponding to a fin. |
| Method | [IGetFinVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinVertices.md) | Gets the IDs of the two vertices that correspond to a fin. |
| Method | [IGetVertexNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexNormal.md) | Gets the information that describes the normal direction corresponding to vertex. |
| Method | [IGetVertexParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexParams.md) | Gets the parameters corresponding to a tessellation vertex. |
| Method | [IGetVertexPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexPoint.md) | Gets the X, Y and Z values that describe a tessellation vertex. |
| Method | [Tessellate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~Tessellate.md) | Performs the tessellation. |

[Top](#top)

 

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

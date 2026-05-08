# ISimpleFilletFeatureData2 Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members`

Allows access to a simple fillet feature.
The following tables list the members exposed by [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AsymmetricFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.md) | Gets or sets whether this simple fillet/chamfer is asymmetric. |
| Property | [ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.md) | Gets or sets the cross-sectional profile for this simple fillet. |
| Property | [ConstantWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConstantWidth.md) | Gets or sets whether this simple fillet has a constant width. |
| Property | [CurvatureContinuous](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.md) | Gets or sets whether to create a smoother curvature between adjacent surfaces for this simple fillet feature. |
| Property | [DefaultConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultConicRhoOrRadius.md) | Gets or sets the default conic rho or radius. |
| Property | [DefaultDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultDistance.md) | Gets or sets the default Distance 2 radius of this asymmetric fillet. |
| Property | [DefaultRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.md) | Gets or sets the default radius of this simple fillet. |
| Property | [Edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Edges.md) | Gets or sets the edges for this simple radius fillet. |
| Property | [EnablePartialEdgeParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters.md) | Gets or sets whether to enable partial edge properties for all edges of this fillet. |
| Property | [Features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Features.md) | Gets or sets the features for this simple fillet radius. |
| Property | [FilletItemsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~FilletItemsCount.md) | Gets the number of fillets for this simple fillet feature. |
| Property | [HelpPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.md) | Gets or sets whether to resolve an ambiguous selection by using a help point when creating a face-face chamfer or a face fillet feature. |
| Property | [HoldLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.md) | Gets or sets the hold lines (boundaries) for a face blend fillet feature. |
| Property | [IsMultipleRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IsMultipleRadius.md) | Gets or sets whether this symmetric fillet or chamfer feature is a multiple radius fillet. |
| Property | [KeepFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~KeepFeatures.md) | Gets or sets whether to keep existing features on the entities selected for the fillet. |
| Property | [Loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Loops.md) | Gets or sets the loops on which to create a simple radius fillet. |
| Property | [OmitAttachedEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~OmitAttachedEdges.md) | Gets whether the simple fillet feature is not applied to the attachment edges of the feature. |
| Property | [OverflowType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~OverflowType.md) | Gets or sets the overflow type of the simple fillet feature. |
| Property | [PropagateFeatureToParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~PropagateFeatureToParts.md) | Gets or sets whether to extend the assembly simple fillet feature to all affected parts. |
| Property | [PropagateToTangentFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~PropagateToTangentFaces.md) | Gets or sets whether to extend fillet to all faces tangent to the selected face or edge. |
| Property | [ReverseFaceNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ReverseFaceNormal.md) | Gets or sets the Reverse Face Normal option when creating a face fillet between surface bodies. |
| Property | [RoundCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RoundCorners.md) | Gets or sets whether to round the corners of this simple fillet feature. |
| Property | [TrimAndAttachSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~TrimAndAttachSurfaces.md) | Gets or sets the Trim surfaces option for surface face fillets. |
| Property | [Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Type.md) | Gets the type of simple fillet feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AccessSelections.md) | Gains access to the selections used to define a simple fillet feature. |
| Method | [GetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetConicRhoOrRadius.md) | Gets the conic rho or radius of this fillet/chamfer. |
| Method | [GetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetDistance.md) | Gets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer. |
| Method | [GetEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetEdgeCount.md) | Gets the number of edges on which to create a simple radius fillet. |
| Method | [GetFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaceCount.md) | Gets the number of faces on which to create a simple radius fillet. |
| Method | [GetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaces.md) | Gets the faces on which to create a simple fillet. |
| Method | [GetFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFeatureCount.md) | Gets the number of features on which to create a simple radius fillet. |
| Method | [GetFilletItemAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.md) | Gets the fillet item at the specified index. |
| Method | [GetHoldLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.md) | Gets the number of hold lines (boundaries) for a face blend fillet feature. |
| Method | [GetLoopCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetLoopCount.md) | Gets the number of loops on which to create a single radius fillet. |
| Method | [GetPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetPartialEdgeFilletData.md) | Gets the partial edge fillet data for the specified edge. |
| Method | [GetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.md) | Gets the radius at the specified fillet/chamfer item. |
| Method | [GetSetbackDistanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackDistanceCount.md) | Gets the number of setback distances for the specified vertex on this simple fillet feature. |
| Method | [GetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertexDistance.md) | Gets the setback distance for the specified vertex on this simple fillet feature. |
| Method | [GetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertices.md) | Gets the setback vertices for this simple fillet feature. |
| Method | [GetSetbackVerticesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVerticesCount.md) | Gets the number of setback vertices for this simple fillet feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IAccessSelections.md) | Gains access to the selections used to define a simple fillet feature. |
| Method | [IGetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetConicRhoOrRadius.md) | Gets the conic rho, conic radius, or circular radius of this fillet. |
| Method | [IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetEdges.md) | Gets the edges on which to put a simple radius fillet. |
| Method | [IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFaces.md) | Gets the faces on which to create a simple radius fillet. |
| Method | [IGetFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFeatures.md) | Gets the features on which to create a simple radius fillet. |
| Method | [IGetFilletItemAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFilletItemAtIndex.md) | Gets the fillet item at the specified index. |
| Method | [IGetHoldLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.md) | Gets the hold lines (boundaries) for a face blend fillet feature. |
| Method | [IGetLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetLoops.md) | Gets the loops on which to create a simple radius fillet. |
| Method | [IGetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.md) | Gets the radius value for specified fillet item. |
| Method | [IGetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertexDistance.md) | Gets the setback distance for the specified vertex on this simple fillet feature. |
| Method | [IGetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertices.md) | Gets the setback vertices for this simple fillet feature. |
| Method | [Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.md) | Initializes this simple fillet feature to the specified type. |
| Method | [ISetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetConicRhoOrRadius.md) | Sets the conic rho, conic radius, or circular radius of this fillet. |
| Method | [ISetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetEdges.md) | Sets the edges on which to create a simple radius fillet. |
| Method | [ISetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFaces.md) | Sets the faces on which to create a simple radius fillet. |
| Method | [ISetFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFeatures.md) | Sets the features on which to create a simple radius fillet. |
| Method | [ISetHoldLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines.md) | Sets the hold lines (boundaries) for this face blend fillet feature. |
| Method | [ISetLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetLoops.md) | Sets the loops on which to put a simple radius fillet. |
| Method | [ISetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.md) | Sets the radius value for specified fillet item. |
| Method | [ISetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertexDistance.md) | Sets the setback distance for the specified vertex and its edges on this simple fillet feature. |
| Method | [ISetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertices.md) | Sets the setback vertices for this simple fillet feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ReleaseSelectionAccess.md) | Releases access to the selections used to define the simple fillet feature. |
| Method | [RepairMissingReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RepairMissingReferences.md) | Finds missing references in this fillet/chamfer and reassigns them to new edges. |
| Method | [SetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetConicRhoOrRadius.md) | Sets the conic rho or radius of this fillet/chamfer. |
| Method | [SetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetDistance.md) | Sets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer. |
| Method | [SetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetFaces.md) | Sets the faces on which to create a simple fillet. |
| Method | [SetPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetPartialEdgeFilletData.md) | Sets the partial edge fillet data for the specified edge. |
| Method | [SetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.md) | Sets the radius at the specified fillet item. |
| Method | [SetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertexDistance.md) | Sets the setback distances on fillet edges from the specified fillet corner vertex on this simple fillet feature. |
| Method | [SetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertices.md) | Sets the setback vertices for this simple fillet feature. |

[Top](#top)

 

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.md)  
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.md)  
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.md)  
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)

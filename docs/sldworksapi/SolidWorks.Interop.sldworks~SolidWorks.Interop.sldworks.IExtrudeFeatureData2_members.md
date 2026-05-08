# IExtrudeFeatureData2 Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members`

Allows access to an extrusion feature.
The following tables list the members exposed by [IExtrudeFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AssemblyFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AssemblyFeatureScope.md) | Gets or sets whether to use scope for this assembly extrude feature. |
| Property | [AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.md) | Gets or sets whether to automatically select all or only specific bodies for the extrude feature to affect in the multibody part. |
| Property | [AutoSelectComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelectComponents.md) | Gets or sets whether to auto-select all components that this assembly extrude feature affects in model. |
| Property | [BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~BothDirections.md) | Gets or sets whether the extrusion is in both directions. |
| Property | [CapEnds](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapEnds.md) | Caps the ends for a thin base extrude feature. |
| Property | [CapThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapThickness.md) | Gets or sets the end cap thickness for a thin base extrude feature. |
| Property | [Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.md) | Gets and sets the selected contours in this extrude feature. |
| Property | [FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScope.md) | Gets or sets whether to use scope for the extrude feature in a multibody part. |
| Property | [FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScopeBodies.md) | Gets or sets the solid bodies that the extrude feature affects in a multibody part. |
| Property | [FlipSideToCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FlipSideToCut.md) | Gets or sets whether to flip the side to cut. |
| Property | [FromOffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.md) | Gets or sets the offset distance if [IExtrudeFeatureData2::FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md) is swExtrudeFrom\_Offset. |
| Property | [FromOffsetReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.md) | Gets or sets whether the offset is reverse for this extrusion if [IExtrudeFeatureData2::FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md)  is swExtrudeFrom\_Offset. |
| Property | [FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md) | Gets or sets the type from which to create an extrusion. |
| Property | [LinkToThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~LinkToThickness.md) | Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature. |
| Property | [Merge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Merge.md) | Gets or sets whether to merge the results of the extrude feature in a multibody part. |
| Property | [NormalCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~NormalCut.md) | Gets or sets whether the cut is created normal to the thickness of the sheet metal part. |
| Property | [OptimizeGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~OptimizeGeometry.md) | Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part. |
| Property | [PropagateFeatureToParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~PropagateFeatureToParts.md) | Gets whether to propagate this assembly extrude feature to the parts that it affects in this model. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ReverseDirection.md) | Gets or sets whether to reverse the direction of the extrusion feature. |
| Property | [ThinWallType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ThinWallType.md) | Gets or sets the thin wall type for a thin base extrude feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AccessSelections.md) | Gains access to the selections used to define the extrusion feature. |
| Method | [GetAutoFilletCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletCorners.md) | Gets whether the corners of this thin feature are automatically filleted. |
| Method | [GetAutoFilletRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletRadius.md) | Gets the automatic corner fillet radius for this thin feature. |
| Method | [GetContoursCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetContoursCount.md) | Gets the number of selected contours for this extrude feature. |
| Method | [GetDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDepth.md) | Gets the depth of the extrusion feature in the forward or reverse direction. |
| Method | [GetDirectionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDirectionReference.md) | Gets the direction of the extrusion. |
| Method | [GetDraftAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.md) | Gets the draft angle of the extrusion in the forward or reverse direction. |
| Method | [GetDraftOutward](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.md) | Gets whether the extrusion feature is drafted outward in the forward or reverse direction. |
| Method | [GetDraftWhileExtruding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.md) | Gets whether the feature is drafted while extruding in the forward or reverse direction. |
| Method | [GetEndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.md) | Gets the type of end condition of this extrusion feature for forward or reverse direction. |
| Method | [GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md) | Gets the reference entity defining the end condition in the forward or reverse direction. |
| Method | [GetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFace.md) | Obsolete. Superseded by [IExtrudeFeatureData2::GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md). |
| Method | [GetFeatureScopeBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFeatureScopeBodiesCount.md) | Gets the number of solid bodies affected by the extrude feature in a multibody part. |
| Method | [GetFromEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFromEntity.md) | Gets the entity and its type from which the extrusion was created. |
| Method | [GetReverseOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetReverseOffset.md) | Gets the offset direction for this extrude feature. |
| Method | [GetTranslateSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetTranslateSurface.md) | Gets the translate surface setting for this extrude feature. |
| Method | [GetVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetVertex.md) | Obsolete. Superseded by [IExtrudeFeatureData2::GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md). |
| Method | [GetWallThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetWallThickness.md) | Gets the wall thickness of the thin extrusion feature in forward or reverse direction. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IAccessSelections.md) | Gains access to the selections used to define the extrusion feature. |
| Method | [IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.md) | Gets the selected contours for this extrude feature. |
| Method | [IGetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetFace.md) | Obsolete. Superseded by [IExtrudeFeatureData2::GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md). |
| Method | [IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetFeatureScopeBodies.md) | Gets the solid bodies that the extrude feature affects in a multibody part. |
| Method | [IGetVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetVertex.md) | Obsolete. Superseded by [IExtrudeFeatureData2::GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md). |
| Method | [IsBaseExtrude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsBaseExtrude.md) | Obsolete. Superseded by [IFeature::IsBase2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsBase2.md). |
| Method | [IsBossFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsBossFeature.md) | Gets whether the extrusion is a boss feature. |
| Method | [ISetChangeToConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetChangeToConfigurations.md) | Applies changes made to this extrude feature to the specified configurations. |
| Method | [ISetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetContours.md) | Sets the selected contours for this extrude feature. |
| Method | [ISetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetFace.md) | Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md). |
| Method | [ISetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetFeatureScopeBodies.md) | Sets the solid bodies that the extrude feature affects in the multibody part. |
| Method | [ISetVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetVertex.md) | Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md). |
| Method | [IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.md) | Gets whether the extrusion is a thin feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ReleaseSelectionAccess.md) | Releases access to the selections used to define the extrude feature. |
| Method | [SetAutoFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetAutoFillet.md) | Sets the automatic corner fillet properties of this thin feature. |
| Method | [SetChangeToConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetChangeToConfigurations.md) | Applies changes made to this extrude feature to the specified configurations. |
| Method | [SetDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDepth.md) | Sets the depth of the feature in the forward or reverse direction. |
| Method | [SetDirectionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDirectionReference.md) | Sets the direction of the extrusion. |
| Method | [SetDraftAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.md) | Sets the draft angle of the extrusion in the forward or reverse direction. |
| Method | [SetDraftOutward](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.md) | Sets whether the extrusion feature should draft outward in the forward or reverse direction. |
| Method | [SetDraftWhileExtruding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.md) | Sets whether the feature is drafted while extruding in the forward or reverse direction. |
| Method | [SetEndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.md) | Sets the end condition type of the extrusion feature for the forward or reverse direction. |
| Method | [SetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md) | Sets the reference entity that defines the end condition in a forward or reverse direction. |
| Method | [SetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetFace.md) | Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md). |
| Method | [SetFromEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetFromEntity.md) | Sets the entity from which to create an extrusion. |
| Method | [SetReverseOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetReverseOffset.md) | Sets the offset direction for this extrude feature. |
| Method | [SetTranslateSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetTranslateSurface.md) | Sets the translate surface setting for this extrude feature. |
| Method | [SetVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetVertex.md) | Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md). |
| Method | [SetWallThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetWallThickness.md) | Sets the wall thickness of the thin extrusion feature in a forward or reverse direction. |

[Top](#top)

 

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::FeatureCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut2.md)  
[IFeatureManager::FeatureCutThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThin.md)  
[IFeatureManager::FeatureExtrusion2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusion2.md)  
[IFeatureManager::FeatureExtrusionThin2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2.md)

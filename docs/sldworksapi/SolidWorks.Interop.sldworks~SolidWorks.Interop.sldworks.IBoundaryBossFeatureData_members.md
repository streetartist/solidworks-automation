# IBoundaryBossFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members`

Allows access to a boundary feature that is a boss or base.
The following tables list the members exposed by [IBoundaryBossFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~AutoSelect.md) | Gets or sets whether to automatically select all or only specific bodies for the boundary feature to affect in the multibody part. |
| Property | [D1CurveInfluence](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1CurveInfluence.md) | Gets or sets the type of curve influence for Direction 1 for this boundary feature. |
| Property | [D1Curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.md) | Gets or sets the curves for Direction 1 for this boundary feature. |
| Property | [D2CurveInfluence](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2CurveInfluence.md) | Gets or sets the type of curve influence for Direction 2 for this boundary feature. |
| Property | [D2Curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.md) | Gets or sets the curves for Direction 2 for this boundary feature. |
| Property | [FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScope.md) | Gets or sets whether to use scope for the boundary feature in a multibody part. |
| Property | [FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodies.md) | Gets or sets the bodies that this boundary feature affects in a multibody part. |
| Property | [FeatureScopeBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodiesCount.md) | Gets the number of bodies that this boundary feature affects in a multibody part. |
| Property | [MergeResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeResult.md) | Gets or sets whether to merge all boundary feature elements. |
| Property | [MergeTangentFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeTangentFaces.md) | Gets or sets whether to make the surfaces in the resulting boundary feature tangent if the corresponding boundary segments are tangent. |
| Property | [ThinFeatureReversed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureReversed.md) | Gets whether this thin feature boundary feature is reversed. |
| Property | [ThinFeatureThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureThickness.md) | Gets or sets the thickness of this thin feature boundary feature. |
| Property | [ThinFeatureType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureType.md) | Gets or sets the type of thin feature for this boundary feature. |
| Property | [TrimByD1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~TrimByD1.md) | Gets whether to trim surfaces in Direction 1 when curves do not form a closed boundary feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~AccessSelections.md) | Gains access to the selections that define this boundary feature. |
| Method | [GetAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetAlignmentType.md) | Gets the type of alignment for the specified curve in the specified direction for this boundary feature. |
| Method | [GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.md) | Gets the number of curves in the specified direction in this boundary feature. |
| Method | [GetDirectionVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDirectionVector.md) | Gets the entity used as the direction vector for the specified curve in the specified direction in this boundary feature. |
| Method | [GetDraftAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDraftAngle.md) | Gets the draft angle for the specified curve in the specified direction in this boundary feature. |
| Method | [GetDraftAngleReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDraftAngleReverseDirection.md) | Gets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | [GetGuideTangencyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.md) | Gets the type of tangency for the specified curve in the specified direction in this boundary feature. |
| Method | [GetTangentApplyToAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentApplyToAll.md) | Gets whether one handle that controls all constraints for the entire profile is displayed for the specified curve in the specified direction in this boundary feature. |
| Method | [GetTangentDirectionReversed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentDirectionReversed.md) | Gets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | [GetTangentInfluence](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.md) | Gets the curve influence for the specified curve in the specified direction in this boundary feature. |
| Method | [GetTangentLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentLength.md) | Gets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature. |
| Method | [IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~IsThinFeature.md) | Gets whether the boundary feature is a thin feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections for this boundary feature. |
| Method | [SetAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetAlignmentType.md) | Sets the type of alignment for the specified curve in the specified direction for this boundary feature. |
| Method | [SetDirectionVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDirectionVector.md) | Sets the entity to use as the direction vector for the specified curve in the specified direction in this boundary feature. |
| Method | [SetDraftAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngle.md) | Sets the draft angle for the specified curve in the specified direction in this boundary feature. |
| Method | [SetDraftAngleReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngleReverseDirection.md) | Sets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | [SetGuideTangencyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetGuideTangencyType.md) | Sets the type of tangency for the specified curve in the specified direction in this boundary feature. |
| Method | [SetTangentApplyToAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentApplyToAll.md) | Sets whether to display one handle that controls all constraints for the entire profile for the specified curve in the specified direction in this boundary feature. |
| Method | [SetTangentDirectionReversed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentDirectionReversed.md) | Sets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | [SetTangentInfluence](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.md) | Sets the curve influence toward the next curve for the specified curve in the specified direction in this boundary feature. |
| Method | [SetTangentLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentLength.md) | Sets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature. |

[Top](#top)

 

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertNetBlend Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertNetBlend.md)  
[IFeatureManager::SetNetBlendCurveData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendCurveData.md)  
[IFeatureManager::SetNetBlendDirectionData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData.md)

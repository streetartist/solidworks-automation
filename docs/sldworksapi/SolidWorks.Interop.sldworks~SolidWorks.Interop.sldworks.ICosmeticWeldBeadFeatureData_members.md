# ICosmeticWeldBeadFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members`

Allows access to a cosmetic weld bead feature.
The following tables list the members exposed by [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [BeadSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~BeadSize.md) | Gets or sets the thickness of a weld bead. |
| Property | [FromToLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength.md) | Gets or sets whether to enable the from/to length properties. |
| Property | [FromToReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToReverse.md) | Gets or sets whether to start the weld from the opposite end. |
| Property | [FromToStartPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint.md) | Gets or sets the position of the first weld bead with respect to the end of the selected face or edge. |
| Property | [FromToWeldLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToWeldLength.md) | Gets or sets the length of the weld. |
| Property | [Gap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Gap.md) | Gets or sets the gap between intermittent weld beads. |
| Property | [GapOrPitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch.md) | Gets or sets whether to use gap or pitch spacing for intermittent weld beads. |
| Property | [IntermittentWeld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.md) | Gets or sets whether to enable intermittent weld properties. |
| Property | [IntermittentWeldLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeldLength.md) | Gets or sets the length of the weld for intermittent weld beads. |
| Property | [Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Pitch.md) | Gets or sets the pitch of intermittent weld beads. |
| Property | [Side](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Side.md) | Gets or sets how the weld bead is applied to selected faces or edges. |
| Property | [Staggered](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Staggered.md) | Gets or sets whether to alternate the positioning of the weld beads on both sides of the weld body. |
| Property | [TangentPropagation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~TangentPropagation.md) | Gets or sets whether to apply the weld bead to all edges that are tangent to the selected faces or edges. |
| Property | [WeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~WeldSymbol.md) | Gets or sets the weld symbol for this weld bead. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~AccessSelections.md) | Gains access to the selections that define this cosmetic weld bead feature. |
| Method | [GetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntities.md) | Obsolete. Superseded by [ICosmeticWeldBeadFeatureData::GetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.md) and [ICosmeticWeldBeadFeatureData::GetEntitiesWeldTo.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo.md) |
| Method | [GetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.md) | Gets the weld-from entity type and weld-from entities for this cosmetic weld bead, which was created using weld geometry. |
| Method | [GetEntitiesWeldPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldPath.md) | Gets the entities for this cosmetic weld bead, which was created using a weld path. |
| Method | [GetEntitiesWeldTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo.md) | Gets the weld-to entity type and weld-to entities for this cosmetic weld bead, which was created using weld geometry. |
| Method | [GetReferenceEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetReferenceEdges.md) | Gets the reference edges created by this cosmetic weld bead feature. |
| Method | [GetWeldBeadFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetWeldBeadFolder.md) | Gets the weld bead folder. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that define this cosmetic weld bead feature. |
| Method | [SetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntities.md) | Obsolete. Superseded by [ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.md) and [ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.md) |
| Method | [SetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.md) | Sets the weld-from entities for this cosmetic weld bead, which was created using weld geometry. |
| Method | [SetEntitiesWeldPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldPath.md) | Sets the entities for this cosmetic weld bead, which was created using a weld path. |
| Method | [SetEntitiesWeldTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.md) | Sets the weld-to entities for this cosmetic weld bead, which was created using weld geometry. |

[Top](#top)

 

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ICosmeticWeldBeadFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder.md)  
[IFeatureManager::InsertCosmeticWeldBead2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2.md)

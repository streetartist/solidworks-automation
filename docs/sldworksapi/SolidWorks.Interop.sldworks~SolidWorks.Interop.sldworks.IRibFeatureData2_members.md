# IRibFeatureData2 Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members`

Allows access to a rib feature.
The following tables list the members exposed by [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~Body.md) | Gets or sets the body where the rib is created. |
| Property | [DraftAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftAngle.md) | Gets or sets the draft angle for the rib. |
| Property | [DraftFromWall](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftFromWall.md) | Gets or sets whether to draft the rib from the wall interface or the sketch plane. |
| Property | [DraftOutward](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftOutward.md) | Gets or sets whether the rib has an outward draft. |
| Property | [EnableDraft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~EnableDraft.md) | Gets or sets whether the rib has an associated draft. |
| Property | [ExtrusionDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ExtrusionDirection.md) | Gets or sets the direction in which to extrude the rib. |
| Property | [FlipSide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~FlipSide.md) | Gets or sets whether material is added to the reverse side of the rib. |
| Property | [IsTwoSided](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~IsTwoSided.md) | Gets or sets whether the rib is created on two sides of the midplane or in a single direction (see [IRibFeatureData2::ReverseThicknessDir](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ReverseThicknessDir.md)). |
| Property | [RefSketchIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~RefSketchIndex.md) | Gets or sets which sketch segment defines the draft direction of the rib feature. |
| Property | [ReverseThicknessDir](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ReverseThicknessDir.md) | Gets or sets whether the extrusion is on the reverse side of this single-sided rib. |
| Property | [Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~Thickness.md) | Gets or set the overall thickness of the rib. |
| Property | [Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~Type.md) | Gets or sets the type of rib. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~AccessSelections.md) | Gains access to the the selections for this rib feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~IAccessSelections.md) | Gains access to the the selections for this rib feature. |
| Method | [NextReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~NextReference.md) | Cycles through the possible sketch entities that can be used to define the draft, if it is used, for ribs with multiple contours. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ReleaseSelectionAccess.md) | Releases access to the selections that define this rib feature. |

[Top](#top)

 

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertRib Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRib.md)

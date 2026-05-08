# IIndentFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members`

Allows access to an indent feature.
The following tables list the members exposed by [IIndentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance.md) | Gets or sets the clearance between the target and tool bodies in this indent feature. |
| Property | [ClearanceDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ClearanceDirection.md) | Gets or sets the direction of the [clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance.md) for this indent feature. |
| Property | [CutDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~CutDirection.md) | Gets or sets whether to flip the side of the cut for this indent feature. |
| Property | [IsCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.md) | Gets or sets whether to remove the intersection area of the [target body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.md). |
| Property | [SelectionState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~SelectionState.md) | Gets or sets the side of the model to keep or remove. |
| Property | [TargetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.md) | Gets or sets the solid or surface body to indent. |
| Property | [Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Thickness.md) | Gets or sets the thickness of the indent feature. |
| Property | [ToolBodyRegion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.md) | Gets or sets the tool body region for the indent feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~AccessSelections.md) | Gains access to the selections that define this indent feature. |
| Method | [GetBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~GetBodiesCount.md) | Gets the number of solid or surface [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) for the [tool body region](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.md). |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections for this indent feature. |

[Top](#top)

 

See Also

#### Reference

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertIndent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertIndent.md)

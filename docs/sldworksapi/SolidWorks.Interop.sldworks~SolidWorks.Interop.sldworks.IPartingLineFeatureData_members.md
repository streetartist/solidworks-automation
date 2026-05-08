# IPartingLineFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members`

Allows access to a parting line feature.
The following tables list the members exposed by [IPartingLineFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~Angle.md) | Gets or sets the draft angle for the parting line. |
| Property | [CoreCavitySplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~CoreCavitySplit.md) | Gets or sets the core/cavity split option for a parting line. |
| Property | [PartingLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PartingLines.md) | Gets and sets the edges for the parting lines. |
| Property | [PullDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirection.md) | Gets whether the direction of pull is reversed. |
| Property | [PullDirectionBase](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionBase.md) | Gets or sets the direction of pull for the parting line feature. |
| Property | [PullDirectionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.md) | Gets the type of entity indicating the direction of pull. |
| Property | [SplitFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFaces.md) | Gets or sets whether to split faces. |
| Property | [SplitFacesOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFacesOption.md) | Gets or sets the split faces option for this parting line. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~AccessSelections.md) | Gains access to the selections that describe the parting line feature. |
| Method | [DraftAnalysis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.md) | Performs draft analysis for the input angle and the direction of pull. |
| Method | [GetEntitiesToSplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplit.md) | Gets the entities that are used to split a face. |
| Method | [GetEntitiesToSplitCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplitCount.md) | Gets the number of entities to use to split a face and add edges to the parting line feature. |
| Method | [GetFacesByType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType.md) | Gets the specified faces after performing a draft analysis of the parting line feature. |
| Method | [GetFacesByTypeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount.md) | Gets the number of faces of the specified type for this parting line. |
| Method | [GetPartingLinesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetPartingLinesCount.md) | Gets the number of edges used as parting lines. |
| Method | [IGetEntitiesToSplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetEntitiesToSplit.md) | Gets the entities that are used to split a face. |
| Method | [IGetFacesByType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType.md) | Gets the specified faces after performing a draft analysis of the parting line feature. |
| Method | [IGetPartingLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetPartingLines.md) | Gets the edges used as parting lines. |
| Method | [ISetEntitiesToSplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetEntitiesToSplit.md) | Sets the entities to use to split a face and add edges to the parting line feature. |
| Method | [ISetPartingLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetPartingLines.md) | Sets the edges to use as parting lines. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that define this parting line feature. |
| Method | [SetEntitiesToSplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SetEntitiesToSplit.md) | Sets the entities to use to split a face and add edges to the parting line feature. |
| Method | [Status](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~Status.md) | Gets the status of this parting line feature. |

[Top](#top)

 

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertMoldPartingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.md)  
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)  
[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)

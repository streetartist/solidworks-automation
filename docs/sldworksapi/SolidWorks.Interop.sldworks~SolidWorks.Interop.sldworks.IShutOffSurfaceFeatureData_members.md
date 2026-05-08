# IShutOffSurfaceFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members`

Allows access to a shut-off surface feature.
The following tables list the members exposed by [IShutOffSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Edges.md) | Gets or sets the edges that form closed loops for the patches. |
| Property | [Knit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Knit.md) | Gets or sets whether to knit the patches in this shut-off surface feature. |
| Property | [LoopEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.md) | Gets the edges in the specified loop in this shut-off surface feature. |
| Property | [LoopPatchType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.md) | Gets and sets the type of patch for the specified loop for this shut-off surface feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~AccessSelections.md) | Gains access to the selections that define this shut-off surface feature. |
| Method | [FlipFaceTangentTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~FlipFaceTangentTo.md) | Indicates to create the patch on the opposite tangent face. |
| Method | [GetEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetEdgeCount.md) | Gets the number of edges that form a closed loop. |
| Method | [GetFaceTangentTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetFaceTangentTo.md) | Gets the tangent face for the specified loop where to create the patch. |
| Method | [GetLoopCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopCount.md) | Gets the number of closed loops for all of the patches. |
| Method | [GetLoopEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount.md) | Gets the number of edges in the specified loop. |
| Method | [IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetEdges.md) | Gets the edges that form closed loops to use for the patches. |
| Method | [IGetLoopEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.md) | Gets the edges in the specified loop. |
| Method | [ISetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~ISetEdges.md) | Sets the edges to use to form closed loops for patches. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that define this shut-off surface feature. |
| Method | [SetAllPatchTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.md) | Sets the type of patch for all loops for this shut-off surface feature. |
| Method | [Status](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Status.md) | Gets the status of the shut-off surface feature. |

[Top](#top)

 

See Also

#### Reference

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertMoldShutOffSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.md)

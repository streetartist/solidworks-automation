# IIntersectFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members`

Allows access to an intersect feature.
The following tables list the members exposed by [IIntersectFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CapPlanar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~CapPlanar.md) | Gets or sets whether to close the flat openings of surfaces. |
| Property | [Consume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~Consume.md) | Gets or sets whether to remove input surfaces from the FeatureManager design tree. |
| Property | [Merge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~Merge.md) | Gets or sets whether to merge included regions into one body. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~AccessSelections.md) | Gains access to the selections that define this intersect feature. |
| Method | [GetIntersections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersections.md) | Gets the intersect regions in this intersect feature. |
| Method | [GetIntersectionsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsCount.md) | Gets the number of intersect regions in this intersect feature. |
| Method | [GetIntersectionsTools](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools.md) | Gets the intersecting solids, surfaces, and planes in this intersect feature. |
| Method | [GetIntersectionsToolsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsToolsCount.md) | Gets the number of solids, surfaces, and planes used to create this intersect feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections for this intersect feature. |
| Method | [SetIntersections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersections.md) | Specifies which of the intersect regions to exclude from this intersect feature. |
| Method | [SetIntersectionsTools](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersectionsTools.md) | Specifies the intersecting solids, surfaces, and planes for this intersect feature. |

[Top](#top)

 

See Also

#### Reference

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::PostIntersect Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostIntersect.md)  
[IFeatureManager::PreIntersect Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect.md)

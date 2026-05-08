# IStructuralMemberFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members`

Allows access to a structural member.
The following tables list the members exposed by [IStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AllowProtrusion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~AllowProtrusion.md) | Gets or sets whether to allow protrusion. |
| Property | [ApplyCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.md) | Gets or sets whether or not to apply a corner treatment to this structural member. |
| Property | [ConfigurationName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConfigurationName.md) | Gets or sets the name of the configuration in the custom weldment profile for this structural member. |
| Property | [ConnectedSegmentsOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectedSegmentsOption.md) | Gets or sets the connected segments option. |
| Property | [ConnectionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType.md) | Gets or sets the type of corner treatment at the specified connection point of this structural member. |
| Property | [CornerTreatmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.md) | Gets or sets the type of corner treatment for this structural member. |
| Property | [Groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.md) | Gets or sets the groups to use in this structural member. |
| Property | [LibraryProfileMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LibraryProfileMaterial.md) | Gets the name of the material for the library profile for this structural member. |
| Property | [LocateProfilePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LocateProfilePoint.md) | Gets or sets the point to use to locate the profile for this structural member. |
| Property | [PathSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~PathSegments.md) | Gets the path segments used or sets the path segments to use to create this structural member. |
| Property | [RotationAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~RotationAngle.md) | Gets or sets the angle by which the structural member turns relative to the adjacent structural member. |
| Property | [TransferMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~TransferMaterial.md) | Gets or sets whether to transfer the [material properties of a library profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LibraryProfileMaterial.md) for this structural member. |
| Property | [WeldmentProfilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~WeldmentProfilePath.md) | Gets or sets the path for the profile for this structural member. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~AccessSelections.md) | Gains access to the selections that define this structural member. |
| Method | [GetConnectionPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.md) | Gets the connection points for this structural member. |
| Method | [GetConnectionPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount.md) | Gets the number of sketch points for this structural member. |
| Method | [GetGroupsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.md) | Gets the number of structural-member groups for this structural member. |
| Method | [GetPathSegmentAt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentAt.md) | Gets the sketch segment associated with the body of this structural member. |
| Method | [GetPathSegmentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentsCount.md) | Gets the number of path segments for this structural member. |
| Method | [GetSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetSketchSegments.md) | Gets the sketch segments that define the path of the specified structural member body. |
| Method | [IGetConnectionPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.md) | Gets the connection points for this structural member. |
| Method | [IGetGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.md) | Gets the structural-member groups in this structural member. |
| Method | [IGetPathSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetPathSegments.md) | Gets the path segments used to create this structural member. |
| Method | [ISetGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.md) | Sets the structural-member groups to use in this structural member. |
| Method | [ISetPathSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetPathSegments.md) | Sets the path segments to use to create this structural member. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that define this structural member. |

[Top](#top)

 

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)  
[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md)  
[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md)  
[IFeatureManager::InsertStructuralWeldment3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.md)  
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)

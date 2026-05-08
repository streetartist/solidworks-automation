# IMirrorPatternFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members`

Allows access to a mirror pattern feature.
The following tables list the members exposed by [IMirrorPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScope.md) | Gets or sets whether to use scope for the mirror pattern feature in a multibody part. |
| Property | [FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScopeBodies.md) | Gets or sets the solid bodies that the mirror pattern feature affects in a multibody part. |
| Property | [GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GeometryPattern.md) | Gets or sets whether to mirror only the geometry (faces and edges) of the feature for this mirror pattern feature. |
| Property | [MirrorFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~MirrorFaceArray.md) | Gets or sets the faces to mirror. |
| Property | [PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~PatternFeatureArray.md) | Gets or sets the seed features to use to create the mirror pattern. |
| Property | [Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~Plane.md) | Gets or sets the plane about which to mirror the part. |
| Property | [PropagateVisualProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~PropagateVisualProperty.md) | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all pattern instances. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~AccessSelections.md) | Gains access to the selections that define the mirror pattern feature. |
| Method | [GetFeatureScopeBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetFeatureScopeBodiesCount.md) | Gets the number of solid bodies affected by the mirror pattern feature in a multibody part. |
| Method | [GetMirrorFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetMirrorFaceCount.md) | Gets the number of mirrored faces. |
| Method | [GetMirrorPlaneType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetMirrorPlaneType.md) | Gets whether the mirror plane is a face or a reference plane. |
| Method | [GetPatternFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetPatternFeatureCount.md) | Gets the number of seed features used to create this mirror pattern. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IAccessSelections.md) | Obsolete. Superseded by [IMirrorPatternFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IAccessSelections2.md). |
| Method | [IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IAccessSelections2.md) | Gains access to the selections that define the mirror pattern feature. |
| Method | [IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetFeatureScopeBodies.md) | Gets the solid bodies that the mirror pattern feature affects in a multibody part. |
| Method | [IGetMirrorFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetMirrorFaceArray.md) | Gets the mirrored faces. |
| Method | [IGetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetPatternFeatureArray.md) | Gets the seed features used to create the mirror pattern. |
| Method | [ISetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetFeatureScopeBodies.md) | Sets the solid bodies that the mirror pattern feature affects in a multibody part. |
| Method | [ISetMirrorFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetMirrorFaceArray.md) | Sets the faces to mirror. |
| Method | [ISetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetPatternFeatureArray.md) | Sets the seed features to use to create this mirror pattern feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections used to define the mirror pattern feature. |

[Top](#top)

 

See Also

#### Reference

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeature::InsertMirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature.md)

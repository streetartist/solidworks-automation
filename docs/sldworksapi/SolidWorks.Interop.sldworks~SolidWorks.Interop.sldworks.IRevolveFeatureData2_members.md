# IRevolveFeatureData2 Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members`

Allows access to a revolve feature.
The following tables list the members exposed by [IRevolveFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AssemblyFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AssemblyFeatureScope.md) | Gets or sets whether to use scope for this assembly revolve feature. |
| Property | [AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelect.md) | Gets or sets whether to automatically select all or only specific bodies for the revolve feature to affect in a multibody body. |
| Property | [AutoSelectComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelectComponents.md) | Gets or sets whether to auto-select all components that this assembly revolve feature affects in model. |
| Property | [Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Axis.md) | Gets or sets the axis of revolution for this revolve feature. |
| Property | [Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.md) | Gets and sets the selected contours on this revolve feature. |
| Property | [FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~FeatureScope.md) | Gets or sets whether to use scope for the revolve feature in a multibody part. |
| Property | [FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~FeatureScopeBodies.md) | Gets or sets the solid bodies that the revolve feature affects in a multibody part. |
| Property | [Merge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Merge.md) | Gets or sets whether to merge the results of this revolve feature in a multibody part. |
| Property | [PropagateFeatureToParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~PropagateFeatureToParts.md) | Gets whether to propagate this assembly revolve feature to the parts that it affects in this model. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ReverseDirection.md) | Gets or sets whether the direction of the revolution feature should be reversed. |
| Property | [ThinWallType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ThinWallType.md) | Gets and sets the thin wall type for a thin revolve feature. |
| Property | [Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Type.md) | Gets or sets the revolution feature type. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AccessSelections.md) | Gains access to the selections that define this revolve feature. |
| Method | [GetAxisType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetAxisType.md) | Gets the type of axis of revolution for this revolve feature. |
| Method | [GetContoursCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetContoursCount.md) | Gets the number of selected contours for this revolve feature. |
| Method | [GetFeatureScopeBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetFeatureScopeBodiesCount.md) | Gets the number of solid bodies affected by the revolve feature in a multibody part. |
| Method | [GetRevolutionAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetRevolutionAngle.md) | Gets the angle of the revolve feature in Direction 1 or Direction 2. |
| Method | [GetWallThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetWallThickness.md) | Gets the wall thickness of the thin revolution feature in forward or reverse direction. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IAccessSelections.md) | Gains access to the selections that define this revolve feature. |
| Method | [IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetContours.md) | Gets the selected contours for this revolve feature. |
| Method | [IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetFeatureScopeBodies.md) | Gets the solid bodies that the revolve feature affects in a multibody part. |
| Method | [IsBossFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsBossFeature.md) | Gets whether the revolution is a boss feature. |
| Method | [ISetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetContours.md) | Sets the selected contours for this revolve feature. |
| Method | [ISetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetFeatureScopeBodies.md) | Sets the solid bodies that the revolve feature affects in a multibody part. |
| Method | [IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.md) | Gets whether the revolution is a thin feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ReleaseSelectionAccess.md) | Releases access to the selections that define this revolve feature. |
| Method | [SetRevolutionAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle.md) | Sets the angle of the revolve feature in Direction 1 or Direction 2. |
| Method | [SetWallThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetWallThickness.md) | Sets the wall thickness of the thin revolution feature in forward/reverse direction. |

[Top](#top)

 

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::FeatureRevolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve.md)  
[IFeatureManager::FeatureRevolveCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.md)  
[IFeatureManager::FeatureRevolveThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.md)  
[IFeatureManager::FeatureRevolveThinCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.md)

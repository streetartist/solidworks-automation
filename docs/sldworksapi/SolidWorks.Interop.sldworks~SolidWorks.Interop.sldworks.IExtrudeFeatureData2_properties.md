# IExtrudeFeatureData2 Interface Properties

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_properties`

Allows access to an extrusion feature.
For a list of all members of this type, see [IExtrudeFeatureData2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AssemblyFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AssemblyFeatureScope.md) | Gets or sets whether to use scope for this assembly extrude feature. |
| Property | [AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.md) | Gets or sets whether to automatically select all or only specific bodies for the extrude feature to affect in the multibody part. |
| Property | [AutoSelectComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelectComponents.md) | Gets or sets whether to auto-select all components that this assembly extrude feature affects in model. |
| Property | [BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~BothDirections.md) | Gets or sets whether the extrusion is in both directions. |
| Property | [CapEnds](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapEnds.md) | Caps the ends for a thin base extrude feature. |
| Property | [CapThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapThickness.md) | Gets or sets the end cap thickness for a thin base extrude feature. |
| Property | [Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.md) | Gets and sets the selected contours in this extrude feature. |
| Property | [FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScope.md) | Gets or sets whether to use scope for the extrude feature in a multibody part. |
| Property | [FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScopeBodies.md) | Gets or sets the solid bodies that the extrude feature affects in a multibody part. |
| Property | [FlipSideToCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FlipSideToCut.md) | Gets or sets whether to flip the side to cut. |
| Property | [FromOffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.md) | Gets or sets the offset distance if [IExtrudeFeatureData2::FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md) is swExtrudeFrom\_Offset. |
| Property | [FromOffsetReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.md) | Gets or sets whether the offset is reverse for this extrusion if [IExtrudeFeatureData2::FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md)  is swExtrudeFrom\_Offset. |
| Property | [FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md) | Gets or sets the type from which to create an extrusion. |
| Property | [LinkToThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~LinkToThickness.md) | Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature. |
| Property | [Merge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Merge.md) | Gets or sets whether to merge the results of the extrude feature in a multibody part. |
| Property | [NormalCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~NormalCut.md) | Gets or sets whether the cut is created normal to the thickness of the sheet metal part. |
| Property | [OptimizeGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~OptimizeGeometry.md) | Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part. |
| Property | [PropagateFeatureToParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~PropagateFeatureToParts.md) | Gets whether to propagate this assembly extrude feature to the parts that it affects in this model. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ReverseDirection.md) | Gets or sets whether to reverse the direction of the extrusion feature. |
| Property | [ThinWallType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ThinWallType.md) | Gets or sets the thin wall type for a thin base extrude feature. |

[Top](#top)

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::FeatureCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut2.md)  
[IFeatureManager::FeatureCutThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThin.md)  
[IFeatureManager::FeatureExtrusion2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusion2.md)  
[IFeatureManager::FeatureExtrusionThin2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2.md)

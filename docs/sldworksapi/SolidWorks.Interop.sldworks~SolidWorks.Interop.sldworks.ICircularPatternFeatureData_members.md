# ICircularPatternFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members`

Allows access to a circular pattern feature.
The following tables list the members exposed by [ICircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AutoSelect.md) | Gets whether to automatically select all bodies in a multibody part intersected by this circular pattern feature. |
| Property | [Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Axis.md) | Gets or sets the entity used to determine the direction of this circular pattern feature. |
| Property | [BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~BodyPattern.md) | Gets or sets whether to base this circular pattern feature on bodies and structure systems or features and faces. |
| Property | [Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Direction2.md) | Gets or sets whether to create a bidirectional circular pattern feature. |
| Property | [EqualSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing.md) | Gets or sets whether the pattern instances in Direction 1 are equally spaced in this circular pattern feature. |
| Property | [EqualSpacing2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing2.md) | Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular pattern feature. |
| Property | [FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScope.md) | Gets which bodies in this multibody part are affected by this circular pattern feature. |
| Property | [FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScopeBodies.md) | Gets the bodies in this multibody part that are affected by this circular pattern feature. |
| Property | [GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GeometryPattern.md) | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature. |
| Property | [InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.md) | Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature. |
| Property | [PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternBodyArray.md) | Gets or sets a list of bodies to pattern in a multibody part for this circular pattern feature. |
| Property | [PatternElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternElement.md) | Gets or sets the type of entities on which to base this circular pattern feature. |
| Property | [PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternFaceArray.md) | Gets or sets the list of faces to pattern for this circular pattern feature. |
| Property | [PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternFeatureArray.md) | Gets or sets the seed features for the circular pattern feature. |
| Property | [PropagateVisualProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PropagateVisualProperty.md) | Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all pattern instances in this circular pattern feature. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ReverseDirection.md) | Gets or sets whether the direction of the axis should be reversed in this circular pattern feature. |
| Property | [SkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SkippedItemArray.md) | Gets or sets the list of items to skip in this circular pattern feature. |
| Property | [Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing.md) | Gets or sets the spacing between pattern instances in Direction 1 of the circular pattern feature. |
| Property | [Spacing2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing2.md) | Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular pattern feature. |
| Property | [StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~StructureSystemToPatternArray.md) | Gets or sets the structure systems to pattern in this circular pattern feature. |
| Property | [Symmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Symmetric.md) | Gets or sets whether to create a symmetric or asymmetric circular pattern feature in Direction 2. |
| Property | [TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances.md) | Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature. |
| Property | [TotalInstances2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances2.md) | Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular pattern feature. |
| Property | [VarySketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~VarySketch.md) | Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AccessSelections.md) | Gains access to selections used to define a circular pattern feature. |
| Method | [GetAxisType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetAxisType.md) | Gets the type of geometry used to determine the direction of this circular pattern. |
| Method | [GetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetInstanceToVaryOptions.md) | Gets the options for varying the spacing of pattern instances in this circular pattern feature. |
| Method | [GetPatternBodyCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternBodyCount.md) | Gets the number of seed bodies in this circular pattern feature. |
| Method | [GetPatternFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternFaceCount.md) | Gets the number of patterned faces. |
| Method | [GetPatternFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternFeatureCount.md) | Gets the number of seed features used to create this circular pattern. |
| Method | [GetSkippedItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetSkippedItemCount.md) | Gets the number of items skipped in this circular pattern. |
| Method | [GetTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetTransform.md) | Gets the transform for the specified instance of this circular-pattern feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IAccessSelections.md) | Obsolete. Superseded by [ICircularPatternFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IAccessSelections2.md). |
| Method | [IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IAccessSelections2.md) | Gains access to selections used to define a circular pattern feature. |
| Method | [IGetPatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternBodyArray.md) | Gets a list of the seed bodies for this circular pattern. |
| Method | [IGetPatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternFaceArray.md) | Gets a list of patterned faces for this circular pattern. |
| Method | [IGetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternFeatureArray.md) | Gets the seed features for this circular pattern. |
| Method | [IGetSkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetSkippedItemArray.md) | Gets an array of integers that represent the skipped items in this circular feature. |
| Method | [ISetPatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternBodyArray.md) | Sets a list of seed bodies for the circular pattern. |
| Method | [ISetPatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternFaceArray.md) | Sets a list of patterned faces for this circular pattern. |
| Method | [ISetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternFeatureArray.md) | Sets the seed features to use to create the circular pattern. |
| Method | [ISetSkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetSkippedItemArray.md) | Sets the list of skipped items in this circular pattern. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that define this circular pattern. |
| Method | [SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetFeatureScope.md) | Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this circular pattern feature. |
| Method | [SetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetInstanceToVaryOptions.md) | Sets the options for varying the spacing of pattern instances in this circular pattern feature. |

[Top](#top)

 

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)

# ILocalCircularPatternFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members`

Allows access to a circular component pattern feature in an assembly.
The following tables list the members exposed by [ILocalCircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Axis.md) | Gets or sets the circular axis for this circular component pattern feature. |
| Property | [Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Direction2.md) | Gets or sets whether to create a bidirectional circular component pattern feature. |
| Property | [EqualSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing.md) | Gets or sets whether to equally space the pattern instances in Direction 1 in this circular component pattern feature. |
| Property | [EqualSpacing2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.md) | Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular component pattern feature. |
| Property | [ForceUseSeedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ForceUseSeedConfiguration.md) | Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local circular pattern feature. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ReverseDirection.md) | Gets or sets whether the direction axis for this local circular pattern is reversed for this circular component pattern feature. |
| Property | [SeedComponentArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SeedComponentArray.md) | Gets or sets an array of seed component features for this circular component pattern feature. |
| Property | [SkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SkippedItemArray.md) | Gets or sets the skipped components in this circular component pattern feature. |
| Property | [Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing.md) | Gets or sets the distance between pattern instances in Direction 1 for this circular component pattern feature. |
| Property | [Spacing2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing2.md) | Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular component pattern feature. |
| Property | [Symmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Symmetric.md) | Gets or sets whether Direction 2 properties are symmetric with those of Direction 1 of this bidirectional circular component pattern feature. |
| Property | [SynchronizeFlexibleComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SynchronizeFlexibleComponents.md) | Gets or sets whether to synchronize the movement of flexible subassembly components in this circular component pattern feature. |
| Property | [TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances.md) | Gets or sets the total number of instances in Direction 1 for this circular component pattern feature. |
| Property | [TotalInstances2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances2.md) | Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular component pattern feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~AccessSelections.md) | Gains access to the selections that define this circular component pattern feature. |
| Method | [GetAxisType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetAxisType.md) | Gets whether the circular axis is a reference axis, edge, or dimension for this circular component pattern feature. |
| Method | [GetModifiedInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstance.md) | Gets the modified values for the specified pattern instance in this circular component pattern feature. |
| Method | [GetModifiedInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstances.md) | Gets the instance numbers of all modified instances in this circular component pattern. |
| Method | [GetSeedComponentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSeedComponentCount.md) | Gets the number of seed component features for this circular component pattern feature. |
| Method | [GetSkippedItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSkippedItemCount.md) | Gets the number of skipped items for this circular component pattern feature. |
| Method | [GetTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetTransform.md) | Gets the transform for the specified instance of this circular component pattern feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IAccessSelections.md) | Obsolete. Superseded by [ILocalCircularPatternFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IAccessSelections2.md). |
| Method | [IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IAccessSelections2.md) | Gains access to the selections that define this circular component pattern feature. |
| Method | [IGetSeedComponentArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSeedComponentArray.md) | Gets an array of seed component features for this circular component pattern feature. |
| Method | [IGetSkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSkippedItemArray.md) | Gets the list of skipped items in this circular component pattern feature. |
| Method | [ISetSeedComponentArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSeedComponentArray.md) | Sets an array of seed component features for this circular component pattern feature. |
| Method | [ISetSkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSkippedItemArray.md) | Sets the list of skipped items for this circular component pattern feature. |
| Method | [ModifyInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ModifyInstance.md) | Modifies the specified pattern instance with the specified angle in this circular component pattern feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections for this circular component pattern feature. |

[Top](#top)

 

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)

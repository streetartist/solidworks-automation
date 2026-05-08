# IBomFeature Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members`

Allows access to the BOM table feature.
The following tables list the members exposed by [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Configuration.md) | Gets or sets the name of configuration for this BOM table. |
| Property | [DetailedCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DetailedCutList.md) | Gets or sets whether to show the detailed cut list in this BOM table. |
| Property | [DisplayAsOneItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DisplayAsOneItem.md) | Gets or sets whether all of the configurations appear with the same item number if the BOM table contains components that have multiple configurations. |
| Property | [DissolvePartLevelRows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows.md) | Gets or sets whether to dissolve weldment part level rows. |
| Property | [FollowAssemblyOrder2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder2.md) | Gets or sets whether the order of the item numbers in the BOM follows the order in which the assembly appears in the FeatureManager design tree. |
| Property | [KeepCurrentItemNumbers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepCurrentItemNumbers.md) | Gets or sets whether item numbers are kept with their components when reordering rows of a BOM table. |
| Property | [KeepMissingItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepMissingItems.md) | Gets and sets the Keep Missing Items option for this BOM feature. |
| Property | [KeepReplacedCompOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepReplacedCompOption.md) | Gets or sets how to replace components when keeping missing items. |
| Property | [Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Name.md) | Gets the name of this BOM table feature. |
| Property | [NumberingTypeOnIndentedBOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~NumberingTypeOnIndentedBOM.md) | Gets and sets the type of numbering for this indented BOM table. |
| Property | [PartConfigurationGrouping](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~PartConfigurationGrouping.md) | Gets and sets the part configuration grouping for this BOM table. |
| Property | [RoutingComponentGrouping](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~RoutingComponentGrouping.md) | Gets or sets the routing component grouping options for this BOM table in a drawing of an assembly containing routing components. |
| Property | [SequenceStartNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SequenceStartNumber.md) | Gets or sets the number with which to start the numbering for this BOM table. |
| Property | [StrikeoutMissingItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~StrikeoutMissingItems.md) | Inserts a horizontal line through missing items in this BOM table (also called strike outs). |
| Property | [TableType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType.md) | Gets and sets the type of table for the Bill of Materials. |
| Property | [ZeroQuantityDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ZeroQuantityDisplay.md) | Gets or sets the character or value to display when a value is 0 in this BOM table. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [FollowAssemblyOrder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder.md) | Obsolete. Superseded by [IBomFeature::FollowAssemblyOrder2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder2.md). |
| Method | [GetConfigurationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurationCount.md) | Gets the number of configurations available to this BOM table or used in this BOM table. |
| Method | [GetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.md) | Gets the configurations available to this BOM table or used in this BOM table. |
| Method | [GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetFeature.md) | Gets the BOM table feature. |
| Method | [GetLinkToDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetLinkToDisplayState.md) | Gets the name of the Display State linked to this BOM feature. |
| Method | [GetReferencedModelName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetReferencedModelName.md) | Gets the name of the model referenced by this BOM feature. |
| Method | [GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotationCount.md) | Gets the number of BOM table annotations for this BOM table feature. |
| Method | [GetTableAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotations.md) | Gets the BOM table annotations for this BOM table feature. |
| Method | [IGetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.md) | Gets the configurations available to this BOM table or used in this BOM table. |
| Method | [IGetTableAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetTableAnnotations.md) | Gets the BOM table annotations for this BOM table feature. |
| Method | [ISetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.md) | Sets the configurations used in this BOM table. |
| Method | [SetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.md) | Sets the configurations used in this BOM table. |
| Method | [SetLinkToDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetLinkToDisplayState.md) | Sets the name of the Display State to which to link this BOM feature. |

[Top](#top)

 

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

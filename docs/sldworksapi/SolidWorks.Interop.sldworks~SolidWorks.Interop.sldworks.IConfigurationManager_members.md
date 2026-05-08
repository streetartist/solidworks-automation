# IConfigurationManager Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members`

Allows access to a configuration in a model.
The following tables list the members exposed by [IConfigurationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [ActiveConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md) | Gets the active configuration. |
| Property | [Document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~Document.md) | Gets the related model document. |
| Property | [EnableConfigurationTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~EnableConfigurationTree.md) | Gets or sets whether to update the ConfigurationManager tree. |
| Property | [LinkDisplayStatesToConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.md) | Gets or sets whether to link or unlink display states to or from the active configuration. |
| Property | [ShowConfigurationDescriptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationDescriptions.md) | Gets or sets whether to display configuration descriptions in ConfigurationManager. |
| Property | [ShowConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationNames.md) | Gets or sets whether to display configuration names in ConfigurationManager. |
| Property | [ShowPreview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowPreview.md) | Gets or sets whether to display the preview of a selected configuration. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddCADFamilyConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.md) | Adds the specified configuration to [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm). |
| Method | [AddConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration.md) | Obsolete. Superseded by [IConfigurationManager::AddConfiguration2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration2.md). |
| Method | [AddConfiguration2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration2.md) | Creates a new configuration. |
| Method | [AddRebuildSaveMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.md) | Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved. |
| Method | [AddSpeedPak](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak.md) | Obsolete. Superseded by [IConfigurationManager::AddSpeedPak2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2.md). |
| Method | [AddSpeedPak2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2.md) | Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration. |
| Method | [GetConfigurationParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.md) | Gets the parameters for this configuration. |
| Method | [GetConfigurationParamsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.md) | Gets the number of parameters for this configuration. |
| Method | [IGetConfigurationParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.md) | Gets the parameters for this configuration. |
| Method | [ISetConfigurationParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.md) | Sets the parameters for this configuration. |
| Method | [RemoveMarkForAllConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations.md) | Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved. |
| Method | [SetConfigurationParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.md) | Sets the parameters for this configuration. |
| Method | [SetExpanded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetExpanded.md) | Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager. |
| Method | [SortConfigurationTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SortConfigurationTree.md) | Specifies the order in which to list configurations in the ConfigurationManager. |

[Top](#top)

 

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)

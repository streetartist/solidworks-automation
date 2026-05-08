# IConfiguration Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members`

Allows you to manage different part or assembly states.
The following tables list the members exposed by [IConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AddRebuildSaveMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.md) | Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data saved every time you save the model document. |
| Property | [AlternateName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.md) | Gets or sets the configuration's alternate name (i.e., user-specified name). |
| Property | [BOMPartNoSource](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~BOMPartNoSource.md) | Gets or sets the source of the part number used in the BOM table. |
| Property | [ChildComponentDisplayInBOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM.md) | Gets or sets the child component display option of this configuration in the Bill of Materials (BOM) for an assembly or for a cutlist part (weldment and/or sheet metal). |
| Property | [Comment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Comment.md) | Gets or sets the configuration comment. |
| Property | [CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md) | Gets the custom property information for this configuration. |
| Property | [Description](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Description.md) | Gets or sets the description of the configuration. |
| Property | [DimXpertManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DimXpertManager.md) | Gets the DimXpert schema for this configuration. |
| Property | [HideNewComponentModels](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~HideNewComponentModels.md) | Gets or sets whether new components are hidden in this inactive configuration. |
| Property | [LargeDesignReviewMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~LargeDesignReviewMark.md) | Gets or sets whether to add display data to this configuration when the document is saved. |
| Property | [Lock](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Lock.md) | Gets or sets whether the configuration is locked. |
| Property | [Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.md) | Gets or sets the configuration name. |
| Property | [NeedsRebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.md) | Gets whether the configuration needs to be rebuilt. |
| Property | [RepresentationShared](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RepresentationShared.md) | Gets or sets whether this [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) Representation configuration is shared. |
| Property | [ShowChildComponentsInBOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ShowChildComponentsInBOM.md) | Obsolete. Superseded by [IConfiguration::ChildComponentDisplayInBOM.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM.md) |
| Property | [SuppressNewComponentModels](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewComponentModels.md) | Gets or sets whether new components are suppressed in this configuration. |
| Property | [SuppressNewFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewFeatures.md) | Gets or sets whether to suppress new features in this configuration. |
| Property | [Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Type.md) | Gets the type of configuration. |
| Property | [UseAlternateNameInBOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseAlternateNameInBOM.md) | Gets or sets whether the [alternate name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.md) (i.e., user-specified name) is displayed in the bill of materials for this configuration. |
| Property | [UseDescriptionInBOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseDescriptionInBOM.md) | Gets or sets whether the [description](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Description.md) of the configuration is displayed in the bill of materials. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.md) | Obsolete. Superseded by [IConfiguration::AddExplodeStep2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2.md). |
| Method | [AddExplodeStep2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2.md) | Adds a regular (translate and rotate) explode step to the explode view of the active configuration. |
| Method | [AddPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.md) | Adds an explode step to the specified explode view of a multibody part. |
| Method | [AddRadialExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.md) | Adds a radial explode step to the explode view of the active configuration. |
| Method | [ApplyDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.md) | Applies the specified display state to this configuration. |
| Method | [CopyDisplayStateFromConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.md) | Copies the specified display state from the specified configuration to this configuration. |
| Method | [CreateDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.md) | Creates a display state for this configuration. |
| Method | [DeleteDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.md) | Deletes the specified display state from this configuration. |
| Method | [DeleteExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md) | Deletes the specified explode step. |
| Method | [Get3DExperienceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.md) | Gets how this configuration is viewed in [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm). |
| Method | [GetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.md) | Gets all of the children configurations of this derived configuration. |
| Method | [GetChildrenCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.md) | Gets the number of children for this configuration. |
| Method | [GetComponentConfigName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetComponentConfigName.md) | Gets the referenced configuration name of the specified component in this configuration. |
| Method | [GetComponentSuppressionState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetComponentSuppressionState.md) | Gets the suppression state of the specified component in this configuration. |
| Method | [GetCurrentPartExplodeViewName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCurrentPartExplodeViewName.md) | Gets the explode view name in the current configuration. |
| Method | [GetCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCustomProperties.md) | Obsolete. Superseded by [IConfiguration::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md). |
| Method | [GetCustomPropertiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCustomPropertiesCount.md) | Obsolete. Superseded by [IConfiguration::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md). |
| Method | [GetCutListItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCutListItems.md) | Gets the cut list folders in this active or non-active configuration. |
| Method | [GetDisplayStateBodyProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.md) | Gets the bodies and their material properties in the specified display state. |
| Method | [GetDisplayStateComponentProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.md) | Gets the components and their material properties in the specified display state. |
| Method | [GetDisplayStateComponentVisibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.md) | Gets the components and their visibilities in the specified display state. |
| Method | [GetDisplayStateFaceProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.md) | Gets the faces and their material properties in the specified display state. |
| Method | [GetDisplayStateFeatureProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.md) | Gets the features and their material properties in the specified display state. |
| Method | [GetDisplayStateProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.md) | Gets the material properties of the specified display state. |
| Method | [GetDisplayStates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md) | Gets the names of the display states for this configuration. |
| Method | [GetDisplayStatesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.md) | Gets the number of display states for this configuration. |
| Method | [GetExpanded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExpanded.md) | Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager. |
| Method | [GetExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.md) | Gets the specified explode step in this configuration's explode step sequence. |
| Method | [GetID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetID.md) | Gets the configuration ID of this configuration. |
| Method | [GetNumberOfExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.md) | Gets the number of explode steps for this configuration. |
| Method | [GetNumberOfPartExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfPartExplodeSteps.md) | Gets the number of explode steps in the explode view of a multibody part. |
| Method | [GetParameterCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.md) | Gets the number of parameters for this configuration. |
| Method | [GetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.md) | Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | [GetParent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.md) | Gets the parent configuration of this derived configuration. |
| Method | [GetPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.md) | Gets the specified explode step of an explode view of a multibody part. |
| Method | [GetRepresentationParent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRepresentationParent.md) | Gets the Physical Product represented by this configuration. |
| Method | [GetRootComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent.md) | Obsolete. Superseded by [IConfiguration::GetRootComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md). |
| Method | [GetRootComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md) | Gets the root component for this assembly configuration. |
| Method | [GetScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetScene.md) | Gets the ISwScene object for this configuration. |
| Method | [GetStreamName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetStreamName.md) | Gets the name of the stream for the current configuration. |
| Method | [IAddExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.md) | Adds a new explode step to the configuration. |
| Method | [IGetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.md) | Gets all of the children configurations of this derived configuration. |
| Method | [IGetCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetCustomProperties.md) | Obsolete. Superseded by [IConfiguration::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md). |
| Method | [IGetDisplayStates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.md) | Gets the names of the display states for this configuration. |
| Method | [IGetExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.md) | Gets a pointer to the specified explode step in the configuration explode step sequence. |
| Method | [IGetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.md) | Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | [IGetRootComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent.md) | Obsolete. Superseded by [IConfiguration::IGetRootComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md). |
| Method | [IGetRootComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md) | Obsolete. Superseded by [IConfiguration::GetRootComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md). |
| Method | [IsDefeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDefeature.md) | Gets whether this configuration is a defeature configuration. |
| Method | [IsDerived](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDerived.md) | Gets whether this configuration is a derived configuration. |
| Method | [IsDirty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDirty.md) | Gets whether this configuration is dirty (i.e., needs to be updated). |
| Method | [ISetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.md) | Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | [IsLoaded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsLoaded.md) | Gets whether a configuration is loaded. |
| Method | [IsSpeedPak](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsSpeedPak.md) | Gets whether the configuration is a SpeedPak. |
| Method | [RenameDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.md) | Renames a display state of this configuration. |
| Method | [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Select.md) | Obsolete. Superseded by [IConfiguration::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Select2.md). |
| Method | [Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Select2.md) | Selects the configuration. |
| Method | [Set3DExperienceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Set3DExperienceType.md) | Converts this configuration in [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm). |
| Method | [SetColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetColor.md) | Sets the color for this configuration. |
| Method | [SetExpanded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetExpanded.md) | Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager. |
| Method | [SetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.md) | Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | [UpdateSpeedPak](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UpdateSpeedPak.md) | Updates the SpeedPak configuration for this configuration. |

[Top](#top)

 

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

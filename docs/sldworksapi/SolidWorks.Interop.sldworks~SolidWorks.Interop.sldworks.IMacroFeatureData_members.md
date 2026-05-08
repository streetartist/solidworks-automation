# IMacroFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members`

Allows access to the data that defines a macro feature.
The following tables list the members exposed by [IMacroFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CurrentConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~CurrentConfiguration.md) | Gets the macro feature configuration being rebuilt. |
| Property | [EditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.md) | Gets or sets the bodies to be modified by this macro feature. |
| Property | [EditBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBody.md) | Obsolete. Superseded by [IMacroFeatureData::IGetEditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.md), [IMacroFeatureData::ISetEditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetEditBodies.md), and [IMacroFeatureData::EditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.md). |
| Property | [EnableMultiBodyConsume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume.md) | Gets or sets whether to replace the original edit body with multiple solid bodies created during regeneration of a multibody macro feature. |
| Property | [FeatureTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~FeatureTransform.md) | Gets and sets the macro feature transform. |
| Property | [IconFiles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IconFiles.md) | Gets or sets the file names for the icons for this macro feature. |
| Property | [MacroFileEmbedded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileEmbedded.md) | Gets whether the macro file is embedded ini the model with the macro feature. |
| Property | [MacroFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileName.md) | Gets or sets the path and file name for the macro for the macro feature. |
| Property | [ModuleName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ModuleName.md) | Gets or sets the name of a module in the macro for this macro feature. |
| Property | [Parents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Parents.md) | Gets or sets the parent features for this macro feature. |
| Property | [PatternTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PatternTransform.md) | Gets the pattern transform. |
| Property | [ProcedureName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ProcedureName.md) | Gets or sets a name of the procedure in the macro for this macro feature. |
| Property | [PropertyManagerHandleMacroFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleMacroFileName.md) | Gets or sets the path and file name for the macro file from or to the PropertyManager handle for this macro feature. |
| Property | [PropertyManagerHandleModuleName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleModuleName.md) | Gets or sets the name of the module in the macro file from or to the PropertyManager handle. |
| Property | [PropertyManagerHandleProcedureName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleProcedureName.md) | Gets or sets the name of the procedure in the macro file from or to the PropertyManager handle. |
| Property | [Provider](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.md) | Gets or sets the error message to display in the What's Wrong dialog when a non-embedded macro feature fails to rebuild due to missing files. |
| Property | [SecurityHandleMacroFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleMacroFileName.md) | Gets or sets the name of the procedure in the macro file from or to the security handle. |
| Property | [SecurityHandleModuleName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleModuleName.md) | Gets and sets the name of the module in the macro file from or to the security handle. |
| Property | [SecurityHandleProcedureName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleProcedureName.md) | Gets or sets the name of the procedure in the macro file from or to the security handle. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~AccessSelections.md) | Gains access to the selections associated with this macro feature. |
| Method | [EmbedMacroFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EmbedMacroFile.md) | Sets whether to embed the macro file in the model with the macro feature. |
| Method | [GetBaseName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetBaseName.md) | Gets the name of the base feature for this macro feature. |
| Method | [GetDisplayDimensionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensionCount.md) | Gets the number of display dimensions for this macro feature. |
| Method | [GetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.md) | Gets the display dimensions for this macro feature. |
| Method | [GetDoubleByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.md) | Gets a double value by parameter name. |
| Method | [GetEdgeIdType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.md) | Gets the ID type of the specified edge for the macro feature. |
| Method | [GetEdgeUserId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.md) | Gets the user-defined IDs for the specified edge for the macro feature. |
| Method | [GetEditBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditBodiesCount.md) | Gets the number of bodies to be modified by this macro feature. |
| Method | [GetEditTargetTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditTargetTransform.md) | Gets the transform of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component. |
| Method | [GetEntitiesNeedUserId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.md) | Gets a list of faces and edges that need be assigned user IDs for the macro feature. |
| Method | [GetEntitiesNeedUserIdCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.md) | Gets the number of faces and edges that need to be assigned user IDs for the macro feature. |
| Method | [GetFaceIdType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.md) | Gets the ID type from the face for the macro feature. |
| Method | [GetFaceUserId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.md) | Gets the user-defined IDs for the specified face. |
| Method | [GetIconFileCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIconFileCount.md) | Gets the number of the files for the icons for this macro feature. |
| Method | [GetIntegerByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.md) | Gets an integer value by parameter name. |
| Method | [GetModuleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleCount.md) | Gets the number of modules for the macro feature. |
| Method | [GetModuleNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleNames.md) | Gets the names of the modules in the macro for the macro feature. |
| Method | [GetParameterCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.md) | Gets the number of user-defined parameters. |
| Method | [GetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.md) | Gets the user-defined parameters. |
| Method | [GetParentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParentsCount.md) | Gets the number of parent features for this macro feature. |
| Method | [GetProcedureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProcedureCount.md) | Gets the number of procedures in the specified module in the macro for this macro feature. |
| Method | [GetProcedureNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProcedureNames.md) | Gets the names of the procedures in the specified module for the macro for the macro feature. |
| Method | [GetProgId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProgId.md) | Gets the version-independent program ID that is valid for this COM feature. |
| Method | [GetPropertyManagerHandleModuleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleCount.md) | Gets the number of modules in the macro from the PropertyManager handle for the macro feature. |
| Method | [GetPropertyManagerHandleModuleNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleNames.md) | Gets the names of the modules in the macro from the PropertyManager handle for the macro feature. |
| Method | [GetPropertyManagerHandleProcedureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureCount.md) | Gets the number of procedures in the specified module in the macro from the PropertyManager handle for this macro feature. |
| Method | [GetPropertyManagerHandleProcedureNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureNames.md) | Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature. |
| Method | [GetSelectionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelectionCount.md) | Gets the number of selected objects for the macro feature. |
| Method | [GetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections.md) | Obsolete. Superseded by [IMacroFeatureData::GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md). |
| Method | [GetSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections2.md) | Obsolete. Superseded by [IMacroFeatureData::GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md). |
| Method | [GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md) | Gets the selected objects for the macro feature. |
| Method | [GetStringByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.md) | Gets a string value by the name of the parameter for the macro feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IAccessSelections.md) | Gains access to the selections associated with this macro feature. |
| Method | [IAddDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IAddDisplayDimensions.md) | Adds the specified display dimensions to this macro feature. |
| Method | [IGetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetDisplayDimensions.md) | Gets the display dimensions for this macro feature. |
| Method | [IGetEditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.md) | Gets the bodies to be modified by this macro feature. |
| Method | [IGetEntitiesNeedUserId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEntitiesNeedUserId.md) | Gets a list of faces and edges that need be assigned user IDs for the macro feature. |
| Method | [IGetIconFiles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetIconFiles.md) | Gets the file names for the icons for this macro feature. |
| Method | [IGetModuleNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetModuleNames.md) | Gets the names of the modules in the macro for the macro feature. |
| Method | [IGetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters.md) | Gets the user-defined parameters. |
| Method | [IGetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParents.md) | Gets the parent features of this macro feature. |
| Method | [IGetProcedureNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetProcedureNames.md) | Gets the names of the procedures in the specified module in the macro for the macro feature. |
| Method | [IGetPropertyManagerHandleModuleNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleModuleNames.md) | Gets the names of the modules in the macro from the PropertyManager handle for the macro feature. |
| Method | [IGetPropertyManagerHandleProcedureNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleProcedureNames.md) | Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature. |
| Method | [IGetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections.md) | Obsolete. Superseded by [IMacroFeatureData::IGetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md). |
| Method | [IGetSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections2.md) | Obsolete. Superseded by [IMacroFeatureData::IGetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md). |
| Method | [IGetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md) | Gets the selected objects for the macro feature. |
| Method | [IsCOMFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IsCOMFeature.md) | Gets whether the feature is a COM feature. |
| Method | [ISetEditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetEditBodies.md) | Sets the bodies to be modified by this macro feature. |
| Method | [ISetIconFiles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetIconFiles.md) | Sets the file names for the icons for this macro feature. |
| Method | [ISetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParameters.md) | Sets the user-defined parameters. |
| Method | [ISetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParents.md) | Sets the parent features for this macro feature. |
| Method | [ISetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections.md) | Obsolete. Superseded by [IMacroFeatureData::ISetSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.md). |
| Method | [ISetSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.md) | Sets the selected objects for the macro feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections associated with this macro feature. |
| Method | [SetDoubleByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetDoubleByName.md) | Sets a double value by parameter name for the macro feature. |
| Method | [SetEdgeUserId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.md) | Sets the user-defined IDs for the specified edge for the macro feature. |
| Method | [SetFaceUserId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.md) | Sets user-defined IDs for the face for the macro feature. |
| Method | [SetIntegerByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetIntegerByName.md) | Sets an integer value by parameter name. |
| Method | [SetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetParameters.md) | Sets the user-defined parameters. |
| Method | [SetProgId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetProgId.md) | Sets the version-independent program ID that is valid for this COM feature. |
| Method | [SetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections.md) | Obsolete. Superseded by [IMacroFeatureData::SetSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.md). |
| Method | [SetSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.md) | Sets the selected objects for the macro feature. |
| Method | [SetStringByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.md) | Sets a string value by parameter name. |

[Top](#top)

 

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::IInsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.md)  
[IFeatureManager::InsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md)

# IFeature Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members`

Allows access to the feature type, name, parameter data, and the next feature in the FeatureManager design tree.
The following tables list the members exposed by [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CreatedBy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CreatedBy.md) | Gets the name of the user who created the feature. |
| Property | [CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CustomPropertyManager.md) | Gets the custom property information for weldment and cut-list item features only. |
| Property | [DateCreated](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateCreated.md) | Gets the date on which the feature was created. |
| Property | [DateModified](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateModified.md) | Gets the date on which the feature was last modified. |
| Property | [Description](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Description.md) | Gets or sets the description for this feature. |
| Property | [ExcludeFromCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ExcludeFromCutList.md) | Gets or sets whether to exclude this feature from the cut list. |
| Property | [Is3DInterconnectFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectFeature.md) | Gets whether this is a 3D Interconnect feature. |
| Property | [Is3DInterconnectUpdateAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectUpdateAvailable.md) | Gets whether an update is available for this 3D Interconnect part or assembly. |
| Property | [Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md) | Gets or sets the name of the current feature. |
| Property | [Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.md) | Gets the visibility state of this feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.md) | Adds a comment to this feature. |
| Method | [AddPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddPropertyExtension.md) | Adds a property extension to this feature. |
| Method | [BreakLink](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~BreakLink.md) | Breaks the link to third-party native CAD parts and assemblies. |
| Method | [DeSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DeSelect.md) | Deselects this feature. |
| Method | [EnumDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~EnumDisplayDimensions.md) | This method returns a [display dimensions enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions.md) for this feature. |
| Method | [GetAffectedFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount.md) | Gets the number of faces modified by a feature, such as a draft feature. |
| Method | [GetAffectedFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaces.md) | Gets the faces modified by a feature, such as a draft feature. |
| Method | [GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBody.md) | Obsolete. Superseded by [IFeatures::GetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.md), [IFeatures::IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md), [IFace2::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBody.md), and [IFace2::IGetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBody.md). |
| Method | [GetBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.md) | Gets the bounding box for this feature. |
| Method | [GetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.md) | Gets the child features belonging to this feature. |
| Method | [GetCreatedVersion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetCreatedVersion.md) | Gets the SOLIDWORKS version number in which the selected feature was created. |
| Method | [GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) | Gets the feature data object for a feature, such as an advanced mate, extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature. |
| Method | [GetDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDisplayDimension.md) | Gets the display dimension object for the specified pattern property. |
| Method | [GetEditStatus](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetEditStatus.md) | Gets whether the feature can currently be edited. |
| Method | [GetErrorCode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode.md) | Obsolete. Superseded by [IFeature::GetErrorCode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.md). |
| Method | [GetErrorCode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.md) | Gets the error code for this feature. |
| Method | [GetFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaceCount.md) | Gets the number of faces in this feature. |
| Method | [GetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.md) | Gets the faces in this feature. |
| Method | [GetFirstDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension.md) | Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature. |
| Method | [GetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.md) | Gets the first sub-feature that belongs to this feature. |
| Method | [GetID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetID.md) | Gets the feature ID of this feature. |
| Method | [GetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFeatureParameters.md) | Gets the data object for this 3D Interconnect part or assembly. |
| Method | [GetImportedFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFileName.md) | Gets the file name from an imported feature. |
| Method | [GetMaterialIdName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialIdName.md) | Gets the material name. |
| Method | [GetMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues.md) | Obsolete. Superseded by [IFeature::GetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.md). |
| Method | [GetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.md) | Gets the material property values for this feature in the specified configurations. |
| Method | [GetMaterialUserName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialUserName.md) | Gets the material name for this feature, which is visible to the user. |
| Method | [GetModifiedVersion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetModifiedVersion.md) | Gets the SOLIDWORKS version number in which this feature was last modified. |
| Method | [GetNameForSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.md) | Gets the selected feature's type and name. |
| Method | [GetNextDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextDisplayDimension.md) | Gets the next display dimension associated with this feature. |
| Method | [GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md) | Gets the next feature in the part. |
| Method | [GetNextSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.md) | Gets the next sub-feature from the owner of this sub-feature. |
| Method | [GetOwnerFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.md) | Gets the feature that owns this feature. |
| Method | [GetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.md) | Gets the parent features for this feature. |
| Method | [GetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetPropertyExtension.md) | Gets the property extension on this feature. |
| Method | [GetSpecificFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature.md) | Obsolete. Superseded by [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md). |
| Method | [GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) | Gets the more specific interface to a selected feature. |
| Method | [GetTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.md) | Gets the texture applied to this feature in the specified configuration. |
| Method | [GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) | Gets the type of feature.  **NOTE:** To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call this method; otherwise, call [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md). |
| Method | [GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) | Gets the type of feature.  **NOTE:** To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md); otherwise, call this method. |
| Method | [GetUIState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUIState.md) | Gets the user-interface state of the current feature. |
| Method | [GetUpdateStamp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUpdateStamp.md) | Gets the current update stamp for this feature. |
| Method | [HasFrozenUpdatePending](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.md) | Gets whether this feature has pending freeze updates. |
| Method | [HasMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasMaterialPropertyValues.md) | Gets whether this feature has an appearance. |
| Method | [IGetAffectedFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetAffectedFaces.md) | Gets the faces modified by a feature, such as a draft feature. |
| Method | [IGetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBody.md) | Obsolete. Superseded by [IFeatures::GetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.md), [IFeatures::IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md), [IFace2::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBody.md), and [IFace2::IGetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBody.md). |
| Method | [IGetBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBody2.md) | Obsolete. Superseded by [IFeatures::GetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.md), [IFeatures::IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md), [IFace2::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBody.md), and [IFace2::IGetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBody.md). |
| Method | [IGetBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.md) | Gets the bounding box for this feature. |
| Method | [IGetChildCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.md) | Gets the number of child features that belong to this feature. |
| Method | [IGetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.md) | Gets the child features belonging to this feature. |
| Method | [IGetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.md) | Gets the feature data object for a feature, such as an extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature. |
| Method | [IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces.md) | Obsolete. Superseded by [IFeature::IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md). |
| Method | [IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md) | Gets the faces in this feature. |
| Method | [IGetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.md) | Gets the first sub-feature that belongs to this feature. |
| Method | [IGetMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues.md) | Obsolete. Superseded by [IFeature::IGetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.md). |
| Method | [IGetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.md) | Gets the material property values for this feature in the specified configurations. |
| Method | [IGetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.md) | Gets the next feature. |
| Method | [IGetNextSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.md) | Gets the next sub-feature from the owner of this sub-feature. |
| Method | [IGetParentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.md) | Gets the number of parent features for this feature. |
| Method | [IGetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.md) | Gets the parent features for this feature. |
| Method | [IGetSpecificFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetSpecificFeature.md) | Obsolete. Superseded by [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md). |
| Method | [IIsSuppressed2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IIsSuppressed2.md) | Gets whether the feature in the specified configurations is suppressed. |
| Method | [IListExternalFileReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences.md) | Obsolete. Superseded by [IFeature::IListExternalFileReferences2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.md). |
| Method | [IListExternalFileReferences2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.md) | Gets the names and statuses of the external references for this feature in a part or assembly. |
| Method | [IModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition.md) | Obsolete. Superseded by [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md). |
| Method | [IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) | Updates the definition of a feature with the new values in an associated feature data object obtained with [IFeature::IGetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.md). |
| Method | [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.md) | Gets a pointer to the object for the specified parameter or a pointer to the specified parameter. |
| Method | [IRemoveMaterialProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2.md) | Removes material property values from this feature. |
| Method | [IsBase](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsBase.md) | Obsolete. Superseded by [IFeature::IsBase2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsBase2.md). |
| Method | [IsBase2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsBase2.md) | Gets whether this feature is a base feature. |
| Method | [IsDimXpertAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsDimXpertAnnotation.md) | Gets whether this feature is a DimXpert annotation. |
| Method | [IsDimXpertFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsDimXpertFeature.md) | Gets whether this feature is a DimXpert feature. |
| Method | [ISetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody.md) | Obsolete. Superseded by [IFeature::ISetBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.md). |
| Method | [ISetBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody2.md) | Obsolete. Superseded by [IFeature::ISetBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.md). |
| Method | [ISetBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.md) | Replaces the body of the base feature. |
| Method | [ISetMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues.md) | Obsolete. Superseded by [IFeature::ISetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.md). |
| Method | [ISetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.md) | Sets the material property values for this feature in the specified configurations. |
| Method | [ISetSuppression2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetSuppression2.md) | Sets the suppression state of this feature. |
| Method | [IsFrozen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.md) | Gets whether this feature is frozen. |
| Method | [IsHiddenLock](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.md) | Gets whether this feature is the freeze bar. |
| Method | [IsRolledBack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsRolledBack.md) | Gets whether this feature is rolled back. |
| Method | [IsSuppressed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed.md) | Obsolete. Superseded by [IFeature::IsSuppressed2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed2.md). |
| Method | [IsSuppressed2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed2.md) | Gets whether the feature in the specified configurations is suppressed. |
| Method | [ListExternalFileReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences.md) | Obsolete. Superseded by [IFeature::ListExternalFileReferences2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.md). |
| Method | [ListExternalFileReferences2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.md) | Gets the names and statuses of the external references on the feature in a part or assembly. |
| Method | [ListExternalFileReferencesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferencesCount.md) | Gets the number of external references on the feature in a part or assembly. |
| Method | [MakeSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MakeSubFeature.md) | Makes a feature become a subfeature of this feature. |
| Method | [ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) | Updates the definition of a feature with the new values in an associated feature data object obtained with [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md). |
| Method | [MoveFreezeBarTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.md) | Obsolete. Superseded by [IFeature::MoveFreezeBarTo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo2.md). |
| Method | [MoveFreezeBarTo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo2.md) | Moves the freeze bar to the specified location in the FeatureManager design tree. |
| Method | [Parameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.md) | Gets a pointer to the object for the specified parameter or a pointer to the specified parameter. |
| Method | [RemoveMaterialProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty.md) | Obsolete. Superseded by [IFeature::RemoveMaterialProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.md). |
| Method | [RemoveMaterialProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.md) | Removes material property values from this feature. |
| Method | [RemoveTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.md) | Removes texture from this feature in either all of the configurations or only the specified configuration. |
| Method | [RemoveTextureByDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.md) | Removes texture from this feature in the specified display state. |
| Method | [ResetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ResetPropertyExtension.md) | Deletes the property extension for this feature. |
| Method | [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select.md) | Obsolete. Superseded by [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md). |
| Method | [Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) | Selects and marks this feature. |
| Method | [SelectByMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SelectByMark.md) | Obsolete. Superseded by [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md). |
| Method | [SetBodiesToKeep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBodiesToKeep.md) | Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies. |
| Method | [SetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody.md) | Obsolete. Superseded by [IFeature::SetBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody2.md). |
| Method | [SetBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody2.md) | Replaces an imported base feature body. |
| Method | [SetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.md) | Sets the data object for this 3D Interconnect part or assembly. |
| Method | [SetImportedFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFileName.md) | Sets the file name of an imported feature. |
| Method | [SetMaterialIdName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialIdName.md) | Sets the material name for this feature. |
| Method | [SetMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues.md) | Obsolete. Superseded by [IFeature::SetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.md). |
| Method | [SetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.md) | Sets the material property values for this feature in the specified configurations. |
| Method | [SetMaterialUserName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialUserName.md) | Sets the material user name for this feature, which is visible to the user. |
| Method | [SetSuppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression.md) | Obsolete. Superseded by [IFeature::SetSuppression2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression2.md). |
| Method | [SetSuppression2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression2.md) | Sets the suppression state of this feature. |
| Method | [SetTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.md) | Applies texture to this feature in either all configurations or only the specified configuration. |
| Method | [SetTextureByDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.md) | Applies texture to this feature in the specified display state. |
| Method | [SetUIState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetUIState.md) | Sets the user-interface state of the current feature. |
| Method | [Update3DInterconnectModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Update3DInterconnectModel.md) | Updates the model for this 3D Interconnect part or assembly. |
| Method | [UpdateExternalFileReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~UpdateExternalFileReferences.md) | Updates the external file references on this model. |

[Top](#top)

 

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

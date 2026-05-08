# IModelViewManager Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members`

Allows access to the model view.
The following tables list the members exposed by [IModelViewManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [ActiveFeatureManagerTabIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActiveFeatureManagerTabIndex.md) | Gets or sets the index of the active tab in the Manager Pane. |
| Property | [Document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~Document.md) | Gets the document to which this model view belongs. |
| Property | [FeatureManagerTabsVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible.md) | Gets or sets whether all of the tabs in the Manager Pane are visible. |
| Property | [LinkedViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~LinkedViews.md) | Gets or sets whether linking of viewports is enabled in this document. |
| Property | [ViewportDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.md) | Sets the model's viewport arrangement. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [ActivateControlTab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateControlTab.md) | Selects a control tab on the model view to be the active tab. |
| Method | [ActivateModelTab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateModelTab.md) | Selects a control tab on the model view. |
| Method | [AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.md) | Adds a tab to this model view using the specified ActiveX control. |
| Method | [AddControl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl2.md) | Obsolete. Superseded by [IModelViewManager::AddControl3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.md). |
| Method | [AddControl3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.md) | Adds a tab to this model view that supports tab traversal using the specified ActiveX control. |
| Method | [AddSnapShot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot.md) | Creates a snapshot with the specified name of an assembly. |
| Method | [CreateFeatureMgrControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl.md) | Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrControl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.md). |
| Method | [CreateFeatureMgrControl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.md) | Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrControl3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.md). |
| Method | [CreateFeatureMgrControl3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.md) | Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrControl4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl4.md). |
| Method | [CreateFeatureMgrControl4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl4.md) | Creates a new FeatureManager design tree view containing the specified ActiveX control with a tab that displays the specified scaleable icon. |
| Method | [CreateFeatureMgrView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView.md) | Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md). |
| Method | [CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md) | Creates a new view (tab) in this FeatureManager design tree. |
| Method | [CreateFeatureMgrWindowFromHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandle.md) | Creates a new view in the FeatureManager design tree using the specified .NET tab control. |
| Method | [CreateFeatureMgrWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandlex64.md) | On 64-bit machines, creates a new view in the FeatureManager design tree using the specified .NET tab control. |
| Method | [CreateManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateManipulator.md) | Creates a manipulator, which is similar to the triad in the SOLIDWORKS user interface. |
| Method | [CreateSectionView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md) | Creates a section view in parts and assemblies. |
| Method | [CreateSectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.md) | Creates an empty [ISectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md) object whose properties you set before [creating a section view in a part or an assembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md). |
| Method | [DeleteControlTab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.md) | Deletes the specified control tab. |
| Method | [DeleteSnapShot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot.md) | Deletes the specified snapshot from an assembly. |
| Method | [DisplayWindowFromHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandle.md) | Displays a .NET control in this model view. |
| Method | [DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandlex64.md) | Displays a .NET control in this model view on 64-bit machines. |
| Method | [GetConfigurationManagerTabIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetConfigurationManagerTabIndex.md) | Gets the index of the ConfigurationManager tab in the Manager Pane. |
| Method | [GetControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetControl.md) | Gets the control associated with this model view. |
| Method | [GetDimXpertManagerTabIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDimXpertManagerTabIndex.md) | Gets the index of the DimXpertManager tab in the Manager Pane. |
| Method | [GetDisplayManagerTabIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDisplayManagerTabIndex.md) | Gets the index of the DisplayManager tab in the Manager Pane. |
| Method | [GetFeatureManagerTabs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTabs.md) | Gets the tabs from right to left in the Manager Pane. |
| Method | [GetFeatureManagerTreeTabIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTreeTabIndex.md) | Gets the index of the FeatureManager design tree tab in the Manager Pane. |
| Method | [GetFeatureMgrViewHWnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd.md) | Gets the window handle for the specified FeatureManager design tree view. |
| Method | [GetFeatureMgrViewHWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.md) | Gets the window handle for the specified FeatureManager design tree view in 64-bit applications. |
| Method | [GetPropertyManagerTabIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetPropertyManagerTabIndex.md) | Gets the index of the PropertyManager tab in the Manager Pane. |
| Method | [GetSectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData.md) | Gets access to the data of the specified section view. |
| Method | [GetSnapShot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.md) | Gets the specified snapshot of an assembly. |
| Method | [GetSnapShots](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots.md) | Gets the snapshots of an assembly. |
| Method | [IGetControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IGetControl.md) | Gets the control associated with this model view. |
| Method | [IsControlTabActive](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsControlTabActive.md) | Gets whether the specified control is active. |
| Method | [IsModelTabActive](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsModelTabActive.md) | Gets whether the control on this model view is active. |
| Method | [RemoveSectionView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView.md) | Removes a section view from a part and assembly. |

[Top](#top)

 

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)  
[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)

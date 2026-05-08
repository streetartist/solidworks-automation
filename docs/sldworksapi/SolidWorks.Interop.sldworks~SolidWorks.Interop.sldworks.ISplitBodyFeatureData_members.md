# ISplitBodyFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members`

Allows access to a Split feature.
The following tables list the members exposed by [ISplitBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Consume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~Consume.md) | Gets or sets whether the bodies in this Split feature are consumed. |
| Property | [OverrideDefaultTemplateSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~OverrideDefaultTemplateSettings.md) | Gets or sets whether to use an alternate template to apply to all new part or assembly files created during the split operation. |
| Property | [TemplatePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TemplatePath.md) | Gets or sets the template to use to make this Split feature. |
| Property | [TrimTools](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TrimTools.md) | Gets the trimming surfaces used as trim tools in this Split feature.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~AccessSelections.md) | Gains access to a Split feature. |
| Method | [GetSplitBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md) | Gets the split bodies in this Split feature. |
| Method | [GetSplitBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.md) | Gets the number of split bodies in this Split feature. |
| Method | [GetTrimToolsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetTrimToolsCount.md) | Gets the number of trimming surfaces used as trim tools in this Split feature. |
| Method | [IGetSplitBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.md) | Gets the split bodies for this Split feature. |
| Method | [IGetTrimTools](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetTrimTools.md) | Gets the trimming surfaces used as trim tools in this Split feature. |
| Method | [ISetSplitBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetSplitBodies.md) | Obsolete. Superseded by [ISplitBodyFeatureData::SetSplitBodies2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md) |
| Method | [ISetTrimTools](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetTrimTools.md) | Gets the trimming surfaces used as trim tools in this Split feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that define this Split feature. |
| Method | [SetSplitBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies.md) | Obsolete. Superseded by [ISplitBodyFeatureData::SetSplitBodies2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md) |
| Method | [SetSplitBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md) | Edits the current split bodies in this Split feature. |

[Top](#top)

 

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.md)

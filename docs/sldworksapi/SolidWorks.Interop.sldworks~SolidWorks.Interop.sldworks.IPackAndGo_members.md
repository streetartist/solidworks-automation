# IPackAndGo Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members`

Allows access to Pack and Go.
The following tables list the members exposed by [IPackAndGo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AddPrefix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddPrefix.md) | Gets or sets a prefix for all filenames for Pack and Go. |
| Property | [AddSuffix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddSuffix.md) | Gets or sets a suffix for all filenames for Pack and Go. |
| Property | [FlattenToSingleFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.md) | Gets or sets whether to save all files to the root directory of the Pack and Go destination folder. |
| Property | [FolderStructureOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FolderStructureOption.md) | Gets or sets the folder structure to save to with Pack and Go. |
| Property | [IncludeDrawings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeDrawings.md) | Gets or sets whether to add the model's drawing documents to Pack and Go. |
| Property | [IncludeSimulationResults](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeSimulationResults.md) | Gets or sets whether to add the model's SOLIDWORKS Simulation results to Pack and Go. |
| Property | [IncludeSuppressed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeSuppressed.md) | Gets or sets whether to included suppressed components in Pack and Go. |
| Property | [IncludeToolboxComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeToolboxComponents.md) | Gets or sets whether to include SOLIDWORKS Toolbox components in Pack and Go. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddExternalDocuments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddExternalDocuments.md) | Adds non-SOLIDWORKS files to Pack and Go. |
| Method | [GetDocumentNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.md) | Gets the original paths and filenames of all of the model's documents for Pack and Go. |
| Method | [GetDocumentNamesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.md) | Gets the number of documents comprising the model for Pack and Go. |
| Method | [GetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames.md) | Gets the paths and filenames to which to save the model's documents for Pack and Go set by [IPackAndGo::SetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md). |
| Method | [GetExternalDocuments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetExternalDocuments.md) | Gets the paths and filenames of the non-SOLIDWORKS files added to Pack And Go. |
| Method | [GetSaveToName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetSaveToName.md) | Gets the path or the path and filename of the Zip file for Pack and Go set by [IPackAndGo::SetSaveToName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.md). |
| Method | [IGetDocumentNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.md) | Gets the original paths and filenames of all of the model's documents for Pack and Go. |
| Method | [IGetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.md) | Gets the paths and filenames to which to save the model's documents for Pack and Go set by [IPackAndGo::ISetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md). |
| Method | [ISetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md) | Sets the paths and filenames of the documents to save in Pack and Go. |
| Method | [RemoveExternalDocuments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~RemoveExternalDocuments.md) | Removes the specified non-SOLIDWORKS files from Pack and Go. |
| Method | [SetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md) | Sets the paths and filenames of the documents for Pack and Go. |
| Method | [SetSaveToName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.md) | Obsolete. Superseded by [IPackAndGo::SetSaveToName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2.md). |
| Method | [SetSaveToName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2.md) | Overrides the paths and filenames of the documents set by [IPackAndGo::SetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md) or [IPackAndGo::ISetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md) with the specified path or the path and name of the Zip file. |

[Top](#top)

 

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

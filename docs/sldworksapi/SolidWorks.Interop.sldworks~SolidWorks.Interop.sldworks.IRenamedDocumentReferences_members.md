# IRenamedDocumentReferences Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members`

Allows you to update references to a renamed file in unopened documents.
The following tables list the members exposed by [IRenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CompletionAction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~CompletionAction.md) | Gets or sets whether to update references to the renamed file in unopened documents. |
| Property | [IncludeFileLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.md) | Gets or sets whether to search the folders listed under **Referenced Documents** in **Tools > Options > System Options > File Locations**. |
| Property | [UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.md) | Gets or sets whether to update the references to the new file name. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddSearchFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.md) | Adds the specified folder in which to search for documents whose references to update. |
| Method | [GetSearchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.md) | Gets the folders to search. |
| Method | [ReferencesArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray.md) | Gets the pathnames of the documents with references to this renamed document. |
| Method | [RemoveReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveReference.md) | Removes the specified reference from the [list of references](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray.md) to update. |
| Method | [RemoveSearchFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.md) | Removes the specified folder in which to search for documents whose references to update. |
| Method | [Search](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~Search.md) | Searches for documents whose references to update. |

[Top](#top)

 

See Also

#### Reference

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::HasRenamedDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.md)  
[IModelDocExtension::RenameDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.md)

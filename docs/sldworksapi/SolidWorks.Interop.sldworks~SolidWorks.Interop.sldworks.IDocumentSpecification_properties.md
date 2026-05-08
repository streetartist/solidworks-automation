# IDocumentSpecification Interface Properties

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_properties`

Allows you to specify how to open a model document. Use this interface's properties before calling ISldWorks::OpenDoc7 to specify how you want to open a model document.
For a list of all members of this type, see [IDocumentSpecification members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AddToRecentDocumentList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AddToRecentDocumentList.md) | Gets or sets whether to add the opened document to the Recent Documents list. |
| Property | [AutoRepair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair.md) | Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened. |
| Property | [ComponentList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ComponentList.md) | Gets or sets the selected components to load when opening an assembly document. |
| Property | [ConfigurationName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ConfigurationName.md) | Gets or sets the name of the configuration to load when opening a model document. |
| Property | [CriticalDataRepair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~CriticalDataRepair.md) | Gets or sets whether to automatically repair critical data errors in the file to be opened. |
| Property | [DetailingMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DetailingMode.md) | Gets or sets whether this drawing document is in detailing mode. |
| Property | [DisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DisplayState.md) | Gets or sets the name of the display state to use when opening a model document. |
| Property | [DocumentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DocumentType.md) | Gets or sets the type of model document to open. |
| Property | [Error](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Error.md) | Gets or sets the file load errors when opening a model document. |
| Property | [FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~FileName.md) | Gets or sets the path and filename of the model document to open. |
| Property | [IgnoreHiddenComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~IgnoreHiddenComponents.md) | Gets or sets whether to load hidden components when opening an assembly or drawing document. |
| Property | [InteractiveAdvancedOpen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveAdvancedOpen.md) | Gets whether to display an intermediate dialog, which allows the interactive user to set options before opening a document. |
| Property | [InteractiveComponentSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection.md) | Gets whether to display the Selective Open dialog, which allows the interactive user to either select and open specific components or open all of the displayed components. |
| Property | [LightWeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LightWeight.md) | Gets or sets whether to open an assembly or drawing document with lightweight parts. |
| Property | [LoadExternalReferencesInMemory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadExternalReferencesInMemory.md) | Gets or sets whether to load external references in memory when opening a document. |
| Property | [LoadModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadModel.md) | Gets or sets whether to load the model if the document is a detached drawing. |
| Property | [PLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~PLMObjectSpecification.md) | Gets the specification of this SOLIDWORKS Connected document. |
| Property | [Query](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Query.md) | Gets or sets whether the options passed during a document's open, load, and save can be retrieved by this API. |
| Property | [ReadOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ReadOnly.md) | Gets or sets whether the model document is opened read-only or read-write. |
| Property | [Selective](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective.md) | Gets or sets whether to open a document in Quick view (parts and drawings) or Quick view / Selective (assemblies) mode. |
| Property | [SheetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~SheetName.md) | Gets or sets the name of the sheet in a drawing document to open. |
| Property | [Silent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.md) | Gets or sets whether to open the model document silently. |
| Property | [UseLightWeightDefault](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~UseLightWeightDefault.md) | Gets or sets whether to use the system default lightweight setting. |
| Property | [UseSpeedPak](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~UseSpeedPak.md) | Gets or sets whether to open an assembly document using the SpeedPak option. |
| Property | [ViewOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.md) | Gets or sets whether to open the assembly document in Large Design Review mode. |
| Property | [Warning](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Warning.md) | Gets or sets any file load warnings when opening a model document. |

[Top](#top)

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISldWorks::OpenDoc6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)

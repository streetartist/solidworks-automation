# OpenDoc7 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7`

Opens an existing document and returns a pointer to the document object.
Opens an existing document and returns a pointer to the document object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function OpenDoc7( _
   ByVal Specification As System.Object _
) As ModelDoc2
```

```

Dim instance As ISldWorks
Dim Specification As System.Object
Dim value As ModelDoc2
 
value = instance.OpenDoc7(Specification)
```

```

ModelDoc2 OpenDoc7( 
   System.object Specification
)
```

```

ModelDoc2^ OpenDoc7( 
   System.Object^ Specification
) 
```

#### Parameters

*Specification*
:   [Document specification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)

#### Return Value

[Document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Remarks

As of SOLIDWORKS 2020 SP03.1, SOLIDWORKS can run on the **3D**EXPERIENCE platform as [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm). While running SOLIDWORKS Connected, this method can be called to either import local SOLIDWORKS Desktop documents or open **3D**EXPERIENCE documents. Inspect the Remarks section on each property of IDocumentSpecification to see whether it can be used to open a **3D**EXPERIENCE platform document. Also see [IDocumentSpecifiation::PLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~PLMObjectSpecification.md).

The following remarks apply primarily to SOLIDWORKS Desktop.

When opening a parent document (assembly, drawing, and so on):

- SOLIDWORKS also opens any additional documents that are referenced in the parent document (parts, subassemblies, and so on).
- SOLIDWORKS follows certain rules in trying to locate its referenced documents. If explicit Search Folders have not been set using Tools, Options, System Options, ExternalReferences, then the first place SOLIDWORKS looks for the referenced documents is in the current working directory. If SOLIDWORKS finds the referenced file in the current working directory, then it is loaded from that directory.

Calling ISldWorks::OpenDoc7 does not change the current working directory to that of the opened file, whereas, interactively using the File Open dialog box does. This may affect documents with references.

Because the user may have interactively opened files from some random directory, you cannot be certain that the current working directory is pointing to the desired location. This may affect the referenced documents that ultimately get loaded when using ISldWorks::OpenDoc7 versus performing File Open interactively. You may want to set the current working directory before calling ISldWorks::OpenDoc7. This can be done using the [ISldWorks::SetCurrentWorkingDirectory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.md) method. To mimic the behavior of the File Open dialog, you set the current working directory to that of the file being opened.

When opening files that contain references, you may also want to consider the current Search Folder settings because they may affect the references that ultimately get loaded. This can be done using [ISldWorks::GetSearchFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.md) and [ISldWorks::SetSearchFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders.md). If Search Folders are currently in use, SOLIDWORKS looks for references in the Search Folders before trying to locate references in the current working directory.

ISldWorks::OpenDoc7 does not activate and display the document if the file is already open in memory in an assembly or drawing. However, ISldWorks::OpenDoc7 should return a valid [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) pointer that is usable with functions that do not require a document to be displayed. If you want, [ISldWorks::ActivateDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc2.md) or [ISldWorks::IActivateDoc3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc3.md) will activate and display the document. Because calling ISldWorks::OpenDoc7 does not activate nor display the file, calling the [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) or [ISldWorks::IActiveDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md) property will not return a pointer to this document.

This method fires the SOLIDWORKS event [FileOpenNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.md) event. Also, the SOLIDWORKS event [ActiveDocChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.md) and [ActiveModelDocChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler.md) events are sent if the file being loaded is not already open as the active document.

TIPS

|  |  |
| --- | --- |
| **To...** | **Then...** |
| Open an assembly in Large Design Review mode | Set [IDocumentSpecification::ViewOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.md) to true. This option displays large assemblies without actually loading them. This is useful for conducting a quick walk-through of a large assembly. Call [IAssemblyDoc::SelectiveOpen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.md) to open selected components after an assembly has been opened in Large Design Review mode. |
| Avoid warnings when opening the document | Set [IDocumentSpecification::Silent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.md) to true. The software uses the last-displayed configuration if it discovers missing configurations or component references. |
| Open a library feature part | Set [IDocumentSpecification::DocumentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DocumentType.md) to [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html).swDocPART. |
| Open foreign files (IGES, STEP, and so on) | Use [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md). |
| Avoid a warning when opening shaded models in views | Set [IDocumentSpecification::LoadModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadModel.md) to true. This option loads the model so that the view comes in shaded automatically. |
| Avoid large increases in memory usage caused when adding parts to assemblies | Opening a model causes SceneGraph to display the model. SceneGraph uses maps with defaults sizes of 2MB - 3MB for even the simplest model. And, assemblies and parts do not share the same SceneGraph buffer. To avoid large increases in your memory usage:   1. Set the document to invisible. 2. Open the parts. 3. Set the document to visible. 4. Add the part to the assembly.   See [ISldWorks::DocumentVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DocumentVisible.md) for details. |
| To open a document without a specified display state | Use [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md). |

A warning is displayed if you [open a Detached drawing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsRapidDraft.md) without loading the model, and the model was saved since the drawing was last saved.

This method honors:

- [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) swLargeAsmModeEnabled

    - and -

- [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) swLargeAsmModeEnabled, true/false (NOTE: if this toggle is set to true, then the document opens in lightweight mode)

Example

[Hide All Edges in Drawing (VBA)](Hide_All_Edges_in_Drawing_View_Example_VB.htm)  
[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)  
[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)  
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)  
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)  
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)  
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)  
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::CopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.md)  
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.md)  
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.md)  
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.md)  
[ISldWorks::GetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.md)  
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.md)  
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.md)  
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md)  
[ISldWorks::GetRecentFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRecentFiles.md)  
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.md)  
[ISldWorks::IGetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.md)  
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.md)  
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.md)  
[ISldWorks::IMoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IMoveDocument.md)  
[ISldWorks::PreviewDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDoc.md)  
[ISldWorks::PreviewDocx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDocx64.md)  
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.md)  
[ISldWorks::SetPromptFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename.md)  
[ISldWorks::IsBackgroundProcessingCompleted Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.md)  
[ISldWorks::EnableBackgroundProcessing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.md)

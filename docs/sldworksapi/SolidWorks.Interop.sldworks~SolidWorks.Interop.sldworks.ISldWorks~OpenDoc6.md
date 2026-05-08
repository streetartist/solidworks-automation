# OpenDoc6 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6`

Opens an existing document and returns a pointer to the document object.
Opens an existing document and returns a pointer to the document object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function OpenDoc6( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal Configuration As System.String, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As ModelDoc2
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim Options As System.Integer
Dim Configuration As System.String
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As ModelDoc2
 
value = instance.OpenDoc6(FileName, Type, Options, Configuration, Errors, Warnings)
```

```

ModelDoc2 OpenDoc6( 
   System.string FileName,
   System.int Type,
   System.int Options,
   System.string Configuration,
   out System.int Errors,
   out System.int Warnings
)
```

```

ModelDoc2^ OpenDoc6( 
   System.String^ FileName,
   System.int Type,
   System.int Options,
   System.String^ Configuration,
   [Out] System.int Errors,
   [Out] System.int Warnings
) 
```

#### Parameters

*FileName*
:   Document name or full path if not in current directory, including extension

*Type*
:   Document type as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*Options*
:   Mode in which to open the document as defined in [swOpenDocOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOpenDocOptions_e.html)

*Configuration*
:   Model configuration in which to open this document

    - Applies to parts and assemblies, not drawings
    - If this argument is empty or the specified configuration is not present in the model, the model is opened in the last-used configuration

*Errors*
:   Load errors as defined in [swFileLoadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html) (**See Remarks**)

*Warnings*
:   Warnings or extra information generated during the open operation as defined in [swFileLoadWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html)

#### Return Value

Newly loaded [model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) or NULL if document failed to open

Remarks

As of SOLIDWORKS 2020 SP03.1, SOLIDWORKS works on the **3D**EXPERIENCE platform as [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm). Use [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md) to open documents with SOLIDWORKS Connected.

As of SOLIDWORKS 2012 SP5, loading future file versions is supported, and ISldWorks::OpenDoc6 no longer throws a [swFileLoadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).swFutureVersion error. Use [IModelDocExtension::IsFutureVersion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsFutureVersion.md) to determine whether a component is for a future version of SOLIDWORKS.

As of SOLIDWORKS 2008, [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md) performs the same work as this method, but also:

- Allows you to open a document with a specified display state.
- Uses [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md) to specify input parameters.

This method also allows control over whether to:

- Suppress displaying dialog boxes
- Open the document read-only
- Open the document in Large Design Review mode
- Convert a drawing to a detached drawing

When opening a parent document (assembly, drawing, and so on):

- SOLIDWORKS also opens any additional documents that are referenced in the parent document (parts, subassemblies, and so on).
- SOLIDWORKS follows certain rules in trying to locate its referenced documents. If explicit Search Folders have not been set using Tools, Options, System Options, ExternalReferences, then the first place SOLIDWORKS looks for the referenced documents is in the current working directory. If SOLIDWORKS finds the referenced file in the current working directory, then it is loaded from that directory.

Calling ISldWorks::OpenDoc6 does not change the current working directory to that of the opened file, whereas, interactively using the File Open dialog box does. This may affect documents with references.

Because the user may have interactively opened files from some random directory, you cannot be certain that the current working directory is pointing to the desired location. This may affect the referenced documents that ultimately get loaded when using ISldWorks::OpenDoc6 versus performing File Open interactively. You may want to set the current working directory before calling ISldWorks::OpenDoc6. This can be done using the [ISldWorks::SetCurrentWorkingDirectory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.md) method. To mimic the behavior of the File Open dialog, you set the current working directory to that of the file being opened.

When opening files that contain references, you may also want to consider the current Search Folder settings because they may affect the references that ultimately get loaded. This can be done using [ISldWorks::GetSearchFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.md) and [ISldWorks::SetSearchFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders.md). If Search Folders are currently in use, SOLIDWORKS looks for references in the Search Folders before trying to locate references in the current working directory.

If this method successfully opens an assembly, it still returns swFileLoadError\_e.swFileNotFoundError in Errors if a referenced component file cannot be located.

ISldWorks::OpenDoc6 does not activate and display the document if the file is already open in memory in an assembly or drawing. However, ISldWorks::OpenDoc6 should return a valid [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) pointer that is usable with functions that do not require a document to be displayed. If you want, [ISldWorks::ActivateDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc2.md) or [ISldWorks::IActivateDoc3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc3.md) will activate and display the document. Because calling ISldWorks::OpenDoc6 does not activate nor display the file, calling the [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) or [ISldWorks::IActiveDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md) property will not return a pointer to this document.

This method fires the the SOLIDWORKS event [FileOpenNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.md) event. Also, the SOLIDWORKS event [ActiveDocChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.md) and [ActiveModelDocChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler.md) events are sent if the file being loaded is not already open as the active document.

TIPS

|  |  |
| --- | --- |
| **To...** | **Then...** |
| Open an assembly in Large Design Review mode | Set the Options argument to swOpenDocOptions\_LDR\_EditAssembly. This option opens large assemblies in edit mode without actually loading them. This is useful for conducting a quick walk-through of a large assembly. Call [IAssemblyDoc::SelectiveOpen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.md) to open selected components after an assembly has been opened in Large Design Review mode. |
| Avoid warnings when opening the document | Set the Options argument to swOpenDocOptions\_Silent. The software uses the last-displayed configuration if it discovers missing configurations or component references. |
| Open a library feature part | Set the Type argument to swDocPART. |
| Open foreign files (IGES, STEP, and so on) | Use [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md). |
| Avoid a warning when opening shaded models in views | Set the Options argument to swOpenDocOptions\_LoadModel. This option loads the model so that the view comes in shaded automatically. |
| Avoid large increases in memory usage caused when adding parts to assemblies | Opening a model causes SceneGraph to display the model. SceneGraph uses maps with defaults sizes of 2MB - 3MB for even the simplest model. And, assemblies and parts do not share the same SceneGraph buffer. To avoid large increases in your memory usage:   1. Set the document to invisible. 2. Open the parts. 3. Set the document to visible. 4. Add the part to the assembly.   See [ISldWorks::DocumentVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DocumentVisible.md) for details. |
| Open a document with a specified display state | Use ISldWorks::OpenDoc7. |

A warning is displayed if you [open a Detached drawing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsRapidDraft.md) without loading the model, and the model was saved since the drawing was last saved.

This method honors:

- [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) swLargeAsmModeEnabled

    - and -

- [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) swLargeAsmModeEnabled, true/false (NOTE: if this toggle is set to true, then the file opens in lightweight mode)

Example

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)  
[Open Document (VBA)](Open_Document_Example_VB.htm)  
[Open Document Silently (VBA)](Open_Document_Silently_Example_VB.htm)  
[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)  
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)  
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)  
[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)  
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)  
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

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
[ISldWorks::GetOpenedFileInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenedFileInfo.md)  
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.md)  
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
[ISldWorks::EnableBackgroundProcessing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.md)  
[ISldWorks::IsBackgroundProcessingCompleted Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.md)

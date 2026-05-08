# SaveAs3 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3`

Saves the active document to the specified name with advanced options.
Saves the active document to the specified name with advanced options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAs3( _
   ByVal Name As System.String, _
   ByVal Version As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal ExportData As System.Object, _
   ByVal AdvancedSaveAsOptions As System.Object, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Name As System.String
Dim Version As System.Integer
Dim Options As System.Integer
Dim ExportData As System.Object
Dim AdvancedSaveAsOptions As System.Object
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean
 
value = instance.SaveAs3(Name, Version, Options, ExportData, AdvancedSaveAsOptions, Errors, Warnings)
```

```

System.bool SaveAs3( 
   System.string Name,
   System.int Version,
   System.int Options,
   System.object ExportData,
   System.object AdvancedSaveAsOptions,
   out System.int Errors,
   out System.int Warnings
)
```

```

System.bool SaveAs3( 
   System.String^ Name,
   System.int Version,
   System.int Options,
   System.Object^ ExportData,
   System.Object^ AdvancedSaveAsOptions,
   [Out] System.int Errors,
   [Out] System.int Warnings
) 
```

#### Parameters

*Name*
:   Full pathname of the document to save; the file extension indicates any conversion that should be performed (for example, **Part1.igs** to save in IGES format) (see **Remarks**)

*Version*
:   Format in which to save this document as defined in [swSaveAsVersion\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsVersion_e.html) (see **Remarks**)

*Options*
:   Option indicating how to save the document as defined in [swSaveAsOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html) (see **Remarks**)

*ExportData*
:   [IExportPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.md) object for exporting drawing sheets to PDF (see **Remarks**)

*AdvancedSaveAsOptions*
:   [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) (see **Remarks**)

*Errors*
:   Errors that caused the save to fail as defined in [swFileSaveError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html) (see **Remarks**)

*Warnings*
:   Warnings or extra information generated during the save operation as defined in [swFileSaveWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html) (see **Remarks**)

#### Return Value

True if the save is successful, false if not

Remarks

The difference between this method and the now obsolete [IModelDocExtension::SaveAs2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs2.md) is that this method uses an IAdvancedSaveAsOptions object to specify advanced options. For example:

- Saving a subset of configurations
- Renaming and/or relocating individual component references
- Specifying the prefix and/or suffix for all component reference names

To specify the AdvancedSaveAsOptions parameter of this method, call [IModelDocExtension::GetAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.md) to create an IAdvancedSaveAsOptions object.

To save as an IGES, STL, or STEP file, the document to convert must be the active document. Before calling this method:

1. Call [ISldWorks::ActivateDoc3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc3.md) to make the document to convert the active document.
2. Call [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) to get the active document.

This method:

- Exports the entire model, unless faces or bodies are selected, in which case, it exports only those. Call [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md) before calling this method to clear the selection list and export the entire model.
- Overwrites existing files unless they are read only.
- Results in the FileSaveNotify event being sent to any application listening.
- Removes any configuration-specific bitmap previews, except the current configuration's.

Use Name to specify the full pathname of the saved document. If you specify only the file name, then it is saved in the active document's directory. The filename extension indicates the conversion that should be performed (for example, **Part1.igs** to save to IGES). If the filename extension does not uniquely indicate how the file should be formatted, use Version to specify how to save the file. For example, to save:

- A standard drawing document as a detached drawing, specify swSaveAsDetachedDrawing for Version.
- A detached drawing as a standard drawing, specify swSaveAsStandardDrawing for Version.
- A standard or detached drawing document in the same format, specify swSaveAsCurrentVersion for Version.

Use ExportData to specify which drawings sheets to save to PDF. If ExportData is Nothing or null, then all sheets are saved to PDF. Saving a document as PDF when the document is open as view-only is not supported.

Use Options to specify save options. You can specify additional options using [ISldWorks::SetUserPreferenceIntegerValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.md). For example:

' Save assembly as multibody part and save exterior faces as surface bodies

swApp.SetUserPreferenceIntegerValue swSaveAssemblyAsPartOptions, \_

swSaveAsmAsPart\_ExteriorFaces

swModelDocExt.SaveAs "H:\Assem1.SLDPRT", swSaveAsCurrentVersion, \_

swSaveAsOptions\_Silent, Nothing, nErrors, nWarnings

- or -

' Save all drawing sheets in active drawing document as an eDrawings file

swApp.SetUserPreferenceIntegerValue swEdrawingsSaveAsSelectionOption, swEdrawingSaveAll

swModelDocExt.SaveAs "H:\Grid.edrw", swSaveAsCurrentVersion, \_

swSaveAsOptions\_Silent, Nothing, nErrors, nWarnings

If the file is saved successfully, then the returned value is true and Errors is 0. If the save is not successful, then the returned value is false and Errors contains a bitwise OR of the error codes that were generated in saving the document. Check the masks against the Errors enumeration. If you do not want SOLIDWORKS to return error information, set Errors to Nothing or null.

Even if the file is saved successfully, there might be warnings or information that occur during the save operation in which you might be interested. Warnings contains a bitwise OR of the warning codes that were generated when saving the document. Check the masks against the Warnings enumeration. If you do not want warning information returned, set Warnings to Nothing or null.

Use [IModelDoc2::Save3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.md) to save a file using its current name.

Example

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::SaveDeFeaturedFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDeFeaturedFile.md)  
[ISldWorks::CheckpointConvertedDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CheckpointConvertedDocument.md)  
[ISldWorks::CloseAllDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::CloseDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::CopyDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.md)  
[ISldWorks::ExitApp Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp.md)  
[ISldWorks::LoadFile4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)  
[ISldWorks::OpenDoc7 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md)  
[ISldWorks::QuitDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.md)

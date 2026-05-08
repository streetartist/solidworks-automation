# SaveAs2 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs2`

Obsolete. Superseded by IModelDocExtension::SaveAs3.
Obsolete. Superseded by [IModelDocExtension::SaveAs3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAs2( _
   ByVal Name As System.String, _
   ByVal Version As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal ExportData As System.Object, _
   ByVal ReferencePrefixOrSuffixText As System.String, _
   ByVal AddTextAsPrefix As System.Boolean, _
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
Dim ReferencePrefixOrSuffixText As System.String
Dim AddTextAsPrefix As System.Boolean
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean
 
value = instance.SaveAs2(Name, Version, Options, ExportData, ReferencePrefixOrSuffixText, AddTextAsPrefix, Errors, Warnings)
```

```

System.bool SaveAs2( 
   System.string Name,
   System.int Version,
   System.int Options,
   System.object ExportData,
   System.string ReferencePrefixOrSuffixText,
   System.bool AddTextAsPrefix,
   out System.int Errors,
   out System.int Warnings
)
```

```

System.bool SaveAs2( 
   System.String^ Name,
   System.int Version,
   System.int Options,
   System.Object^ ExportData,
   System.String^ ReferencePrefixOrSuffixText,
   System.bool AddTextAsPrefix,
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

*ReferencePrefixOrSuffixText*
:   Text to prefix names of reference files (AddTextAsPrefix is true) or text to suffix them (AddTextAsPrefix is false); empty string to neither prefix nor suffix the names of reference files; valid only for assemblies (see **Remarks**)

*AddTextAsPrefix*
:   True to prefix names of reference files with ReferencePrefixOrSuffixText, false to suffix names of reference files with ReferencePrefixOrSuffixText; valid only for assemblies and when ReferencePrefixOrSuffixText is a non-empty string (see **Remarks**)

*Errors*
:   Errors that caused the save to fail as defined in [swFileSaveError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html) (see **Remarks**)

*Warnings*
:   Warnings or extra information generated during the save operation as defined in [swFileSaveWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html) (see **Remarks**)

#### Return Value

True if the save is successful, false if not

Remarks

The difference between this method and the now obsolete [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md) is that when you save assemblies using this method, you can prefix or suffix reference file names by specifying AddTextAsPrefix and ReferencePrefixOrSuffixText. To save references in the assembly, specify Options by bitwise ANDing swSaveAsOptions\_e:

- swSaveAsOptions\_SaveReferenced
- swSaveAsOptions\_Copy or swSaveAsOptions\_CopyAndOpen
- swSaveAsOptions\_Silent

To save as an IGES, STL, or STEP file, the document to convert must be the active document. Before calling this method:

1. Call [ISldWorks::ActivateDoc3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc3.md) to make the document to convert the active document.
2. Call [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) to get the active document.

This method:

- Exports the entire model, unless faces or bodies are selected, in which case, it exports only those. Call [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md) before calling IModelDocExtension::SaveAs to clear the selection list and export the entire model.
- Overwrites existing files unless they are read only.
- Results in the FileSaveNotify event being sent to any application listening.
- Removes any configuration-specific bitmap previews, except the current configuration's.

Saving a document as PDF when the document is open as view only is not supported.

Do not use ModelDocExtension::SaveAs to copy assemblies, drawings, or parts with in-context references. Instead, use [ISldWorks::CopyDocument](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.md) or [ISldWorks::ICopyDocument](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.md).

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

If the file is saved successfully, then the returned value is true and Errors is 0. If the save is not successful, then the returned value is false and Errors contains a bitwise OR of the error codes that were generated in saving the document. Check the masks against the [swFileSaveError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html) enumeration. If you do not want SOLIDWORKS to return error information, set Errors to Nothing or null.

Even if the file is saved successfully, there might be warnings or information that occur during the save operation in which you might be interested. Warnings contains a bitwise OR of the warning codes that were generated when saving the document. Check the masks against the [swFileSaveWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html) enumeration. If you do not want warning information returned, set Warnings to Nothing or null.

Use [IModelDoc2::Save3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.md) to save a file using its current name.

Example

'VBA

'Preconditions:

'1. Open **C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\advdrawings\98food processor.sldasm**.

'2. Ensure **c:\temp** exists.

'Postconditions:

'1. Silently saves a copy of the assembly (**food\_processor\_Suff.sldasm**) and re-named reference files (**\*\_Suff.sldprt**) to **c:\temp**.

'2. Opens the saved assembly.

'3. Observe the re-named components in the FeatureManager design tree.

' NOTE: Because the model is used elsewhere, do not save changes.

'=========================================

Option Explicit

    Dim swApp                As SldWorks.SldWorks  
    Dim swModel             As SldWorks.ModelDoc2  
    Dim swModelDocExt   As SldWorks.ModelDocExtension  
    Dim boolstatus          As Boolean  
    Dim FileName            As String  
    Dim DIR                   As String  
    Dim EXT                   As String  
    Dim opt                    As Long  
    Dim lErrors               As Long  
    Dim lWarnings          As Long

Sub main()

    DIR = "c:\temp\"  
     
    EXT = ".SLDASM"  
    Set swApp = Application.SldWorks  
    swApp.Visible = True

    Set swModel = swApp.ActiveDoc  
    Set swModelDocExt = swModel.Extension  
    
    '1 =    swSaveAsOptions\_Silent  
    '4 =    swSaveAsOptions\_SaveReferenced  
    '512 = swSaveAsOptions\_CopyAndOpen  
      
    opt = 512 + 4 + 1  
     
    FileName = DIR & "food\_processor\_Suff" & EXT

    boolstatus = swModelDocExt.SaveAs2(FileName, 0, opt, Nothing, "\_Suff", False, lErrors, lWarnings)

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::SaveDeFeaturedFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDeFeaturedFile.md)  
[ISldWorks::ActivateDoc3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc3.md)  
[ISldWorks::ActiveDoc Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md)  
[ISldWorks::CheckpointConvertedDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CheckpointConvertedDocument.md)  
[ISldWorks::CloseAllDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::CloseDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::CopyDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.md)  
[ISldWorks::ExitApp Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp.md)  
[ISldWorks::LoadFile4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)  
[ISldWorks::OpenDoc7 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md)  
[ISldWorks::QuitDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.md)

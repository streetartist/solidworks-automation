# LoadFile4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4`

Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect.
Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadFile4( _
   ByVal FileName As System.String, _
   ByVal ArgString As System.String, _
   ByVal ImportData As System.Object, _
   ByRef Errors As System.Integer _
) As ModelDoc2
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim ArgString As System.String
Dim ImportData As System.Object
Dim Errors As System.Integer
Dim value As ModelDoc2
 
value = instance.LoadFile4(FileName, ArgString, ImportData, Errors)
```

```

ModelDoc2 LoadFile4( 
   System.string FileName,
   System.string ArgString,
   System.object ImportData,
   out System.int Errors
)
```

```

ModelDoc2^ LoadFile4( 
   System.String^ FileName,
   System.String^ ArgString,
   System.Object^ ImportData,
   [Out] System.int Errors
) 
```

#### Parameters

*FileName*
:   Full path and file name of the third-party native CAD part or assembly document to import (see **Remarks**)

*ArgString*
:   Space-separated string that allows optional arguments to be specified when opening a third-party native CAD file; empty string if 3D Interconnect is enabled (see Remarks)

*ImportData*
:   [IImportIgesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md), [IImportDxfDwgData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md), or [IImportStepData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData.md) object; null or Nothing if 3D Interconnect is not enabled (see Remarks)

*Errors*
:   Errors as defined in [swFileLoadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html)

#### Return Value

[Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Remarks

This method:

- Uses 3D Interconnect to load FileName into a new SOLIDWORKS document. Before calling this method, turn on 3D Interconnect by setting **Tools > Options > System Options > Import > Enable 3D Interconnect** or calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swMultiCAD\_Enable3DInterconnect, True). With 3D Interconnect enabled, this method supports the following third-party native CAD formats and versions:
  - ACIS: .sat, .sab, .asat, .asab for r1 - 2018 1.0
  - Autodesk® Inventor: .ipt for V6-V2018, .iam for V11 - V2018
  - CATIA® V5: .CATPart, .CATProduct for V5R8 - V5-6R2017
  - IGES: .igs, .iges for up to 5.3
  - JT: .jt for JT 8.x, 9.x, and 10.x
  - PTC®: .prt, .prt.\*, .asm.\* for Pro/ENGINEER® 16 - Creo 4.0
  - Solid Edge®: .par, .asm, .psm for V18 - ST10
  - STEP: .stp, .step for AP203, AP214, AP24
  - NX™ software: .prt for UG 11 - NX 11
- Imports FileName into the appropriate native SOLIDWORKS part or assembly.
  - For parts, the SOLIDWORKS file created is a copy of the original non-native file. The copy retains an external reference to the original CAD file. If the original third-party native file is modified in its orginal application, the SOLIDWORKS copy can be updated to import those changes. Changes to the SOLIDWORKS copy do not propagate back to the original file.
  - For assemblies, you must save the new SOLIDWORKS assembly in order for SOLIDWORKS to import the third-party native assembly and create the copy. Only after saving the new SOLIDWORKS assembly can you edit the imported top-level assembly or break its reference link. Editing lower-level components of the imported top-level assembly or individually breaking their reference links is not supported.
  - See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) Remarks for information about editing imported CAD data and breaking reference links to third-party native CAD parts and assemblies.
- Imports the geometry as a featureless solid body.
- Does not import FileName into any existing SOLIDWORKS file or the active document. To import a third-party native CAD file into an existing SOLIDWORKS:
  - Part, use [IPartDoc::InsertImportedFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertImportedFeature.md).
  - Assembly, use [IAssemblyDoc::InsertImportedComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent.md).
- Imports third-party native CAD files using different behavior if 3D Interconnect is not enabled:

|  |  |
| --- | --- |
| **If 3D Interconnect is not enabled and you are importing...** | **Then...** |
| Third-party native CAD files | Set ArgString to **FWNS** to display a FeatureWorks dialog after opening. |
| Pro/E files | - To import features, set ArgString to R - To import geometry, set ArgString to: - - B Direct geometry import with knitting   - C Direct geometry import without knitting   - D Geometry import with knitting   - E Geometry import without knitting   - S Surface geometry import with knitting   These arguments are case sensitive. Specifying one of these options suppresses dialog. |
| Non DXF/DWG and Non Pro/E files | - To import the foreign file into a new SOLIDWORKS document, set ArgString to r.   For example, to import an IGES file named cup.igs into a new SOLIDWORKS document:  Set swModel = swApp.LoadFile4 "D:\Samples\cup.IGS", "r", importData, Err.    See [IImportIgesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md) for details about importing IGES data.  NOTES:  - Whether the result is a surface or solid depends on the import options. See [Import and Export File Options](sldworksAPIProgGuide.chm::/OVERVIEW/Import_and_Export_File_Options.htm) for details. - If ArgString is set to an empty string, then dialogs may be presented to the end-user during translation. |
| DXF/DWG files | You can:   - Let SOLIDWORKS determine the default values:    - Paper size and sheet scale are computed to fit the input data.   - Length unit is determined from the header of the input DXF/DWG file.   - Sheet name is the same as the layout name in the input DXF/DWG file.   - or -   - Set your own values by using:    1. [ISldWorks::GetImportFileData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImportFileData.md) to obtain the IImportDxfDwgData interface.   2. Use the following methods with a Sheet argument of "" (an empty string) to set up your defaults before loading the file:       - [IImportDxfDwgData::GetPaperSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPaperSize.md)      - [IImportDxfDwgData::GetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPosition.md)      - [IImportDxfDwgData::GetSheetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetSheetScale.md)      - [IImportDxfDwgData::ImportMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.md)      - [IImportDxfDwgData::LengthUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~LengthUnit.md)      - [IImportDxfDwgData::SetPaperSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPaperSize.md)      - [IImportDxfDwgData::SetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPosition.md)      - [IImportDxfDwgData::SetSheetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetSheetScale.md)      - [IImportDxfDwgData::SheetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SheetName.md)   See [IImportDxfDwgData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md) for details about importing DXF/DWG data.  NOTES:   - Getting the IImportDxfDwgData interface does not get default values from the input file. Any values not set by you are set to the values computed by SOLIDWORKS. - If the DWG/DXF file has multiple sheets, use these methods with a valid layout name in the Sheet argument to set up sheet specific settings, which overrides the default settings. If any of the individual items are not specified for a given layout name, the value used is from the defaults (layout name ""). If the default value is not specified, SOLIDWORKS computes and uses a meaningful value for that item. |

Example

[Import DXF File Into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)  
[Import IGES File (VBA)](Import_IGES_File_Example_VB.htm)  
[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)  
[Use 3D Interconnect to Import Third-Party Native CAD Files (C#)](Import3DInterconnect_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)  
[IFeatureManager::InsertDwgOrDxfFile2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.md)

# IImport3DInterconnectData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData`

Allows access to 3D Interconnect feature data.
Allows access to 3D Interconnect feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IImport3DInterconnectData 
```

```

Dim instance As IImport3DInterconnectData
```

```

public interface IImport3DInterconnectData 
```

```

public interface class IImport3DInterconnectData 
```

Remarks

This interface requires 3D Interconnect. Enable 3D Interconnect by:

- Setting **Tools > Options > System Options > Import > Enable 3D Interconnect**.

    - or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swMultiCAD\_Enable3DInterconnect, True).

Access this interface after importing a third-party native CAD file into:

- an existing SOLIDWORKS part using [IPartDoc::InsertImportedFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertImportedFeature.md).
- an existing SOLIDWORKS assembly using [IAssemblyDoc::InsertImportedComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent.md).
- a new SOLIDWORKS part using [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md).
- a new SOLIDWORKS assembly using ISldWorks::LoadFile4.

Use [IFeature::Is3DInterconnectFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectFeature.md) to determine whether a feature is a 3D Interconnect feature and whether this interface applies.

ISldWorks::LoadFile4 imports into the appropriate native SOLIDWORKS part or assembly as follows:

- For both imported parts and assemblies, you can:
  - Determine whether an update is required ([IFeature::Is3DInterconnectUpdateAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectUpdateAvailable.md)) and update the model ([IFeature::Update3DInterconnectModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Update3DInterconnectModel.md)).
  - Edit the imported data using this interface, its accessor (IFeature::GetImportedFeatureParameters), or [IFeature::SetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.md).
  - Break the link to the original third-party native CAD file using [IFeature::BreakLink](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~BreakLink.md). After you break a link, all references to the original CAD file are lost, and you can no longer change the features to transfer from the original file.
- For imported parts only, the native SOLIDWORKS file created is a copy of the original non-native file. The copy retains an external reference to the original third-party native CAD file. If the original CAD file is modified in its orginal application, the SOLIDWORKS copy can be updated to import those changes. Changes to the SOLIDWORKS copy do not propagate back to the original CAD file.
- For imported assemblies only, after import you must save the new SOLIDWORKS assembly in order for SOLIDWORKS to import and create a copy to edit. Only after saving the new SOLIDWORKS assembly can you edit the imported top-level assembly or break its reference links. Editing lower-level imported components or individually breaking their reference links is not supported.

3D Interconnect supports the following third-party native CAD file formats and versions:

- ACIS: .sat, .sab, .asat, .asab for r1 - 2018 1.0
- Autodesk® Inventor: .ipt for V6-V2018, .iam for V11 - V2018
- CATIA® V5: .CATPart, .CATProduct for V5R8 - V5-6R2017
- IGES: .igs, .iges for up to 5.3
- JT: .jt for JT 8.x, 9.x, and 10.x
- PTC®: .prt, .prt.\*, .asm.\* for Pro/ENGINEER® 16 - Creo 4.0
- Solid Edge®: .par, .asm, .psm for V18 - ST10
- STEP: .stp, .step for AP203, AP214, AP242
- NX™ software: .prt for UG 11 - NX 11

The transfer properties of this interface apply to a subset of supported third-party native CAD files (e.g., Inventor, CATIA V5, Creo, NX, Solid Edge, and a few others). The types of properties that can be imported vary with file format. See the **SOLIDWORKS 3D Interconnect** topics in the SOLIDWORKS user-interface help for specific information.

Example

[Use 3D Interconnect to Import Third-Party Native CAD Files (C#)](Import3DInterconnect_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

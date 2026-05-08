# IImportDxfDwgData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData`

Allows you to specify values when importing or inserting DXF/DWG data.
Allows you to specify values when importing or inserting DXF/DWG data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IImportDxfDwgData 
```

```

Dim instance As IImportDxfDwgData
```

```

public interface IImportDxfDwgData 
```

```

public interface class IImportDxfDwgData 
```

Remarks

When importing DXF/DWG data, you can:

- Let SOLIDWORKS determine the default values:

  - Paper size and sheet scale are computed to fit the input data.
  - Length unit is determined from the header of the input DXF/DWG file.
  - Sheet name is the same as the layout name in the input DXF/DWG file.

     - or -

- Set your own values by using:

  1. [ISldWorks::GetImportFileData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImportFileData.md) to obtain the IImportDxfDwgData interface.
  2. Use the following methods with a Sheet argument of "" (an empty string), to set up your defaults before importing or inserting the file:

     - [IImportDxfDwgData::GetPaperSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPaperSize.md)
     - [IImportDxfDwgData::GetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPosition.md)
     - [IImportDxfDwgData::GetSheetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetSheetScale.md)
     - [IImportDxfDwgData::ImportMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.md)
     - [IImportDxfDwgData::LengthUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~LengthUnit.md)
     - [IImportDxfDwgData::SetPaperSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPaperSize.md)
     - [IImportDxfDwgData::SetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPosition.md)
     - [IImportDxfDwgData::SetSheetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetSheetScale.md)
     - [IImportDxfDwgData::SheetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SheetName.md)

NOTES:

- Getting the IImportDxfDwgData interface does not get default values from the input file. Any values not set by you are set to the values computed by SOLIDWORKS.
- If the DWG/DXF file has multiple sheets, use these methods with a valid layout name in the Sheet argument to set up sheet specific settings, which override the default settings. If any of the individual items are not specified for a given layout name, the value used is from the defaults (layout name ""). If the default value is not specified, SOLIDWORKS computes and uses a meaningful value for that item.

When inserting DXF/DWG data as a feature into the current model document, first select a plane or planar surface and then call [IFeatureManager::InsertDwgOrDxfFile2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.md).

Call [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md) to import the DXF/DWG file as a new SOLIDWORKS model document.

Example

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)  
[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)  
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)  
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)  
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)  
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)  
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md)

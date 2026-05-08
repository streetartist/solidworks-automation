# InsertDwgOrDxfFile2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2`

Inserts a DXF/DWG image feature.
Inserts a DXF/DWG image feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertDwgOrDxfFile2( _
   ByVal FileName As System.String, _
   ByVal DxfDwgImportData As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim FileName As System.String
Dim DxfDwgImportData As System.Object
Dim value As Feature
 
value = instance.InsertDwgOrDxfFile2(FileName, DxfDwgImportData)
```

```

Feature InsertDwgOrDxfFile2( 
   System.string FileName,
   System.object DxfDwgImportData
)
```

```

Feature^ InsertDwgOrDxfFile2( 
   System.String^ FileName,
   System.Object^ DxfDwgImportData
) 
```

#### Parameters

*FileName*
:   Name of the DXF/DWG image file

*DxfDwgImportData*
:   [IImportDxfDwgData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, select a plane or planar surface on which to place the image.

This method:

- returns Nothing or null if the file contains solid bodies data.
- is not supported for use in assembly documents.

When importing DXF/DWG data, you can:

- Let SOLIDWORKS determine the default values:
- - Paper size and sheet scale are computed to fit the input data.
  - Length unit is determined from the header of the input DXF/DWG file.
  - Sheet nameis the same as the layout name in the input DXF/DWG file.

     - or -

- Set your own values:

  1. Call [ISldWorks::GetImportFileData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImportFileData.md) to obtain the IImportDxfDwgData interface.
  2. Use the following methods with a Sheet argument of "" (an empty string), to set up your defaults:

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
- If the DWG/DXF file has multiple sheets, use these methods with a valid layout name in the Sheet argument to set up sheet specific settings, which override the default settings. If any of the individual items are not specified for a given layout name, then the value used is from the defaults (layout name ""). If the default value is not specified, then SOLIDWORKS computes and uses a meaningful value for that item.

Example

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

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)

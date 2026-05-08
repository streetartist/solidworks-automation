# GetImportFileData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImportFileData`

Gets the IGES or DXF/DWG import data for the specified file.
Gets the IGES or DXF/DWG import data for the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetImportFileData( _
   ByVal FileName As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object
 
value = instance.GetImportFileData(FileName)
```

```

System.object GetImportFileData( 
   System.string FileName
)
```

```

System.Object^ GetImportFileData( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and name of the IGES or DXF/DWG file

#### Return Value

[IGES import data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md) or [DXF/DWG import data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)

Remarks

Getting the interface object does not retrieve any information from the input file or set up defaults at this time. Instead, it sets up information such that when it is used in the import process, SOLIDWORKS will compute defaults on the fly.

Example

[Import DXF File Into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)  
[Import DXF File Into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)  
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)  
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)  
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)  
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)  
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)  
[IFeatureManager::InsertDwgOrDxfFile2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.md)

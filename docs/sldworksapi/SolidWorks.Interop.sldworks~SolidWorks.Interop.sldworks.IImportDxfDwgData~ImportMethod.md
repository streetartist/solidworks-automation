# ImportMethod Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod`

Gets or sets whether to import this sheet (layout).
Gets or sets whether to import this sheet (layout).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportMethod( _
   ByVal Sheet As System.String _
) As System.Integer
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Integer
 
instance.ImportMethod(Sheet) = value
 
value = instance.ImportMethod(Sheet)
```

```

System.int ImportMethod( 
   System.string Sheet
) {get; set;}
```

```

property System.int ImportMethod {
   System.int get(System.String^ Sheet);
   void set (System.String^ Sheet, System.int value);
}
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets (see **Remarks**)

#### Property Value

Import method as defined in [swImportDxfDwg\_ImportMethod\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportDxfDwg_ImportMethod_e.html)

Remarks

By default, all sheets are imported into a new drawing.

|  |  |
| --- | --- |
| If you want to import... | Then set... |
| All sheets except for a specific one into a new drawing | ImportDxfDwgData.ImportMethod("<sheet to exclude>") = swImportDxfDwg\_DoNotImportSheet |
| Only a single sheet into a sketch in a new part | ImportDxfDwgData.ImportMethod("") = swImportDxfDwg\_DoNotImportSheet    to make the default not to import sheets. Then set:    ImportDxfDwgData.ImportMethod("<sheet to import>") = swImportDxfDwg\_ImportToPartSketch   to import only this sheet. |

Example

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)  
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)  
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)  
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)  
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)  
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.md)  
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.md)  
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.md)  
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.md)

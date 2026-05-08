# LengthUnit Property (IImportDxfDwgData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~LengthUnit`

Gets or sets the length units for the drawing.
Gets or sets the length units for the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LengthUnit( _
   ByVal Sheet As System.String _
) As System.Integer
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Integer
 
instance.LengthUnit(Sheet) = value
 
value = instance.LengthUnit(Sheet)
```

```

System.int LengthUnit( 
   System.string Sheet
) {get; set;}
```

```

property System.int LengthUnit {
   System.int get(System.String^ Sheet);
   void set (System.String^ Sheet, System.int value);
}
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

#### Property Value

Length as defined in [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html)

Remarks

By default, the length is determined from the header of the input DWG/DXF file.

Example

[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)  
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)  
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)  
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)  
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)  
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)

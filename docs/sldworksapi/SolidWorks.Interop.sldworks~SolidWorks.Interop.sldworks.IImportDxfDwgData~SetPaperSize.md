# SetPaperSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPaperSize`

Sets the size of the paper in the drawing.
Sets the size of the paper in the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPaperSize( _
   ByVal Sheet As System.String, _
   ByVal Size As System.Integer, _
   ByVal Height As System.Double, _
   ByVal Width As System.Double _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Size As System.Integer
Dim Height As System.Double
Dim Width As System.Double
Dim value As System.Boolean
 
value = instance.SetPaperSize(Sheet, Size, Height, Width)
```

```

System.bool SetPaperSize( 
   System.string Sheet,
   System.int Size,
   System.double Height,
   System.double Width
)
```

```

System.bool SetPaperSize( 
   System.String^ Sheet,
   System.int Size,
   System.double Height,
   System.double Width
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

*Size*
:   Size as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Height*
:   If Size is swDwgPapersUserDefined, then the height of the paper in meters

*Width*
:   If Size is swDwgPapersUserDefined, then the width of the paper in meters

#### Return Value

True if paper size is set, false if not

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Example

[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)  
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)  
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)  
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetPaperSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPaperSize.md)

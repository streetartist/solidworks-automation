# SetSheetScale Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetSheetScale`

Sets the sheet scale for the drawing.
Sets the sheet scale for the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSheetScale( _
   ByVal Sheet As System.String, _
   ByVal Numerator As System.Double, _
   ByVal Denominator As System.Double _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Numerator As System.Double
Dim Denominator As System.Double
Dim value As System.Boolean
 
value = instance.SetSheetScale(Sheet, Numerator, Denominator)
```

```

System.bool SetSheetScale( 
   System.string Sheet,
   System.double Numerator,
   System.double Denominator
)
```

```

System.bool SetSheetScale( 
   System.String^ Sheet,
   System.double Numerator,
   System.double Denominator
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

*Numerator*
:   Numerator of the scale

*Denominator*
:   Denominator of the scale

#### Return Value

True if the sheet scale is set, false if not

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
[IImportDxfDwgData::GetSheetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetSheetScale.md)

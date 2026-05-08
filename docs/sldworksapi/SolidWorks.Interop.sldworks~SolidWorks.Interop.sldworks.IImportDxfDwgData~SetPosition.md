# SetPosition Method (IImportDxfDwgData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPosition`

Sets the position of the entities created in the drawing.
Sets the position of the entities created in the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPosition( _
   ByVal Sheet As System.String, _
   ByVal Positioning As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Positioning As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim value As System.Boolean
 
value = instance.SetPosition(Sheet, Positioning, X, Y)
```

```

System.bool SetPosition( 
   System.string Sheet,
   System.int Positioning,
   System.double X,
   System.double Y
)
```

```

System.bool SetPosition( 
   System.String^ Sheet,
   System.int Positioning,
   System.double X,
   System.double Y
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

*Positioning*
:   Position as defined in [swDwgImportEntitiesPositioning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgImportEntitiesPositioning_e.html)

*X*
:   X coordinate of the origin of the imported drawing

*Y*
:   Y coordinate of the origin of the imported drawing

#### Return Value

True if the position is set, false if not

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Example

[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)  
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)  
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPosition.md)

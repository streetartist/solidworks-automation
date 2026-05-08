# SheetName Property (IImportDxfDwgData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SheetName`

Gets or sets the name of the sheet for the drawing.
Gets or sets the name of the sheet for the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SheetName( _
   ByVal Sheet As System.String _
) As System.String
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.String
 
instance.SheetName(Sheet) = value
 
value = instance.SheetName(Sheet)
```

```

System.string SheetName( 
   System.string Sheet
) {get; set;}
```

```

property System.String^ SheetName {
   System.String^ get(System.String^ Sheet);
   void set (System.String^ Sheet, System.String^ value);
}
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

#### Property Value

Name of sheet

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Example

[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)

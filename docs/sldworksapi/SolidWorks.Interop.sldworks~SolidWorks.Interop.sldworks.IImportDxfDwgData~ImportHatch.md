# ImportHatch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportHatch`

Gets or sets whether to import hatch into this part sketch.
Gets or sets whether to import hatch into this part sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportHatch( _
   ByVal Sheet As System.String _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Boolean
 
instance.ImportHatch(Sheet) = value
 
value = instance.ImportHatch(Sheet)
```

```

System.bool ImportHatch( 
   System.string Sheet
) {get; set;}
```

```

property System.bool ImportHatch {
   System.bool get(System.String^ Sheet);
   void set (System.String^ Sheet, System.bool value);
}
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

#### Property Value

True to import hatch, false to not

Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, hatch will be imported.

Example

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)

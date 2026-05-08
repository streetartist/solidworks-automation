# AddSketchConstraints Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~AddSketchConstraints`

Gets or sets whether constraints are added to the geometry in the part sketch after importing the entities.
Gets or sets whether constraints are added to the geometry in the part sketch after importing the entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddSketchConstraints( _
   ByVal Sheet As System.String _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Boolean
 
instance.AddSketchConstraints(Sheet) = value
 
value = instance.AddSketchConstraints(Sheet)
```

```

System.bool AddSketchConstraints( 
   System.string Sheet
) {get; set;}
```

```

property System.bool AddSketchConstraints {
   System.bool get(System.String^ Sheet);
   void set (System.String^ Sheet, System.bool value);
}
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

#### Property Value

True to add constraints, false to not

Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, constraints are not added.

Example

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)

# Text2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text2`

Gets or sets the parametrized string of text for the specified cell of this table.
Gets or sets the parametrized string of text for the specified cell of this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Text2( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.String
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.String
 
instance.Text2(Row, Column, IncludeHidden) = value
 
value = instance.Text2(Row, Column, IncludeHidden)
```

```

System.string Text2( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden
) {get; set;}
```

```

property System.String^ Text2 {
   System.String^ get(System.int Row, System.int Column, System.bool IncludeHidden);
   void set (System.int Row, System.int Column, System.bool IncludeHidden, System.String^ value);
}
```

#### Parameters

*Row*
:   Index of the row

*Column*
:   Index of the column

*IncludeHidden*
:   True to get or set text in the hidden cell, false to not

#### Property Value

Cell text

Remarks

Index for both rows and columns is 0-based.

This property returns the string that drives the text displayed in the specified cell. For example, the string returned by this property would be the parameter string if the cell is linked to a dimension value or custom property. To get the text actually displayed in the cell, use [ITableAnnotation::DisplayedText2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText2.md).

Table annotation:

- [BOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md): All cells are editable.
- [General](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation.md): All cells are editable.
- [Hole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md): Only columns that are not automatically generated are editable. The header row and custom columns are editable.
- [Revision](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.md): All cells are editable

You might experience decreased performance when updating the text in multiple cells in large tables, because the table automatically rebuilds each time you change the text in a cell. To increase performance while updating the text in large tables:

1. Set [IAnnotation::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible.md) to false. (The table is not rebuilt while the table is hidden.)
2. Update the text in the table cells.
3. Set IAnnotation::Visible to true.

Example

[Insert BOM Table and Extract Data (VBA)](Insert_BOM_Table_and_Extract_Data_Example_VB.htm)  
[Insert BOM Table and Extract Data (VB.NET)](Insert_BOM_Table_and_Extract_Data_Example_VBNET.htm)  
[Insert BOM Table and Extract Data (C#)](Insert_BOM_Table_and_Extract_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)

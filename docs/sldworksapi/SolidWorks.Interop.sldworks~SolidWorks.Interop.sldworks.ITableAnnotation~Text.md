# Text Property (ITableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text`

Obsolete. Superseded by ITableAnnotation::Text2.
Obsolete. Superseded by [ITableAnnotation::Text2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Text( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.String
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.String
 
instance.Text(Row, Column) = value
 
value = instance.Text(Row, Column)
```

```

System.string Text( 
   System.int Row,
   System.int Column
) {get; set;}
```

```

property System.String^ Text {
   System.String^ get(System.int Row, System.int Column);
   void set (System.int Row, System.int Column, System.String^ value);
}
```

#### Parameters

*Row*
:   Index of the row

*Column*
:   Index of the column

#### Property Value

Cell text

Remarks

Index for both rows and columns is 0-based.

This property returns the string that drives the text displayed in the specified cell. For example, the string returned by this property would be the parameter string if the cell is linked to a dimension value or custom property. To get the text actually displayed in the cell, use [ITableAnnotation::DisplayedText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText.md).

Table annotation:

- [BOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md): All cells are editable.
- [General](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md): All cells are editable.
- [Hole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md): Only some columns are editable because some information is automatically generated, thus, that information cannot be edited. The header row and custom columns are editable.
- [Revision](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.md): All cells are editable

You might experience decreased performance when updating  the text in multiple cells in large tables because the table is rebuilt after changing the text in a cell. To increase performance while updating the text in large tables:

1. Set [IAnnotation::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible.md) to false. (The table is not rebuilt while the table is hidden.)
2. Update the text in the table cells.
3. Set IAnnotation::Visible to true.

Example

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)  
[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.md)  
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.md)  
[ITableAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetTextFormat.md)  
[ITableAnnotation::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetUseDocTextFormat.md)  
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.md)  
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.md)  
[ITableAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetTextFormat.md)  
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.md)  
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.md)

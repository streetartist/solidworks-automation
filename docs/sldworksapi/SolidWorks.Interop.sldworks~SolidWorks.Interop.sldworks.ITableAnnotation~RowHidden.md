# RowHidden Property (ITableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden`

Gets or sets whether the specified row is hidden in this table.
Gets or sets whether the specified row is hidden in this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RowHidden( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim value As System.Boolean
 
instance.RowHidden(Index) = value
 
value = instance.RowHidden(Index)
```

```

System.bool RowHidden( 
   System.int Index
) {get; set;}
```

```

property System.bool RowHidden {
   System.bool get(System.int Index);
   void set (System.int Index, System.bool value);
}
```

#### Parameters

*Index*
:   Index of row

#### Property Value

True if hidden, false if not

Remarks

The index for both the rows and columns is 0-based.

Example

[Hide and Show Row (VBA)](Hide_and_Show_Row_Example_VB.htm)  
[Insert General Table (VBA)](Insert_General_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::TotalRowCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.md)  
[ITableAnnotation::DeleteColumn Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.md)  
[ITableAnnotation::GetLockRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.md)  
[ITableAnnotation::GetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.md)  
[ITableAnnotation::GetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.md)  
[ITableAnnotation::InsertRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.md)  
[ITableAnnotation::MoveRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.md)  
[ITableAnnotation::SetLockRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.md)  
[ITableAnnotation::SetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.md)  
[ITableAnnotation::SetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.md)  
[ITableAnnotation::RowCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.md)

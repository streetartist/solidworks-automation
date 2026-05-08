# InsertRow Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow`

Inserts a row into this table.
Inserts a row into this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRow( _
   ByVal Where As System.Integer, _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.InsertRow(Where, Index)
```

```

System.bool InsertRow( 
   System.int Where,
   System.int Index
)
```

```

System.bool InsertRow( 
   System.int Where,
   System.int Index
) 
```

#### Parameters

*Where*
:   Where to insert the new row as defined in [swTableItemInsertPosition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableItemInsertPosition_e.html)

*Index*
:   Index of row where to insert new row (see **Remarks**)

Remarks

Index:

- is 0-based.
- is valid only if Where is set to swTableItemInsertPosition\_e.swTableItemInsertPosition\_After or swTableItemInsertPosition\_e.swTableItemInsertPosition\_Before.

Example

[Sort Table (VBA)](Sort_Table_Example_VB.htm)  
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)  
[Sort Table (C#)](Sort_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::DeleteRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.md)  
[ITableAnnotation::GetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.md)  
[ITableAnnotation::GetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.md)  
[ITableAnnotation::MoveRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.md)  
[ITableAnnotation::SetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.md)  
[ITableAnnotation::SetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.md)  
[ITableAnnotation::RowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.md)  
[ITableAnnotation::TotalRowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.md)  
[ITableAnnotation::GetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.md)  
[ITableAnnotation::SetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.md)  
[ITableAnnotation::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.md)

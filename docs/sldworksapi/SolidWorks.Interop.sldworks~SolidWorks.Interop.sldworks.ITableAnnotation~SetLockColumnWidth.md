# SetLockColumnWidth Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth`

Sets whether to lock the width of the specified column in this table annotation.
Sets whether to lock the width of the specified column in this table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLockColumnWidth( _
   ByVal Index As System.Integer, _
   ByVal LockColumnWidth As System.Boolean _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim LockColumnWidth As System.Boolean
Dim value As System.Boolean
 
value = instance.SetLockColumnWidth(Index, LockColumnWidth)
```

```

System.bool SetLockColumnWidth( 
   System.int Index,
   System.bool LockColumnWidth
)
```

```

System.bool SetLockColumnWidth( 
   System.int Index,
   System.bool LockColumnWidth
) 
```

#### Parameters

*Index*
:   0-based index of the column (see **Remarks**)

*LockColumnWidth*
:   True to lock this column's width, false to not

#### Return Value

True if setting whether to lock the width of the specified column is successful, false if not

Remarks

Call [ITableAnnotation::ColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.md) to get the number of visible columns or [ITableAnnotation::TotalColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.md) to get the number of visible and hidden columns in this table annotation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetLockColumnWidth Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.md)  
[ITableAnnotation::DeleteColumn Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.md)  
[ITableAnnotation::GetColumnTitle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.md)  
[ITableAnnotation::GetColumnType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.md)  
[ITableAnnotation::GetColumnWidth Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.md)  
[ITableAnnotation::InsertColumn2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn2.md)  
[ITableAnnotation::MoveColumn Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.md)  
[ITableAnnotation::SetColumnTitle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.md)  
[ITableAnnotation::SetColumnType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.md)  
[ITableAnnotation::SetColumnWidth Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.md)  
[ITableAnnotation::ColumnHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.md)

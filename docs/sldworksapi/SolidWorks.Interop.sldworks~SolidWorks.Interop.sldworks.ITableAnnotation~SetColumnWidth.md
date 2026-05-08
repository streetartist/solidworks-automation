# SetColumnWidth Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth`

Sets the width of the specified column in this table.
Sets the width of the specified column in this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColumnWidth( _
   ByVal Index As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Options As System.Integer _
) As System.Double
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Width As System.Double
Dim Options As System.Integer
Dim value As System.Double
 
value = instance.SetColumnWidth(Index, Width, Options)
```

```

System.double SetColumnWidth( 
   System.int Index,
   System.double Width,
   System.int Options
)
```

```

System.double SetColumnWidth( 
   System.int Index,
   System.double Width,
   System.int Options
) 
```

#### Parameters

*Index*
:   Index of column for which to set the width

*Width*
:   Width at which to set specified column, in system units

*Options*
:   Table's behavior after changing column width as defined by [swTableRowColSizeChangeBehavior\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableRowColSizeChangeBehavior_e.html) (see **Remarks**)

#### Return Value

Width at which specified column is set (see **Remarks**)

Remarks

Index is the column number for which to set the width. Thus, the first column is column 0. It can also be a value from the [swTableCellRangeIdentifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableCellRangeIdentifier_e.html) enumerator.

|  |  |
| --- | --- |
| **If Index equals...** | **Then the width of all of the columns...** |
| swTableCellRange\_All | Is set, if possible. |
| swTableCellRange\_Current | In the current range (see [ITableAnnotation::GetCellRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.md) and [ITableAnnotation::SetCellRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.md)) is set, if possible. |

When the width of a column changes, the rest of the table is affected. The Options argument indicates how the rest of the table should behave.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Options = swTableRowColChange\_TableSizeCanChange | The rest of the columns remain the same width and are shifted away from the table anchor to make room for the changed column. |
| Width of the entire table must remain the same, so that the table continues to fit properly on the drawing | Other columns must absorb the change in width.  There are two possibilities supported by this method.     - If Options = swTableRowColChange\_AbsorbedByNext, then the first column to the right of the columns whose width has changed, is adjusted if possible. If that is not possible, then the first column to the left of the columns whose width has changed, is adjusted if possible. If that is not possible either, then no action is taken. - The other similar case is if Options = swTableRowColChange\_AbsorbedByPrevious. First the column to the left is tried, then the column to the right. |
| Options = swTableRowColChange\_AbsorbedByNext or swTableRowColChange\_AbsorbedByPrevious | It may not be possible to get the desired results. If this is the case, you must determine the full width of the table yourself and set row widths individually using the swTableRowColChange\_TableSizeCanChange option, making sure to end up with the original table width. |

The return value is the width that the column is set to. If you specified a range of columns, it is the width of the first column of that range.

It is possible that the return value is different than the width value that you passed in. One possibility is that if you specify a column width that is less than the minimum column width, the minimum column width is used, instead of what you specified. Another possibility is that if you are trying to maintain a fixed table width, but the width of the adjacent columns is not big enough to absorb the width changes to the columns that you specified, then the return value is the same as the column's original width instead of what you specified.

To get the column width, use [ITableAnnotation::GetColumnWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.md).

To get or set the row height, use [ITableAnnotation::GetRowHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.md) and [ITableAnnotation::SetRowHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::DeleteColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.md)  
[ITableAnnotation::GetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.md)  
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.md)  
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.md)  
[ITableAnnotation::InsertColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn.md)  
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.md)  
[ITableAnnotation::SetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.md)  
[ITableAnnotation::SetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.md)  
[ITableAnnotation::ColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.md)  
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.md)  
[ITableAnnotation::TotalColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.md)  
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.md)  
[ITableAnnotation::SetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.md)

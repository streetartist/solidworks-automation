# SetRowHeight Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight`

Sets the height of the specified row in this table.
Sets the height of the specified row in this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRowHeight( _
   ByVal Index As System.Integer, _
   ByVal Height As System.Double, _
   ByVal Options As System.Integer _
) As System.Double
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Height As System.Double
Dim Options As System.Integer
Dim value As System.Double
 
value = instance.SetRowHeight(Index, Height, Options)
```

```

System.double SetRowHeight( 
   System.int Index,
   System.double Height,
   System.int Options
)
```

```

System.double SetRowHeight( 
   System.int Index,
   System.double Height,
   System.int Options
) 
```

#### Parameters

*Index*
:   Index of row for which to set height

*Height*
:   Height at which to set specified row, in system units

*Options*
:   Table's behavior after changing row as defined by [swTableRowColSizeChangeBehavior\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableRowColSizeChangeBehavior_e.html) (see **Remarks**)

#### Return Value

Height to which specified row is set (see **Remarks**)

Remarks

The index for both rows and columns is 0-based.

Index is the number of the row whose height to set. The first row is row 0.  It can also be a value from the [swTableCellRangeIdentifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableCellRangeIdentifier_e.html) enumerator.

| **If Index equals...** | **Then the height of all of the rows...** |
| --- | --- |
| swTableCellRange\_All | Is set, if possible. |
| swTableCellRange\_Current | In the current range (see [ITableAnnotation::GetCellRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.md) and [ITableAnnotation::SetCellRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.md)) is set, if possible |

When the height of a row changes, then the rest of the table is affected. The Options argument indicates the rest of the table's behavior.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Options = swTableRowColChange\_TableSizeCanChange | The rest of the rows remain the same height and are shifted away from the table anchor to make room for the changed row. |
| Height of the entire table must remain the same, so that the table continues to fit properly on the drawing | Other rows must absorb the change in height. There are two possibilities supported by this method.   - If Options = swTableRowColChange\_AbsorbedByNext, then first row below the rows whose height has changed, are adjusted if possible.  If that is not possible, then the first row above the rows whose height has changed, is adjusted if possible. If that is not possible either, then no action is taken. - The other similar case is if Options = swTableRowColChange\_AbsorbedByPrevious. First the row above is tried, then the row below. |
| Options = swTableRowColChange\_AbsorbedByNext or swTableRowColChange\_AbsorbedByPrevious | It might not be possible to get the desired results. If this is the case, then you must determine the full height of the table yourself and set row heights individually using the swTableRowColChange\_TableSizeCanChange option, making sure to end up with the original  table height. |

The return value is the height at which the row is set. If you specified a range of rows, it is the height of the first row of that range.

It is possible that the return value is different than the value that you passed in. One possibility is that if you specify a row height that is less than the minimum row height, then the minimum row height is used instead of what you specified. Another possibility is that if you are trying to maintain a fixed table height, but the height of the adjacent rows is not big enough to absorb the height changes to the rows that you specified, then the return value is the same as the row's original width instead of what you specified.

To get the row height, use [ITableAnnotation::GetRowHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.md).

To get or set the column width, use [ITableAnnotation::GetColumnWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.md) and [ITableAnnotation::SetColumnWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::DeleteRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.md)  
[ITableAnnotation::GetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.md)  
[ITableAnnotation::InsertRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.md)  
[ITableAnnotation::MoveRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.md)  
[ITableAnnotation::SetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.md)  
[ITableAnnotation::RowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.md)  
[ITableAnnotation::TotalRowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.md)  
[ITableAnnotation::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.md)  
[ITableAnnotation::GetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.md)  
[ITableAnnotation::SetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.md)

# SetCellRange Method (ISelectData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~SetCellRange`

Sets the specified range of table cells for this selection.
Sets the specified range of table cells for this selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCellRange( _
   ByVal FirstRow As System.Integer, _
   ByVal LastRow As System.Integer, _
   ByVal FirstColumn As System.Integer, _
   ByVal LastColumn As System.Integer _
) 
```

```

Dim instance As ISelectData
Dim FirstRow As System.Integer
Dim LastRow As System.Integer
Dim FirstColumn As System.Integer
Dim LastColumn As System.Integer
 
instance.SetCellRange(FirstRow, LastRow, FirstColumn, LastColumn)
```

```

void SetCellRange( 
   System.int FirstRow,
   System.int LastRow,
   System.int FirstColumn,
   System.int LastColumn
)
```

```

void SetCellRange( 
   System.int FirstRow,
   System.int LastRow,
   System.int FirstColumn,
   System.int LastColumn
) 
```

#### Parameters

*FirstRow*
:   0-based row number at the beginning of the selection range

*LastRow*
:   0-based row number at the end of the selection range

*FirstColumn*
:   0-based row column at the beginning of the selection range

*LastColumn*
:   0-based row column at the end of the selection range

Remarks

The range of table cells are only used for a selection made in a table. For all other types of selections, these values are ignored.

By default, the value for FirstRow, LastRow, FirstColumn, and LastColumn is -1, which indicates that the entire table is selected.

|  |  |
| --- | --- |
| To select an entire... | Set... |
| Row | - FirstColumn and LastColumn to value values - FirstRow LastRow to -1 |
| Column | - FirstRow and LastRow to valid values - FirstColumn and LastColumn to -1 |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)  
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.md)  
[ISelectData::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~GetCellRange.md)

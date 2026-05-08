# GetCellData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetCellData`

Gets data from the specified table cell of this Hole Wizard fastener table.
Gets data from the specified table cell of this Hole Wizard fastener table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCellData( _
   ByVal ColumnName As System.String, _
   ByVal RowIndex As System.Integer, _
   ByRef CellData As System.String _
) As System.Boolean
```

```

Dim instance As IHoleDataTable
Dim ColumnName As System.String
Dim RowIndex As System.Integer
Dim CellData As System.String
Dim value As System.Boolean
 
value = instance.GetCellData(ColumnName, RowIndex, CellData)
```

```

System.bool GetCellData( 
   System.string ColumnName,
   System.int RowIndex,
   out System.string CellData
)
```

```

System.bool GetCellData( 
   System.String^ ColumnName,
   System.int RowIndex,
   [Out] System.String^ CellData
) 
```

#### Parameters

*ColumnName*
:   Column name (see **Remarks**)

*RowIndex*
:   0-based row index

*CellData*
:   Cell data

#### Return Value

True if cell data successfully retrieved, false if not

Remarks

To set:

- ColumnName, use [IHoleDataTable::GetColumnNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetColumnNames.md).
- RowIndex, use [IHoleDataTable::GetRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowCount.md).

Example

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md)  
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.md)

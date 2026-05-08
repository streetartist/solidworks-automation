# GetRowData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowData`

Gets data for the specified row of this Hole Wizard fastener table.
Gets data for the specified row of this Hole Wizard fastener table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRowData( _
   ByVal RowIndex As System.Integer, _
   ByRef RowData As System.Object _
) As System.Boolean
```

```

Dim instance As IHoleDataTable
Dim RowIndex As System.Integer
Dim RowData As System.Object
Dim value As System.Boolean
 
value = instance.GetRowData(RowIndex, RowData)
```

```

System.bool GetRowData( 
   System.int RowIndex,
   out System.object RowData
)
```

```

System.bool GetRowData( 
   System.int RowIndex,
   [Out] System.Object^ RowData
) 
```

#### Parameters

*RowIndex*
:   0-based index of row

*RowData*
:   Row data

#### Return Value

True if row data successfully retrieved, false if not

Remarks

To set RowIndex, use [IHoleDataTable::GetRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowCount.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md)  
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.md)

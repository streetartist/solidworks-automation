# GetRowCount Method (IHoleDataTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowCount`

Gets the number of rows in this Hole Wizard fastener table.
Gets the number of rows in this Hole Wizard fastener table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRowCount( _
   ByRef RowCount As System.Integer _
) As System.Boolean
```

```

Dim instance As IHoleDataTable
Dim RowCount As System.Integer
Dim value As System.Boolean
 
value = instance.GetRowCount(RowCount)
```

```

System.bool GetRowCount( 
   out System.int RowCount
)
```

```

System.bool GetRowCount( 
   [Out] System.int RowCount
) 
```

#### Parameters

*RowCount*
:   Number of rows

#### Return Value

True if number of rows successfully retrieved, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md)  
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.md)  
[IHoleDataTable::GetCellData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetCellData.md)  
[IHoleDataTable::GetRowData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowData.md)

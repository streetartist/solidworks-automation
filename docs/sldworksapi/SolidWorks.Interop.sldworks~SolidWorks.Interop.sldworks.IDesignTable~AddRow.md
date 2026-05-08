# AddRow Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow`

Adds a row to the design table.
Adds a row to the design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddRow( _
   ByVal CellValues As System.Object _
) As System.Boolean
```

```

Dim instance As IDesignTable
Dim CellValues As System.Object
Dim value As System.Boolean
 
value = instance.AddRow(CellValues)
```

```

System.bool AddRow( 
   System.object CellValues
)
```

```

System.bool AddRow( 
   System.Object^ CellValues
) 
```

#### Parameters

*CellValues*
:   Array of the cell values

#### Return Value

True if the row was successfully added, false if not

Remarks

Do not use [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md) or [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md) with this method. Instead, use [IDesignTable::EditTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.md) and [IDesignTable::UpdateTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.md).

Example

[Add Row to Design Table (VBA)](Add_Row_to_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.md)  
[IDesignTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.md)  
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.md)  
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.md)  
[IDesignTable::SetRowChanged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetRowChanged.md)  
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.md)  
[IDesignTable::AutoAddNewConfigs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewConfigs.md)  
[IDesignTable::AutoAddNewParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewParams.md)

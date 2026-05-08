# GetTotalRowCount Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount`

Gets the number of rows in the design table.
Gets the number of rows in the design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTotalRowCount() As System.Integer
```

```

Dim instance As IDesignTable
Dim value As System.Integer
 
value = instance.GetTotalRowCount()
```

```

System.int GetTotalRowCount()
```

```

System.int GetTotalRowCount(); 
```

#### Return Value

Total number of rows in this design table

Remarks

The row index ranges from 1 to the return value.

Before you use any of the [IDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md) methods, use [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md) to activate the IDesignTable. After you finish getting IDesignTable data, use [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md) to deactivate the table.

This method differs from [IDesignTable::GetRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.md) in that it counts all the rows in the design table. IDesignTable::GetRowCount counts only the rows that are currently visible in the [IModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md).

To get information outside of the visible region of the design table, get the Microsoft Excel worksheet activated by IDesignTable::Attach. Then, you can use the Microsoft Excel API to make additional queries.

Example

[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)  
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)  
[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.md)  
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.md)  
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.md)  
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.md)  
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.md)  
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.md)

# GetRowCount Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount`

Gets the number of rows in the design table that are currently visible in the model view.
Gets the number of rows in the design table that are currently visible in the model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRowCount() As System.Integer
```

```

Dim instance As IDesignTable
Dim value As System.Integer
 
value = instance.GetRowCount()
```

```

System.int GetRowCount()
```

```

System.int GetRowCount(); 
```

#### Return Value

Number of rows currently visible in the model view

Remarks

Before you use any of the [IDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md) methods, you must first activate the IDesignTable using [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md). Once you are finished getting IDesignTable data, you can deactivate the table using [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md).

Use [IDesignTable::GetTotalRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.md) to get the total number of rows in the design table.

To get information outside the visible region of the IDesignTable, get the Microsoft Excel worksheet activated by IDesignTable::Attach. Then, you can use the Microsoft Excel API to make additional queries.

Example

[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)  
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)  
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.md)  
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.md)  
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.md)  
[IDesignTable::SetRowChanged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetRowChanged.md)  
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.md)  
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.md)

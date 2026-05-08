# GetColumnCount Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount`

Gets the number of columns in the design table that are currently visible in the model view.
Gets the number of columns in the design table that are currently visible in the model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnCount() As System.Integer
```

```

Dim instance As IDesignTable
Dim value As System.Integer
 
value = instance.GetColumnCount()
```

```

System.int GetColumnCount()
```

```

System.int GetColumnCount(); 
```

#### Return Value

Number of columns in the design table

Remarks

Before using any of the [IDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md) methods, you must use [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md) to activate the design table. After you finish getting design table data, use [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md) to deactivate the table.

Use [IDesignTable::GetTotalColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.md) to get the total number of columns in the design table.

To obtain information outside the visible region of the design table, get the Microsoft Excel worksheet that [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md) activated. You can then use the Microsoft Excel API to make additional queries.

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
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.md)  
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.md)  
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.md)  
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.md)  
[IDesignTable::GetHeaderText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetHeaderText.md)

# GetTotalColumnCount Method (IBomTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetTotalColumnCount`

Gets the total number of columns in the BOM table.
Gets the total number of columns in the BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTotalColumnCount() As System.Integer
```

```

Dim instance As IBomTable
Dim value As System.Integer
 
value = instance.GetTotalColumnCount()
```

```

System.int GetTotalColumnCount()
```

```

System.int GetTotalColumnCount(); 
```

#### Return Value

Total number of columns in the BOM table

Remarks

This method returns 0 if the BOM is obscured, which may occur when debugging a macro. This is a quirk in Microsoft Excel, which is used by SOLIDWORKS for the BOM functionality.

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3.md). After you finish getting BOM data, use [IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.md) to deactivate the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)  
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.md)  
[IBomTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetTotalRowCount.md)  
[IBomTable::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetColumnWidth.md)

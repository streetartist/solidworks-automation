# GetColumnWidth Method (IBomTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetColumnWidth`

Gets the specified column width in meters.
Gets the specified column width in meters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnWidth( _
   ByVal Col As System.Integer _
) As System.Double
```

```

Dim instance As IBomTable
Dim Col As System.Integer
Dim value As System.Double
 
value = instance.GetColumnWidth(Col)
```

```

System.double GetColumnWidth( 
   System.int Col
)
```

```

System.double GetColumnWidth( 
   System.int Col
) 
```

#### Parameters

*Col*
:   Column number; this is a 0-based index

#### Return Value

Width of the specified column in meters

Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3.md). After you finish getting BOM data, use [IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.md) to deactivate the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)  
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.md)  
[IBomTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetTotalColumnCount.md)

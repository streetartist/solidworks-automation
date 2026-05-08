# GetEntryText Method (IBomTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetEntryText`

Retrieves the contents of the specified cell as a string regardless of the cell's data type.
Retrieves the contents of the specified cell as a string regardless of the cell's data type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntryText( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer _
) As System.String
```

```

Dim instance As IBomTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim value As System.String
 
value = instance.GetEntryText(Row, Col)
```

```

System.string GetEntryText( 
   System.int Row,
   System.int Col
)
```

```

System.String^ GetEntryText( 
   System.int Row,
   System.int Col
) 
```

#### Parameters

*Row*
:   Row number of the desired cell; this is a 0-based index

*Col*
:   Column number of the desired cell; this is a 0-based index

#### Return Value

Text string from the specified cell

Remarks

Use [IBomTable::GetEntryValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetEntryValue.md) for typed return values.

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3.md). After you finish getting BOM data, use [IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.md) to deactivate the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)  
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.md)

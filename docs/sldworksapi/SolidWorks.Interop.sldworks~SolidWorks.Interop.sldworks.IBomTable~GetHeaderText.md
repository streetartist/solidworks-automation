# GetHeaderText Method (IBomTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetHeaderText`

Gets the header text for the specified column.
Gets the header text for the specified column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHeaderText( _
   ByVal Col As System.Integer _
) As System.String
```

```

Dim instance As IBomTable
Dim Col As System.Integer
Dim value As System.String
 
value = instance.GetHeaderText(Col)
```

```

System.string GetHeaderText( 
   System.int Col
)
```

```

System.String^ GetHeaderText( 
   System.int Col
) 
```

#### Parameters

*Col*
:   Column number with the desired header text; this is a 0-based index

#### Return Value

Text string from the column header

Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3.md). After you finish getting BOM data, use [IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.md) to deactivate the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)  
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.md)

# GetEntryValue Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue`

Gets the contents of the specified cell.
Gets the contents of the specified cell.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntryValue( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer _
) As System.Object
```

```

Dim instance As IDesignTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim value As System.Object
 
value = instance.GetEntryValue(Row, Col)
```

```

System.object GetEntryValue( 
   System.int Row,
   System.int Col
)
```

```

System.Object^ GetEntryValue( 
   System.int Row,
   System.int Col
) 
```

#### Parameters

*Row*
:   0-based row number of the cell

*Col*
:   0-based column number of the cell

#### Return Value

Object containing the information from the specified cell

Remarks

After you receive a valid return value from this method, you can evaluate the the data type of the object (for example, double, long, or string).

Use [IDesignTable::GetEntryText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.md) to return the cell contents as a string.

Before you use any of the design table methods, you must first activate the design table using [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md). After you are finished getting design table data, you can deactivate the table using [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::GetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.md)  
[IDesignTable::SetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.md)  
[IDesignTable::SetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.md)

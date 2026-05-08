# GetEntryText Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText`

Gets the contents of the specified cell as a string regardless of the cell's data type.
Gets the contents of the specified cell as a string regardless of the cell's data type.

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

Dim instance As IDesignTable
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
:   0-based row number of the cell

*Col*
:   0-based column number of the cell

#### Return Value

Text string in the specified cell

Remarks

For example, if the cell is of type double, it is returned as a string.

Use [IDesignTable::GetEntryValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.md) to get typed return values.

Before using any of the [IDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md) methods, use [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md) to activate the design table. After you are finish getting design table data, use [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md) to deactivate the table.

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
[IDesignTable::GetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.md)  
[IDesignTable::SetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.md)  
[IDesignTable::SetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.md)

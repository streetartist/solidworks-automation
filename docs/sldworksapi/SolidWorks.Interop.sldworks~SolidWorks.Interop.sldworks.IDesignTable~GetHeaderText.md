# GetHeaderText Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetHeaderText`

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

Dim instance As IDesignTable
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
:   0-based column number with the header text

#### Return Value

Text string from the column header

Remarks

Before you use any of the design table methods, you must first activate the design table using [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md). After you are finished getting design table data, you can deactivate the table using [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.md)  
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.md)  
[IDesignTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.md)  
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.md)  
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.md)  
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.md)

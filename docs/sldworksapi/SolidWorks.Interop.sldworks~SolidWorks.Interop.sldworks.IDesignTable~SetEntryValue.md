# SetEntryValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue`

Sets the data type and value in the specified cell.
Sets the data type and value in the specified cell.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEntryValue( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer, _
   ByVal IsText As System.Boolean, _
   ByVal Retval As System.String _
) 
```

```

Dim instance As IDesignTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim IsText As System.Boolean
Dim Retval As System.String
 
instance.SetEntryValue(Row, Col, IsText, Retval)
```

```

void SetEntryValue( 
   System.int Row,
   System.int Col,
   System.bool IsText,
   System.string Retval
)
```

```

void SetEntryValue( 
   System.int Row,
   System.int Col,
   System.bool IsText,
   System.String^ Retval
) 
```

#### Parameters

*Row*
:   Row number

*Col*
:   Column number

*IsText*
:   True for text, false for general

*Retval*
:   Value of the specific cell

Remarks

This method lets you change the data type from text to general and from general to text and specify a value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::GetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.md)  
[IDesignTable::GetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.md)  
[IDesignTable::SetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.md)

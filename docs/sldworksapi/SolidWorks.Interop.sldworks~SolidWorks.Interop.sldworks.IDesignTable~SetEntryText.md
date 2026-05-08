# SetEntryText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText`

Sets the text value of the specified entry.
Sets the text value of the specified entry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEntryText( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer, _
   ByVal TextIn As System.String _
) 
```

```

Dim instance As IDesignTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim TextIn As System.String
 
instance.SetEntryText(Row, Col, TextIn)
```

```

void SetEntryText( 
   System.int Row,
   System.int Col,
   System.string TextIn
)
```

```

void SetEntryText( 
   System.int Row,
   System.int Col,
   System.String^ TextIn
) 
```

#### Parameters

*Row*
:   Row number

*Col*
:   Column number

*TextIn*
:   Text value for entry

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::SetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.md)  
[IDesignTable::GetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.md)  
[IDesignTable::GetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.md)

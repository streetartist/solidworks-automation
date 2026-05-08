# GetCellUseDocTextFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat`

Gets whether this cell uses the document setting for its text format.
Gets whether this cell uses the document setting for its text format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCellUseDocTextFormat( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.Boolean
 
value = instance.GetCellUseDocTextFormat(Row, Column)
```

```

System.bool GetCellUseDocTextFormat( 
   System.int Row,
   System.int Column
)
```

```

System.bool GetCellUseDocTextFormat( 
   System.int Row,
   System.int Column
) 
```

#### Parameters

*Row*
:   Index of the row in which the cell resides

*Column*
:   Index of the column in which the cell resides

#### Return Value

True to use the document setting for its text format, false to not

Remarks

The index for both the rows and columns in this table are 0-based.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.md)  
[ITableAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetTextFormat.md)  
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.md)  
[ITableAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetTextFormat.md)  
[ITableAnnotation::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text.md)

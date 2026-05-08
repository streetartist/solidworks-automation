# GetCellRange Method (ISelectData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~GetCellRange`

Gets the specified range of table cells for this selection.
Gets the specified range of table cells for this selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetCellRange( _
   ByRef FirstRow As System.Integer, _
   ByRef LastRow As System.Integer, _
   ByRef FirstColumn As System.Integer, _
   ByRef LastColumn As System.Integer _
) 
```

```

Dim instance As ISelectData
Dim FirstRow As System.Integer
Dim LastRow As System.Integer
Dim FirstColumn As System.Integer
Dim LastColumn As System.Integer
 
instance.GetCellRange(FirstRow, LastRow, FirstColumn, LastColumn)
```

```

void GetCellRange( 
   out System.int FirstRow,
   out System.int LastRow,
   out System.int FirstColumn,
   out System.int LastColumn
)
```

```

void GetCellRange( 
   [Out] System.int FirstRow,
   [Out] System.int LastRow,
   [Out] System.int FirstColumn,
   [Out] System.int LastColumn
) 
```

#### Parameters

*FirstRow*
:   0-based row number at the beginning of the selection range

*LastRow*
:   0-based row number at the end of the selection range

*FirstColumn*
:   0-based column number at the beginning of the selection range

*LastColumn*
:   0-based column number at the end of the selection range

#### Return Value

Remarks

The range of table cells are only used for a selection made in a table. For all other types of selections, these values are ignored.

By default, the value for FirstRow, LastRow, FirstColumn, and LastColumn is -1, which indicates that the entire table is selected.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)  
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.md)  
[ISelectData::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~SetCellRange.md)

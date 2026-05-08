# SetCellTextOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextOrientation`

Sets the text orientation in the specified table cell.
Sets the text orientation in the specified table cell.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCellTextOrientation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal AllCells As System.Boolean, _
   ByVal Orientation As System.Integer _
) 
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim AllCells As System.Boolean
Dim Orientation As System.Integer
 
instance.SetCellTextOrientation(Row, Column, IncludeHidden, AllCells, Orientation)
```

```

void SetCellTextOrientation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells,
   System.int Orientation
)
```

```

void SetCellTextOrientation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells,
   System.int Orientation
) 
```

#### Parameters

*Row*
:   0-based index of row; valid only if AllCells is set to false

*Column*
:   0-based index of column; valid only if AllCells is set to false

*IncludeHidden*
:   True to include hidden rows and columns in the Row and Column indexes, false to not

*AllCells*
:   True for all cells, false if not; if false, set Row and Column

*Orientation*
:   Text orientation as defined in [swTableCellOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableCellOrientation_e.html) (see **Remarks**)

Remarks

You can set Orientation to any member of swTableCellOrientation\_e except swTableCellOrientation\_Varies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellTextOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextOrientation.md)

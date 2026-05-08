# GetCellTextOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextOrientation`

Gets the text orientation in the specified cell of this table.
Gets the text orientation in the specified cell of this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCellTextOrientation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal AllCells As System.Boolean _
) As System.Integer
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim AllCells As System.Boolean
Dim value As System.Integer
 
value = instance.GetCellTextOrientation(Row, Column, IncludeHidden, AllCells)
```

```

System.int GetCellTextOrientation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells
)
```

```

System.int GetCellTextOrientation( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells
) 
```

#### Parameters

*Row*
:   0-based index of the cell row; valid only if AllCells is set to false

*Column*
:   0-based index of the cell column; valid only if AllCells is set to false

*IncludeHidden*
:   True to include hidden rows and columns in Row and Column indexes, false to not

*AllCells*
:   True to get the orientation in all cells, false to not; if false, set Row and Column (see **Remarks**)

#### Return Value

Text orientation as defined in [swTableCellOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableCellOrientation_e.html) (see **Remarks**)

Remarks

If AllCells is set to false, this method returns one of swTableCellOrientation\_e.:

- swTableCellOrientation\_Right
- swTableCellOrientation\_Left
- swTableCellOrientation\_Up
- swTableCellOrientation\_Down

If AllCells is set to true, this method returns one of the above or:

- swTableCellOrientation\_Varies, if all the cells do not share the same text orientation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::SetCellTextOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextOrientation.md)

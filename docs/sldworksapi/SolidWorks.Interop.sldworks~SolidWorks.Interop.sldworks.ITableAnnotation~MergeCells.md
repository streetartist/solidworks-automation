# MergeCells Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells`

Merges the cells in the specified range.
Merges the cells in the specified range.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MergeCells( _
   ByVal RowStart As System.Integer, _
   ByVal ColumnStart As System.Integer, _
   ByVal RowEnd As System.Integer, _
   ByVal ColumnEnd As System.Integer _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim RowStart As System.Integer
Dim ColumnStart As System.Integer
Dim RowEnd As System.Integer
Dim ColumnEnd As System.Integer
Dim value As System.Boolean
 
value = instance.MergeCells(RowStart, ColumnStart, RowEnd, ColumnEnd)
```

```

System.bool MergeCells( 
   System.int RowStart,
   System.int ColumnStart,
   System.int RowEnd,
   System.int ColumnEnd
)
```

```

System.bool MergeCells( 
   System.int RowStart,
   System.int ColumnStart,
   System.int RowEnd,
   System.int ColumnEnd
) 
```

#### Parameters

*RowStart*
:   Index of row at which start the merge

*ColumnStart*
:   Index of column at which to start the merge

*RowEnd*
:   Index of row at which to end the merge

*ColumnEnd*
:   Index of column at which to end the merge

#### Return Value

True if the cells in the specified range merge successfully, false if not

Remarks

The index for both rows and columns is 0-based.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.md)  
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.md)  
[ITableAnnotation::Merge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge.md)  
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.md)  
[ITableAnnotation::GetSplitInformation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.md)  
[ITableAnnotation::Split Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.md)

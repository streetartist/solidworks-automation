# DeleteColumn2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn2`

Deletes the specified column in this table.
Deletes the specified column in this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteColumn2( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.Boolean
 
value = instance.DeleteColumn2(Index, IncludeHidden)
```

```

System.bool DeleteColumn2( 
   System.int Index,
   System.bool IncludeHidden
)
```

```

System.bool DeleteColumn2( 
   System.int Index,
   System.bool IncludeHidden
) 
```

#### Parameters

*Index*
:   Index of the column you want to delete

*IncludeHidden*
:   True to delete the hidden column, false to not

#### Return Value

True if column is deleted successfully, false if not

Remarks

The index for both the rows and columns is 0-based.

This method deletes the entire table if you try to delete the only column in the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::InsertColumn2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn2.md)  
[ITableAnnotation::ColumnCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.md)  
[ITableAnnotation::ColumnHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.md)  
[ITableAnnotation::TotalColumnCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.md)

# GetLockRowHeight Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight`

Gets whether the height of the specified row is locked in this table annotation.
Gets whether the height of the specified row is locked in this table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLockRowHeight( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.GetLockRowHeight(Index)
```

```

System.bool GetLockRowHeight( 
   System.int Index
)
```

```

System.bool GetLockRowHeight( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index of the row (see **Remarks**)

#### Return Value

True if the specified row's height is locked, false if not

Remarks

Call [ITableAnnotation::RowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.md) to get the number of visible rows or [ITableAnnotation::TotalRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.md) to get the number of visible and hidden rows in this table annotation.

Example

[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)  
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)  
[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::SetLockRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.md)  
[ITableAnnotation::DeleteRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.md)  
[ITableAnnotation::GetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.md)  
[ITableAnnotation::GetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.md)  
[ITableAnnotation::InsertRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.md)  
[ITableAnnotation::MoveRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.md)  
[ITableAnnotation::SetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.md)  
[ITableAnnotation::SetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.md)  
[ITableAnnotation::RowHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.md)

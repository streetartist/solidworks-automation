# GetCellRange Method (ITableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange`

Gets the selected table cells' row and column index ranges.
Gets the selected table cells' row and column index ranges.

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

Dim instance As ITableAnnotation
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
:   Index of row of first selected cell

*LastRow*
:   Index of row of last selected cell

*FirstColumn*
:   Index of column of first selected cell

*LastColumn*
:   Index of column of last selected cell

Remarks

The returned indexes are all 0-based.

If you don't multi-select table cells before you call this method, then the cell row/column index range for the entire table is returned.

Before calling this method, you can select the table cells in the graphics area whose row/column index range you want to get. How you make these selections determines what this method returns.

|  |  |  |
| --- | --- | --- |
| **Selection** | **Steps** | **Cell range returned** |
| Table cell | 1. Place the cursor on the desired table cell. 2. Click the left-mouse button. | Selected cell |
|  | 1. Hold down the Ctrl key and place the cursor on the desired table cell. 2. Click the left-mouse button. | Selected cell |
| Multiple table cells | 1. Place the cursor on a desired table cell. 2. Click and hold down the left-mouse button. 3. Drag the cursor over the other desired table cells. 4. Release the left-mouse button when the cursor is on the last table cell that you want selected. | All selected cells |
|  | 1. Hold down the Ctrl key and place the cursor on a desired table cell. 2. Click the left-mouse button. 3. Repeat steps 1 and 2 until all desired table cells are selected. | Each selected cell |
| Table column | Place the cursor just above the desired column and click the left-mouse button when the cursor changes to a solid arrow | All selected cells |
| Table row | Place the cursor to just left of the desired row and click the left-mouse button when the cursor changes to a solid arrow | All selected cells |

Run any of the examples in the **Example** section to better understand the values returned by this method.

Example

[Select Table Cells (C#)](Select_Table_Cells_Example_CSharp.htm)  
[Select Table Cells (VB.NET)](Select_Table_Cells_Example_VBNET.htm)  
[Select Table Cells (VBA)](Select_Table_Cells_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.md)  
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.md)  
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.md)  
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.md)  
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.md)  
[ITableAnnotation::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.md)  
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.md)  
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.md)  
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.md)  
[ITableAnnotation::DisplayedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText.md)

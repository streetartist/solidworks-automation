# GetCellText Method (ISwDMTable)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.html) on this topic. |
| GetCellText Method (ISwDMTable) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md) : GetCellText Method (ISwDMTable) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*RowIndex*
:   Index of row where cell is located

*ColumnIndex*
:   Index of column where cell is located

*CellTextOut*
:   String containing the text in cell

Gets the text in the specified cell.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCellText( _    ByVal RowIndex As System.Integer, _    ByVal ColumnIndex As System.Integer, _    ByRef CellTextOut As System.String _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable Dim RowIndex As System.Integer Dim ColumnIndex As System.Integer Dim CellTextOut As System.String Dim value As SwDmTableError   value = instance.GetCellText(RowIndex, ColumnIndex, CellTextOut) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError GetCellText(     System.int RowIndex,    System.int ColumnIndex,    out System.string CellTextOut ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError GetCellText(  &   System.int RowIndex, &   System.int ColumnIndex, &   [Out] System.String^ CellTextOut ) ``` | |

#### Parameters

*RowIndex*
:   Index of row where cell is located

*ColumnIndex*
:   Index of column where cell is located

*CellTextOut*
:   String containing the text in cell

#### Return Value

Error as defined by [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable::GetCellText](swdocumentmgr~SwDMTable~GetCellText.md).

# Remarks

Before calling this method, call:

- [ISwDMTable::GetRowCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.md) to determine the index of the row where the cell is located.
- [ISwDMTable::GetColumnCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.md) to determine the index of the column where the cell is located.

# See Also

#### 

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.md)
  
[ISwDMTable::SetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~SetCellText.md)
  
[ISwDMTable2::GetCellTextHorizontalJustification Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetCellTextHorizontalJustification.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

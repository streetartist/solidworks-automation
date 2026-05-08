# SetCellText Method (ISwDMTable)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~SetCellText`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~SetCellText.html) on this topic. |
| SetCellText Method (ISwDMTable) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md) : SetCellText Method (ISwDMTable) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*RowIndex*
:   Index of row where cell is located

*ColumnIndex*
:   Index of column where cell is located

*CellTextIn*
:   Text for cell

Sets the specified text in the specified cell.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function SetCellText( _    ByVal RowIndex As System.Integer, _    ByVal ColumnIndex As System.Integer, _    ByVal CellTextIn As System.String _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable Dim RowIndex As System.Integer Dim ColumnIndex As System.Integer Dim CellTextIn As System.String Dim value As SwDmTableError   value = instance.SetCellText(RowIndex, ColumnIndex, CellTextIn) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError SetCellText(     System.int RowIndex,    System.int ColumnIndex,    System.string CellTextIn ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError SetCellText(  &   System.int RowIndex, &   System.int ColumnIndex, &   System.String^ CellTextIn ) ``` | |

#### Parameters

*RowIndex*
:   Index of row where cell is located

*ColumnIndex*
:   Index of column where cell is located

*CellTextIn*
:   Text for cell

#### Return Value

Error as defined by [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable::SetCellText](swdocumentmgr~SwDMTable~SetCellText.md).

# Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call:

- [ISwDMTable::GetRowCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.md) to determine the index of the row where the cell is located.
- [ISwDMTable::GetColumnCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.md) to determine the index of the column where the cell is located.

# See Also

#### 

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.md)
  
[ISwDMTable::GetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.md)
  
[ISwDMTable2;:GetCellTextHorizontalJustification Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetCellTextHorizontalJustification.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

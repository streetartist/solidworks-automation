# GetCellTextHorizontalJustification Method (ISwDMTable2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetCellTextHorizontalJustification`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetCellTextHorizontalJustification.html) on this topic. |
| GetCellTextHorizontalJustification Method (ISwDMTable2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.md) : GetCellTextHorizontalJustification Method (ISwDMTable2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*RowIndex*
:   Index of row where the cell is located

*ColumnIndex*
:   Index of the column where the cell is located

*Error*
:   Error as defined by [swDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

Gets the type of text horizontal alignment for the specified cell in this table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCellTextHorizontalJustification( _    ByVal RowIndex As System.Integer, _    ByVal ColumnIndex As System.Integer, _    ByRef Error As SwDmTableError _ ) As swDmTableCellHorzAlignType ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable2 Dim RowIndex As System.Integer Dim ColumnIndex As System.Integer Dim Error As SwDmTableError Dim value As swDmTableCellHorzAlignType   value = instance.GetCellTextHorizontalJustification(RowIndex, ColumnIndex, Error) ``` | |

| C# |  |
| --- | --- |
| ``` swDmTableCellHorzAlignType GetCellTextHorizontalJustification(     System.int RowIndex,    System.int ColumnIndex,    out SwDmTableError Error ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` swDmTableCellHorzAlignType GetCellTextHorizontalJustification(  &   System.int RowIndex, &   System.int ColumnIndex, &   [Out] SwDmTableError Error ) ``` | |

#### Parameters

*RowIndex*
:   Index of row where the cell is located

*ColumnIndex*
:   Index of the column where the cell is located

*Error*
:   Error as defined by [swDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

#### Return Value

Type of horizontal alignment for this cell as defined by [swDmTableCellHorzAlignType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmTableCellHorzAlignType.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable2::GetCellTextHorizontalJustification](swdocumentmgr~SwDMTable2~GetCellTextHorizontalJustification.md).

# Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call:

- [ISwDMTable::GetRowCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.md) to determine the index of the row where the cell is located.
- [ISwDMTable::GetColumnCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.md) to determine the index of the column where the cell is located.

# See Also

#### 

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.md)
  
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.md)
  
[ISwDMTable::GetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.md)
  
[ISwDMTable::SetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~SetCellText.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

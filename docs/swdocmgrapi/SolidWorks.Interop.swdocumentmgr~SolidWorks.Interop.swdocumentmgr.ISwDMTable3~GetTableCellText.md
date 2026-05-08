# GetTableCellText Method (ISwDMTable3)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3~GetTableCellText`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3~GetTableCellText.html) on this topic. |
| GetTableCellText Method (ISwDMTable3) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3.md) : GetTableCellText Method (ISwDMTable3) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Error*
:   Error as defined by [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

*RowCount*
:   Number of rows in the table

*ColCount*
:   Number of columns in the table

Gets all of the cell text and the number of rows and columns in this table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetTableCellText( _    ByRef Error As SwDmTableError, _    ByRef RowCount As System.Integer, _    ByRef ColCount As System.Integer _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable3 Dim Error As SwDmTableError Dim RowCount As System.Integer Dim ColCount As System.Integer Dim value As System.Object   value = instance.GetTableCellText(Error, RowCount, ColCount) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetTableCellText(     out SwDmTableError Error,    out System.int RowCount,    out System.int ColCount ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetTableCellText(  &   [Out] SwDmTableError Error, &   [Out] System.int RowCount, &   [Out] System.int ColCount ) ``` | |

#### Parameters

*Error*
:   Error as defined by [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

*RowCount*
:   Number of rows in the table

*ColCount*
:   Number of columns in the table

#### Return Value

A 1-dimensional array of strings containing all of the cell text in the table

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable3::GetTableCellText](swdocumentmgr~SwDMTable3~GetTableCellText.md).

# Example

[Get Table Cell Text (C#)](Get_Table_Cell_Text_Example_CSharp.htm)
  
[Get Table Cell Text (VB.NET)](Get_Table_Cell_Text_Example_VBNET.htm)

# Remarks

The returned array is indexed by row count.

# See Also

#### 

[ISwDMTable3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3.md)
  
[ISwDMTable3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3_members.md)
  
[ISwDMTable::GetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.md)

# Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4

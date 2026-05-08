# AddRowHead Method (ISwDMTable)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowHead`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowHead.html) on this topic. |
| AddRowHead Method (ISwDMTable) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md) : AddRowHead Method (ISwDMTable) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*RowDataIn*
:   Array of data for the row

Adds a row to the top of the table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function AddRowHead( _    ByRef RowDataIn As System.Object _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable Dim RowDataIn As System.Object Dim value As SwDmTableError   value = instance.AddRowHead(RowDataIn) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError AddRowHead(     ref System.object RowDataIn ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError AddRowHead(  &   System.Object^% RowDataIn ) ``` | |

#### Parameters

*RowDataIn*
:   Array of data for the row

#### Return Value

Error as defined by [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable::AddRowHead](swdocumentmgr~SwDMTable~AddRowHead.md).

 

# See Also

#### 

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.md)
  
[ISwDMTable::AddRowTail Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowTail.md)
  
[ISwDMTable::DeleteRow Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteRow.md)
  
[ISwDMTable::GetRowCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

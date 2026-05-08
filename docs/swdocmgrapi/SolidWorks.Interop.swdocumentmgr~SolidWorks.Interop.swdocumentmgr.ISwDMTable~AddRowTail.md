# AddRowTail Method (ISwDMTable)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowTail`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowTail.html) on this topic. |
| AddRowTail Method (ISwDMTable) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md) : AddRowTail Method (ISwDMTable) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*RowDataIn*
:   Array of data for the row

Adds a row to the end of the table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function AddRowTail( _    ByRef RowDataIn As System.Object _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable Dim RowDataIn As System.Object Dim value As SwDmTableError   value = instance.AddRowTail(RowDataIn) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError AddRowTail(     ref System.object RowDataIn ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError AddRowTail(  &   System.Object^% RowDataIn ) ``` | |

#### Parameters

*RowDataIn*
:   Array of data for the row

#### Return Value

Error as defined by [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable::AddRowTail](swdocumentmgr~SwDMTable~AddRowTail.md).

 

# See Also

#### 

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.md)
  
[ISwDMTable::AddRowHead Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowHead.md)
  
[ISwDMTable::DeleteRow Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteRow.md)
  
[ISwDMTable::GetRowCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

# UpdateRevisionRow Method (ISwDMTable6)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~UpdateRevisionRow`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~UpdateRevisionRow.html) on this topic. |
| UpdateRevisionRow Method (ISwDMTable6) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.md) : UpdateRevisionRow Method (ISwDMTable6) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Revision*
:   Revision; if empty, the latest revision row is updated

*RowDataIn*
:   Row data

Updates the specified revision row in this table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function UpdateRevisionRow( _    ByVal Revision As System.String, _    ByRef RowDataIn As System.Object _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable6 Dim Revision As System.String Dim RowDataIn As System.Object Dim value As SwDmTableError   value = instance.UpdateRevisionRow(Revision, RowDataIn) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError UpdateRevisionRow(     System.string Revision,    ref System.object RowDataIn ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError UpdateRevisionRow(  &   System.String^ Revision, &   System.Object^% RowDataIn ) ``` | |

#### Parameters

*Revision*
:   Revision; if empty, the latest revision row is updated

*RowDataIn*
:   Row data

#### Return Value

Return code as defined in [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable6::UpdateRevisionRow](swdocumentmgr~SwDMTable6~UpdateRevisionRow.md).

 

# See Also

#### 

[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.md)
  
[ISwDMTable6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6_members.md)

# Availability

SOLIDWORKS Document Manager API 2018 SP0

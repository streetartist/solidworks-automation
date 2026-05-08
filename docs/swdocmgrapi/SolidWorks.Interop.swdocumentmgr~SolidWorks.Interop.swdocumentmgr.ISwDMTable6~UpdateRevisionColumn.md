# UpdateRevisionColumn Method (ISwDMTable6)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~UpdateRevisionColumn`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~UpdateRevisionColumn.html) on this topic. |
| UpdateRevisionColumn Method (ISwDMTable6) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.md) : UpdateRevisionColumn Method (ISwDMTable6) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Revision*
:   Revision; if empty, the column in the latest revision row is updated

*ColType*
:   Type of column as defined in [SwDmColumnType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmColumnType.md)

*Data*
:   Column data

Updates the specified revision column in this table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function UpdateRevisionColumn( _    ByVal Revision As System.String, _    ByVal ColType As SwDmColumnType, _    ByVal Data As System.String _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable6 Dim Revision As System.String Dim ColType As SwDmColumnType Dim Data As System.String Dim value As SwDmTableError   value = instance.UpdateRevisionColumn(Revision, ColType, Data) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError UpdateRevisionColumn(     System.string Revision,    SwDmColumnType ColType,    System.string Data ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError UpdateRevisionColumn(  &   System.String^ Revision, &   SwDmColumnType ColType, &   System.String^ Data ) ``` | |

#### Parameters

*Revision*
:   Revision; if empty, the column in the latest revision row is updated

*ColType*
:   Type of column as defined in [SwDmColumnType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmColumnType.md)

*Data*
:   Column data

#### Return Value

Return code as defined in [swDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable6::UpdateRevisionColumn](swdocumentmgr~SwDMTable6~UpdateRevisionColumn.md).

 

# See Also

#### 

[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.md)
  
[ISwDMTable6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6_members.md)

# Availability

SOLIDWORKS Document Manager API 2018 SP0

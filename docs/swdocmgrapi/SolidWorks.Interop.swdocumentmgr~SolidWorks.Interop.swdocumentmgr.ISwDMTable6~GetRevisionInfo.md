# GetRevisionInfo Method (ISwDMTable6)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~GetRevisionInfo`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~GetRevisionInfo.html) on this topic. |
| GetRevisionInfo Method (ISwDMTable6) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.md) : GetRevisionInfo Method (ISwDMTable6) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Revision*
:   Revision for which to get data

*RowData*
:   Array of revision information

Gets information for the specified revision.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetRevisionInfo( _    ByVal Revision As System.String, _    ByRef RowData As System.Object _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable6 Dim Revision As System.String Dim RowData As System.Object Dim value As SwDmTableError   value = instance.GetRevisionInfo(Revision, RowData) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError GetRevisionInfo(     System.string Revision,    out System.object RowData ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError GetRevisionInfo(  &   System.String^ Revision, &   [Out] System.Object^ RowData ) ``` | |

#### Parameters

*Revision*
:   Revision for which to get data

*RowData*
:   Array of revision information

#### Return Value

Return code as defined in [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable6::GetRevisionInfo](swdocumentmgr~SwDMTable6~GetRevisionInfo.md).

 

# See Also

#### 

[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.md)
  
[ISwDMTable6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6_members.md)

# Availability

SOLIDWORKS Document Manager API 2018 SP0

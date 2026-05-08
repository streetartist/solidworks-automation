# GetReferencesInformation Method (ISwDMConfiguration6)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6~GetReferencesInformation`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6~GetReferencesInformation.html) on this topic. |
| GetReferencesInformation Method (ISwDMConfiguration6) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6.md) : GetReferencesInformation Method (ISwDMConfiguration6) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*references*
:   Array of paths and names of the reference documents

*configurations*
:   Array of configuration names of the reference documents

*sstates*
:   Array of Booleans indicating if the reference document is suppressed (true) or not (false)

Obsolete. Superseded by [ISwDMConfiguration8::GetReferencesInformation2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8~GetReferencesInformation2.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub GetReferencesInformation( _    ByRef references As System.Object, _    ByRef configurations As System.Object, _    ByRef sstates As System.Object _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration6 Dim references As System.Object Dim configurations As System.Object Dim sstates As System.Object   instance.GetReferencesInformation(references, configurations, sstates) ``` | |

| C# |  |
| --- | --- |
| ``` void GetReferencesInformation(     out System.object references,    out System.object configurations,    out System.object sstates ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void GetReferencesInformation(  &   [Out] System.Object^ references, &   [Out] System.Object^ configurations, &   [Out] System.Object^ sstates ) ``` | |

#### Parameters

*references*
:   Array of paths and names of the reference documents

*configurations*
:   Array of configuration names of the reference documents

*sstates*
:   Array of Booleans indicating if the reference document is suppressed (true) or not (false)

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration6::GetReferencesInformation](swdocumentmgr~SwDMConfiguration6~GetReferencesInformation.md).

# Remarks

This method only works with references modified using SOLIDWORKS Document Manager API 2007 and later and SOLIDWORKS Explorer.

# See Also

#### 

[ISwDMConfiguration6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6.md)
  
[ISwDMConfiguration6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6_members.md)

# Availability

SOLIDWORKS Document Manager API 2007 FCS

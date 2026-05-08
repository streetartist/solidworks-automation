# GetReferencesInformation2 Method (ISwDMConfiguration8)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8~GetReferencesInformation2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8~GetReferencesInformation2.html) on this topic. |
| GetReferencesInformation2 Method (ISwDMConfiguration8) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8.md) : GetReferencesInformation2 Method (ISwDMConfiguration8) |

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

*IsVirtual*
:   Array of Booleans indicating whether each configuration reference is a virtual component

Gets the names of any reference documents, the configuration names of the references, and their suppression states.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub GetReferencesInformation2( _    ByRef references As System.Object, _    ByRef configurations As System.Object, _    ByRef sstates As System.Object, _    ByRef IsVirtual As System.Object _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration8 Dim references As System.Object Dim configurations As System.Object Dim sstates As System.Object Dim IsVirtual As System.Object   instance.GetReferencesInformation2(references, configurations, sstates, IsVirtual) ``` | |

| C# |  |
| --- | --- |
| ``` void GetReferencesInformation2(     out System.object references,    out System.object configurations,    out System.object sstates,    out System.object IsVirtual ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void GetReferencesInformation2(  &   [Out] System.Object^ references, &   [Out] System.Object^ configurations, &   [Out] System.Object^ sstates, &   [Out] System.Object^ IsVirtual ) ``` | |

#### Parameters

*references*
:   Array of paths and names of the reference documents

*configurations*
:   Array of configuration names of the reference documents

*sstates*
:   Array of Booleans indicating if the reference document is suppressed (true) or not (false)

*IsVirtual*
:   Array of Booleans indicating whether each configuration reference is a virtual component

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration8::GetReferencesInformation2](swdocumentmgr~SwDMConfiguration8~GetReferencesInformation2.md).

# Remarks

This method only works with references modified using SOLIDWORKS Document Manager API 2007 and later and SOLIDWORKS Explorer.

# See Also

#### 

[ISwDMConfiguration8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8.md)
  
[ISwDMConfiguration8 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8_members.md)

# Availability

SOLIDWORKS Document Manager API 2008 SP1

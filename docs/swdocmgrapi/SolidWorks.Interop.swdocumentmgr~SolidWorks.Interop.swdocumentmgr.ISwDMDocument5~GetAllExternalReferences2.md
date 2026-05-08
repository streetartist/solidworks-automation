# GetAllExternalReferences2 Method (ISwDMDocument5)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2.html) on this topic. |
| GetAllExternalReferences2 Method (ISwDMDocument5) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5.md) : GetAllExternalReferences2 Method (ISwDMDocument5) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*pSrcOption*
:   Pointer to the [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

*brokenRefVar*
:   Array of the statuses of the any broken external references as defined in [swDmReferenceStatus](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmReferenceStatus.md) (see Remarks)

Obsolete. Superseded by [ISwDMDocument12::GetAllExternalReferences3](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument12~GetAllExternalReferences3.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetAllExternalReferences2( _    ByVal pSrcOption As SwDMSearchOption, _    ByRef brokenRefVar As System.Object _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument5 Dim pSrcOption As SwDMSearchOption Dim brokenRefVar As System.Object Dim value As System.Object   value = instance.GetAllExternalReferences2(pSrcOption, brokenRefVar) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetAllExternalReferences2(     SwDMSearchOption pSrcOption,    out System.object brokenRefVar ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetAllExternalReferences2(  &   SwDMSearchOption^ pSrcOption, &   [Out] System.Object^ brokenRefVar ) ``` | |

#### Parameters

*pSrcOption*
:   Pointer to the [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

*brokenRefVar*
:   Array of the statuses of the any broken external references as defined in [swDmReferenceStatus](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmReferenceStatus.md) (see Remarks)

#### Return Value

Array of the names of the external references used in this document

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument5::GetAllExternalReferences2](swdocumentmgr~SwDMDocument5~GetAllExternalReferences2.md).

# Remarks

Although this method returns valid data for files created in SOLIDWORKS 2005 and earlier, this method only returns valid data for the brokenRefVar argument for files created in SOLIDWORKS 2005 files and later. For files created in versions of SOLIDWORKS earlier than SOLIDWORKS 2005, it returns swDmReferenceStatusUnknown for brokenRefVar.

Call this method before calling [ISwDMDocument::ReplaceReference](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.md).

The SOLIDWORKS Document Manager API applies the same rules when searching for a reference as described in the SOLIDWORKS Help topic "Search Routine for Referenced Documents". The mix-and-match of sub-folder combinations is applied to the current document, which for the SOLIDWORKS Document Manager is the document attached using [ISwDMApplication::GetDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md) and the reference being searched for. You can set up the list of folders to be searched using [ISwDMSearchOption::AddSearchPath](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.md), which is equivalent to using the SOLIDWORKS user-interface commands Tools, Options, System Options, File Locations, Referenced Documents.

Two differences between SOLIDWORKS and the SOLIDWORKS Document Manager API searches are:

- the path of the last opened visible top-level document (drawing or assembly) is not tried directly.
- the last user path is not tried directly.

as these concepts have little meaning when SOLIDWORKS is not running.

Because the search routine is shared between SOLIDWORKS and the SOLIDWORKS Document Manager API, most of the same changes apply going from SOLIDWORKS 2006 to SOLIDWORKS 2007 and later. However, one significant change related to caching of resolved paths for references being searched for in SOLIDWORKS does not apply to the SOLIDWORKS Document Manager API. In SOLIDWORKS 2007 and later, the next time these references are needed, a simple lookup suffices instead of a potentially lengthy search. However, because this caching mechanism was not applied to the SOLIDWORKS Document Manager API, the SOLIDWORKS Document Manager API in 2006 and 2007, and later, exhibit similar behavior.

# See Also

#### 

[ISwDMDocument5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5.md)
  
[ISwDMDocument5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5_members.md)
  
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.md)

# Availability

SOLIDWORKS Document Manager API 2005 FCS

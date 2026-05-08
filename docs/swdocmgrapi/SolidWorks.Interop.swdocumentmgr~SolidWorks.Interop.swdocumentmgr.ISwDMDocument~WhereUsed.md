# WhereUsed Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~WhereUsed`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~WhereUsed.html) on this topic. |
| WhereUsed Method (ISwDMDocument) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : WhereUsed Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*pSrcOption*
:   [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)

Gets the names of the files that reference this document using the specified search options.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function WhereUsed( _    ByVal pSrcOption As SwDMSearchOption _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim pSrcOption As SwDMSearchOption Dim value As System.Object   value = instance.WhereUsed(pSrcOption) ``` | |

| C# |  |
| --- | --- |
| ``` System.object WhereUsed(     SwDMSearchOption pSrcOption ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ WhereUsed(  &   SwDMSearchOption^ pSrcOption ) ``` | |

#### Parameters

*pSrcOption*
:   [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)

#### Return Value

Array of the names of the files that reference this document

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::WhereUsed](swdocumentmgr~SwDMDocument~WhereUsed.md).

 

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)
  
[ISwDMDocument::ReplaceReference Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.md)
  
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.md)
  
[ISwDMDocument5::GetAllExternalReferences2 Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS

# GetDocument2 Method (ISwDMComponent4)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4~GetDocument2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4~GetDocument2.html) on this topic. |
| GetDocument2 Method (ISwDMComponent4) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4.md) : GetDocument2 Method (ISwDMComponent4) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*allowReadOnly*
:   True to open the document as read-only, false as read-write

*pSrcOption*
:   [Search options](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)

*result*
:   Error as defined by [ISwDMDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

Gets this component's document using the specified search options.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetDocument2( _    ByVal allowReadOnly As System.Boolean, _    ByVal pSrcOption As SwDMSearchOption, _    ByRef result As SwDmDocumentOpenError _ ) As SwDMDocument ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent4 Dim allowReadOnly As System.Boolean Dim pSrcOption As SwDMSearchOption Dim result As SwDmDocumentOpenError Dim value As SwDMDocument   value = instance.GetDocument2(allowReadOnly, pSrcOption, result) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDocument GetDocument2(     System.bool allowReadOnly,    SwDMSearchOption pSrcOption,    out SwDmDocumentOpenError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDocument^ GetDocument2(  &   System.bool allowReadOnly, &   SwDMSearchOption^ pSrcOption, &   [Out] SwDmDocumentOpenError result ) ``` | |

#### Parameters

*allowReadOnly*
:   True to open the document as read-only, false as read-write

*pSrcOption*
:   [Search options](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)

*result*
:   Error as defined by [ISwDMDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

#### Return Value

[ISwDMDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent4::GetDocument2](swdocumentmgr~SwDMComponent4~GetDocument2.md).

 

# See Also

#### 

[ISwDMComponent4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4.md)
  
[ISwDMComponent4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4_members.md)

# Availability

SOLIDWORKS Document Manager API 2008 SP1

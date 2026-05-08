# GetDocument Method (ISwDMComponent3)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3~GetDocument`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3~GetDocument.html) on this topic. |
| GetDocument Method (ISwDMComponent3) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3.md) : GetDocument Method (ISwDMComponent3) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*allowReadOnly*
:   True to open the document as read-only, false as read-write

*result*
:   Error as defined by [SwDmDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

Obsolete. Superseded by [ISwDMComponent4::GetDocument2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4~GetDocument2.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetDocument( _    ByVal allowReadOnly As System.Boolean, _    ByRef result As SwDmDocumentOpenError _ ) As SwDMDocument ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent3 Dim allowReadOnly As System.Boolean Dim result As SwDmDocumentOpenError Dim value As SwDMDocument   value = instance.GetDocument(allowReadOnly, result) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDocument GetDocument(     System.bool allowReadOnly,    out SwDmDocumentOpenError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDocument^ GetDocument(  &   System.bool allowReadOnly, &   [Out] SwDmDocumentOpenError result ) ``` | |

#### Parameters

*allowReadOnly*
:   True to open the document as read-only, false as read-write

*result*
:   Error as defined by [SwDmDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

#### Return Value

Pointer to the [ISwDMDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) object

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent3::GetDocument](swdocumentmgr~SwDMComponent3~GetDocument.md).

 

# See Also

#### 

[ISwDMComponent3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3.md)
  
[ISwDMComponent3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3_members.md)

# Availability

SOLIDWORKS Document Manager API 2008 FCS

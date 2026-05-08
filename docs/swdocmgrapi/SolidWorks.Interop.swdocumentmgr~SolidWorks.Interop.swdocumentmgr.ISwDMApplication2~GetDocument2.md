# GetDocument2 Method (ISwDMApplication2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2~GetDocument2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2~GetDocument2.html) on this topic. |
| GetDocument2 Method (ISwDMApplication2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMApplication2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.md) : GetDocument2 Method (ISwDMApplication2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*documentStream*
:   Pointer to an unknown type, the IStream or IStorage storage

*result*
:   Error as defined by [SwDmDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

Gets the specified document from an IStream or IStorage storage.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetDocument2( _    ByVal documentStream As System.Object, _    ByRef result As SwDmDocumentOpenError _ ) As SwDMDocument ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMApplication2 Dim documentStream As System.Object Dim result As SwDmDocumentOpenError Dim value As SwDMDocument   value = instance.GetDocument2(documentStream, result) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDocument GetDocument2(     System.object documentStream,    out SwDmDocumentOpenError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDocument^ GetDocument2(  &   System.Object^ documentStream, &   [Out] SwDmDocumentOpenError result ) ``` | |

#### Parameters

*documentStream*
:   Pointer to an unknown type, the IStream or IStorage storage

*result*
:   Error as defined by [SwDmDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

#### Return Value

Pointer to the [ISwDMDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) object

# Visual Basic for Applications (VBA) Syntax

See [SwDMApplication2::GetDocument2](swdocumentmgr~SwDMApplication2~GetDocument2.md).

# Remarks

Use [ISwDMApplication::GetDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md) to get a document using its name.

# See Also

#### 

[ISwDMApplication2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.md)
  
[ISwDMApplication2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2_members.md)

# Availability

SOLIDWORKS Document Manager API 2007 SP3

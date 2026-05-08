# ReplaceReference Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html) on this topic. |
| ReplaceReference Method (ISwDMDocument) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : ReplaceReference Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*OriginalReference*
:   Name of original reference to replace

*ReplacementReference*
:   Name of reference with which to replace OriginalReference

Changes all instances of the specified original reference to the specified replacement reference in this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub ReplaceReference( _    ByVal OriginalReference As System.String, _    ByVal ReplacementReference As System.String _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim OriginalReference As System.String Dim ReplacementReference As System.String   instance.ReplaceReference(OriginalReference, ReplacementReference) ``` | |

| C# |  |
| --- | --- |
| ``` void ReplaceReference(     System.string OriginalReference,    System.string ReplacementReference ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void ReplaceReference(  &   System.String^ OriginalReference, &   System.String^ ReplacementReference ) ``` | |

#### Parameters

*OriginalReference*
:   Name of original reference to replace

*ReplacementReference*
:   Name of reference with which to replace OriginalReference

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::ReplaceReference](swdocumentmgr~SwDMDocument~ReplaceReference.md).

# Remarks

Before calling this method, you must call [ISwDMDocument13::GetAllExternalReferences4](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4.md).

ISwDMDocument::ReplaceReference expects the fully qualified path names, exactly as those returned by ISwDMDocument13::GetAllExternalReferences4.

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)
  
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.md)
  
**ISwDMDocument30::ClearChangedReferences Method ()**

# Availability

SOLIDWORKS Document Manager API 2004 FCS

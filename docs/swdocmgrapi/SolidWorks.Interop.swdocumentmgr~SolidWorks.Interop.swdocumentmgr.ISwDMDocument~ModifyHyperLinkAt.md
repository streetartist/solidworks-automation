# ModifyHyperLinkAt Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt.html) on this topic. |
| ModifyHyperLinkAt Method (ISwDMDocument) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : ModifyHyperLinkAt Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*at*
:   0-based index at which to set the embedded hyperlink

*newlink*
:   New embedded hyperlink

Sets the embedded hyperlink at the specified index for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub ModifyHyperLinkAt( _    ByVal at As System.Integer, _    ByVal newlink As System.String _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim at As System.Integer Dim newlink As System.String   instance.ModifyHyperLinkAt(at, newlink) ``` | |

| C# |  |
| --- | --- |
| ``` void ModifyHyperLinkAt(     System.int at,    System.string newlink ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void ModifyHyperLinkAt(  &   System.int at, &   System.String^ newlink ) ``` | |

#### Parameters

*at*
:   0-based index at which to set the embedded hyperlink

*newlink*
:   New embedded hyperlink

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::ModifyHyperLinkAt](swdocumentmgr~SwDMDocument~ModifyHyperLinkAt.md).

# Remarks

Before calling this method, call [ISwDMDocument::GetHyperLinksCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinksCount.md) to get the number of embedded hyperlinks for this document.

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)
  
[ISwDMDocument::GetHyperLinkAt Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS

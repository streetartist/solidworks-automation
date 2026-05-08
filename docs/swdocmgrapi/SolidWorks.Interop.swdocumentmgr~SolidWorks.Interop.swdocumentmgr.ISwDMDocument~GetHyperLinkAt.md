# GetHyperLinkAt Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt.html) on this topic. |
| GetHyperLinkAt Method (ISwDMDocument) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : GetHyperLinkAt Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*at*
:   0-based index at which to get the embedded hyperlinks

Gets the embedded hyperlinks at the specified index for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetHyperLinkAt( _    ByVal at As System.Integer _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim at As System.Integer Dim value As System.String   value = instance.GetHyperLinkAt(at) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetHyperLinkAt(     System.int at ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetHyperLinkAt(  &   System.int at ) ``` | |

#### Parameters

*at*
:   0-based index at which to get the embedded hyperlinks

#### Return Value

Hyperlinks

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::GetHyperLinkAt](swdocumentmgr~SwDMDocument~GetHyperLinkAt.md).

# Example

[Get Hyperlinks (C#)](Get_Hyperlinks_Example_CSharp.htm)
  
[Get Hyperlinks (VB.NET)](Get_Hyperlinks_Example_VBNET.htm)

# Remarks

Before calling this method, call [ISwDMDocument::GetHyperLinksCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinksCount.md) to get the number of embedded hyperlinks associated with this document.

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)
  
[ISwDMDocument::ModifyHyperLinkAt Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS

# GetHyperLinksCount Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinksCount`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinksCount.html) on this topic. |
| GetHyperLinksCount Method (ISwDMDocument) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : GetHyperLinksCount Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the number of embedded hyperlinks for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetHyperLinksCount() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim value As System.Integer   value = instance.GetHyperLinksCount() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetHyperLinksCount() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetHyperLinksCount(); ``` | |

#### Return Value

Number of embedded hyperlinks

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::GetHyperLinksCount](swdocumentmgr~SwDMDocument~GetHyperLinksCount.md).

# Example

[Get Hyperlinks (C#)](Get_Hyperlinks_Example_CSharp.htm)
  
[Get Hyperlinks (VB.NET)](Get_Hyperlinks_Example_VBNET.htm)

# Remarks

Call this method before calling [ISwDMDocument::GetHyperLinkAt](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt.md) and [ISwDMDocument::ModifyHyperLinkAt](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt.md).

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS

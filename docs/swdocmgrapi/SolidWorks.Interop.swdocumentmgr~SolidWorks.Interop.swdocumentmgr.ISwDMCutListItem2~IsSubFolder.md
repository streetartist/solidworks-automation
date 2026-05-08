# IsSubFolder Property (ISwDMCutListItem2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~IsSubFolder`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~IsSubFolder.html) on this topic. |
| IsSubFolder Property (ISwDMCutListItem2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md) : IsSubFolder Property (ISwDMCutListItem2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether a cut-list item is a sub-folder.

**NOTE: This property is a get-only property. Set is not implemented.**

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property IsSubFolder As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem2 Dim value As System.Boolean   instance.IsSubFolder = value   value = instance.IsSubFolder ``` | |

| C# |  |
| --- | --- |
| ``` System.bool IsSubFolder {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.bool IsSubFolder {    System.bool get();    void set ( &   System.bool value); } ``` | |

#### Property Value

True if the cut-list item is a sub-folder, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem2::IsSubFolder](swdocumentmgr~SwDMCutListItem2~IsSubFolder.md).

# Remarks

A cut-list folder has either one or no child folder.

This property only supports documents saved in SOLIDWORKS 2009 or later.

# See Also

#### 

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md)
  
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.md)

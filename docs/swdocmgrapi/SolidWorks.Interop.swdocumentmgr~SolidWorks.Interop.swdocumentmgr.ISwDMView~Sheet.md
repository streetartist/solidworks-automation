# Sheet Property (ISwDMView)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~Sheet`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~Sheet.html) on this topic. |
| Sheet Property (ISwDMView) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.md) : Sheet Property (ISwDMView) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets or sets the sheet for this drawing view.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property Sheet As SwDMSheet ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMView Dim value As SwDMSheet   instance.Sheet = value   value = instance.Sheet ``` | |

| C# |  |
| --- | --- |
| ``` SwDMSheet Sheet {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property SwDMSheet^ Sheet {    SwDMSheet^ get();    void set ( &   SwDMSheet^ value); } ``` | |

#### Property Value

[Sheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMView::Sheet](swdocumentmgr~SwDMView~Sheet.md).

# See Also

#### 

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.md)
  
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

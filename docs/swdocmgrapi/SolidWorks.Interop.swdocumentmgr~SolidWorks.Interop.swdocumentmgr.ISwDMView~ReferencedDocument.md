# ReferencedDocument Property (ISwDMView)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedDocument`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedDocument.html) on this topic. |
| ReferencedDocument Property (ISwDMView) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.md) : ReferencedDocument Property (ISwDMView) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets or sets the name of the document for this drawing view.  
  

**NOTE:** **This property is a get-only property. Set is not implemented.**

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property ReferencedDocument As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMView Dim value As System.String   instance.ReferencedDocument = value   value = instance.ReferencedDocument ``` | |

| C# |  |
| --- | --- |
| ``` System.string ReferencedDocument {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ ReferencedDocument {    System.String^ get();    void set ( &   System.String^ value); } ``` | |

#### Property Value

Name of document

# Visual Basic for Applications (VBA) Syntax

See [SwDMView::ReferencedDocument](swdocumentmgr~SwDMView~ReferencedDocument.md).

# See Also

#### 

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.md)
  
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

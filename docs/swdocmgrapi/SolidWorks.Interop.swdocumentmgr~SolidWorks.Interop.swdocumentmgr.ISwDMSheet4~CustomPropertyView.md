# CustomPropertyView Property (ISwDMSheet4)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4~CustomPropertyView`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4~CustomPropertyView.html) on this topic. |
| CustomPropertyView Property (ISwDMSheet4) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMSheet4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.md) : CustomPropertyView Property (ISwDMSheet4) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the drawing view on which this sheet's custom properties reside.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property CustomPropertyView As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMSheet4 Dim value As System.Object   value = instance.CustomPropertyView ``` | |

| C# |  |
| --- | --- |
| ``` System.object CustomPropertyView {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.Object^ CustomPropertyView {    System.Object^ get(); } ``` | |

#### Property Value

[ISwDMView](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.md); null if the sheet has no views

# Visual Basic for Applications (VBA) Syntax

See [SwDMSheet4::CustomPropertyView](swdocumentmgr~SwDMSheet4~CustomPropertyView.md).

# Example

See the [ISwDMSheet4](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.md) examples.

# Remarks

This property works only with documents saved in SOLIDWORKS 2017 or later.

# See Also

#### 

[ISwDMSheet4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.md)
  
[ISwDMSheet4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4_members.md)

# Availability

SOLIDWORKS Document Manager API 2017 FCS

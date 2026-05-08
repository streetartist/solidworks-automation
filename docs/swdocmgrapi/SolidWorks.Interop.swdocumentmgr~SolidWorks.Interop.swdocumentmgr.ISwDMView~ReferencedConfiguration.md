# ReferencedConfiguration Property (ISwDMView)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedConfiguration`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedConfiguration.html) on this topic. |
| ReferencedConfiguration Property (ISwDMView) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.md) : ReferencedConfiguration Property (ISwDMView) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the name of the configuration for this drawing view.

**NOTE:** **This property is a get-only property. Set is not implemented.**

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property ReferencedConfiguration As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMView Dim value As System.String   instance.ReferencedConfiguration = value   value = instance.ReferencedConfiguration ``` | |

| C# |  |
| --- | --- |
| ``` System.string ReferencedConfiguration {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ ReferencedConfiguration {    System.String^ get();    void set ( &   System.String^ value); } ``` | |

#### Property Value

Name of configuration

# Visual Basic for Applications (VBA) Syntax

See [SwDMView::ReferencedConfiguration](swdocumentmgr~SwDMView~ReferencedConfiguration.md).

# See Also

#### 

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.md)
  
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.md)
  
[ISwDMView2::ReferencedConfigurationID Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2~ReferencedConfigurationID.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

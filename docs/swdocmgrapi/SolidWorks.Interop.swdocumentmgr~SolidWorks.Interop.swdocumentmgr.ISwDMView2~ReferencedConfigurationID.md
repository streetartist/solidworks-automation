# ReferencedConfigurationID Property (ISwDMView2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2~ReferencedConfigurationID`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2~ReferencedConfigurationID.html) on this topic. |
| ReferencedConfigurationID Property (ISwDMView2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMView2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2.md) : ReferencedConfigurationID Property (ISwDMView2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the ID of the configuration for this drawing view.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property ReferencedConfigurationID As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMView2 Dim value As System.Integer   value = instance.ReferencedConfigurationID ``` | |

| C# |  |
| --- | --- |
| ``` System.int ReferencedConfigurationID {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.int ReferencedConfigurationID {    System.int get(); } ``` | |

#### Property Value

ID of configuration or -1 for legacy files (see **Remarks**)

# Visual Basic for Applications (VBA) Syntax

See [SwDMView2::ReferencedConfigurationID](swdocumentmgr~SwDMView2~ReferencedConfigurationID.md).

# Remarks

This property works only with documents saved in SOLIDWORKS 2017 or later.

# See Also

#### 

[ISwDMView2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2.md)
  
[ISwDMView2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2_members.md)
  
[ISwDMView::ReferencedConfiguration Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedConfiguration.md)

# Availability

SOLIDWORKS Document Manager API 2017 FCS

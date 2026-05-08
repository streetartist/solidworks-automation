# SelectName2 Property (ISwDMComponent11)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11~SelectName2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11~SelectName2.html) on this topic. |
| SelectName2 Property (ISwDMComponent11) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.md) : SelectName2 Property (ISwDMComponent11) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the name of the component needed to specify in the component list in [ISldWorks::IDocumentSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~ComponentList.md) during a selective open using [SldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property SelectName2 As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent11 Dim value As System.String   value = instance.SelectName2 ``` | |

| C# |  |
| --- | --- |
| ``` System.string SelectName2 {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ SelectName2 {    System.String^ get(); } ``` | |

#### Property Value

Name to use during a selective open

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent11::SelectName2](swdocumentmgr~SwDMComponent11~SelectName2.md).

# Example

See the [ISwDMComponent11](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.md) examples.

# See Also

#### 

[ISwDMComponent11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.md)
  
[ISwDMComponent11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11_members.md)

# Availability

SOLIDWORKS Document Manager API 2021 SP0

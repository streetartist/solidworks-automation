# GetTopBlends Method (ISwDMDimXpertExtrudeFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetTopBlends`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetTopBlends.html) on this topic. |
| GetTopBlends Method (ISwDMDimXpertExtrudeFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.md) : GetTopBlends Method (ISwDMDimXpertExtrudeFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the DimXpert blend feature at the top of this DimXpert extrude.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetTopBlends() As SwDMDimXpertFeature ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertExtrudeFeature Dim value As SwDMDimXpertFeature   value = instance.GetTopBlends() ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDimXpertFeature GetTopBlends() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDimXpertFeature^ GetTopBlends(); ``` | |

#### Return Value

[ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertExtrudeFeature::GetTopBlends](swdocumentmgr~SwDMDimXpertExtrudeFeature~GetTopBlends.md).

# Example

See the examples on the interface page.

# Remarks

The top blend is typically an [ISwDMDimXpertFilletFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.md).

# See Also

#### 

[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.md)
  
[ISwDMDimXpertExtrudeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

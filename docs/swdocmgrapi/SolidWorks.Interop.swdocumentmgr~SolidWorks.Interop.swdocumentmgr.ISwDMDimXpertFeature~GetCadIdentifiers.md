# GetCadIdentifiers Method (ISwDMDimXpertFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~GetCadIdentifiers`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~GetCadIdentifiers.html) on this topic. |
| GetCadIdentifiers Method (ISwDMDimXpertFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md) : GetCadIdentifiers Method (ISwDMDimXpertFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets all of the CAD identifiers of this DimXpert feature.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCadIdentifiers() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertFeature Dim value As System.Object   value = instance.GetCadIdentifiers() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetCadIdentifiers() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetCadIdentifiers(); ``` | |

#### Return Value

Array of strings; the format of each string is bodyid:faceid

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertFeature::GetCadIdentifiers](swdocumentmgr~SwDMDimXpertFeature~GetCadIdentifiers.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)
  
[ISwDMDimXpertFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.md)
  
[ISwDMDimXpertFeature::IGetCadIdentifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~IGetCadIdentifiers.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

# GetFeatures Method (ISwDMDimXpertPart)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetFeatures.html) on this topic. |
| GetFeatures Method (ISwDMDimXpertPart) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertPart Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart.md) : GetFeatures Method (ISwDMDimXpertPart) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets all of the DimXpert features in the model.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetFeatures() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertPart Dim value As System.Object   value = instance.GetFeatures() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetFeatures() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetFeatures(); ``` | |

#### Return Value

Array of [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)s

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertPart::GetFeatures](swdocumentmgr~SwDMDimXpertPart~GetFeatures.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertPart Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart.md)
  
[ISwDMDimXpertPart Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart_members.md)
  
[ISwDMDimXpertPart::IGetFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetFeatures.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

# Feature Property (ISwDMDimXpertAnnotation)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~Feature`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~Feature.html) on this topic. |
| Feature Property (ISwDMDimXpertAnnotation) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.md) : Feature Property (ISwDMDimXpertAnnotation) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the DimXpert feature to which this DimXpert annotation is applied.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property Feature As SwDMDimXpertFeature ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertAnnotation Dim value As SwDMDimXpertFeature   value = instance.Feature ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDimXpertFeature Feature {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property SwDMDimXpertFeature^ Feature {    SwDMDimXpertFeature^ get(); } ``` | |

#### Property Value

[ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertAnnotation::Feature](swdocumentmgr~SwDMDimXpertAnnotation~Feature.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.md)
  
[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

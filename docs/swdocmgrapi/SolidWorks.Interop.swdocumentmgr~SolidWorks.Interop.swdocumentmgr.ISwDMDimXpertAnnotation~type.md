# type Property (ISwDMDimXpertAnnotation)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~type`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~type.html) on this topic. |
| type Property (ISwDMDimXpertAnnotation) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.md) : type Property (ISwDMDimXpertAnnotation) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the type of this DimXpert annotation.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property type As swDmDimXpertAnnotationType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertAnnotation Dim value As swDmDimXpertAnnotationType_e   value = instance.type ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertAnnotationType_e type {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertAnnotationType_e type {    swDmDimXpertAnnotationType_e get(); } ``` | |

#### Property Value

Type of annotation as defined in [swDmDimXpertAnnotationType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertAnnotationType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertAnnotation::type](swdocumentmgr~SwDMDimXpertAnnotation~type.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.md)
  
[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

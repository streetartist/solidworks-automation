# DimensionType Property (ISwDMDimXpertDimensionTolerance)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~DimensionType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~DimensionType.html) on this topic. |
| DimensionType Property (ISwDMDimXpertDimensionTolerance) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.md) : DimensionType Property (ISwDMDimXpertDimensionTolerance) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the type of this DimXpert dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property DimensionType As swDmDimXpertDimensionToleranceType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertDimensionTolerance Dim value As swDmDimXpertDimensionToleranceType_e   value = instance.DimensionType ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertDimensionToleranceType_e DimensionType {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertDimensionToleranceType_e DimensionType {    swDmDimXpertDimensionToleranceType_e get(); } ``` | |

#### Property Value

Type of dimension tolerance as defined in [SwDmDimXpertDimensionToleranceType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertDimensionToleranceType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertDimensionTolerance::DimensionType](swdocumentmgr~SwDMDimXpertDimensionTolerance~DimensionType.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.md)
  
[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

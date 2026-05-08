# DimensionTypeIntraFeature Property (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~DimensionTypeIntraFeature`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~DimensionTypeIntraFeature.html) on this topic. |
| DimensionTypeIntraFeature Property (ISwDMDimXpertCompositeDistanceBetweenDimTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md) : DimensionTypeIntraFeature Property (ISwDMDimXpertCompositeDistanceBetweenDimTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the type of dimension tolerance used by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property DimensionTypeIntraFeature As swDmDimXpertDimensionToleranceType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol Dim value As swDmDimXpertDimensionToleranceType_e   value = instance.DimensionTypeIntraFeature ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertDimensionToleranceType_e DimensionTypeIntraFeature {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertDimensionToleranceType_e DimensionTypeIntraFeature {    swDmDimXpertDimensionToleranceType_e get(); } ``` | |

#### Property Value

Type of dimension tolerance as defined in [swDmDimXpertDimensionToleranceType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertDimensionToleranceType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::DimensionTypeIntraFeature](swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~DimensionTypeIntraFeature.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md)
  
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

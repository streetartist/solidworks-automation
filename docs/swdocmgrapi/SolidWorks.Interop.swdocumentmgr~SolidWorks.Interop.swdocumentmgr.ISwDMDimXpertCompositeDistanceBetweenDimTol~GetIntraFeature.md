# GetIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.html) on this topic. |
| GetIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md) : GetIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Feature*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

*FosUsage*
:   How to treat the feature of size when applying this tolerance as defined in [swDmDimXpertDistanceFosUsage\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertDistanceFosUsage_e.md)

Gets the DimXpert feature located by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetIntraFeature( _    ByRef Feature As SwDMDimXpertFeature, _    ByRef FosUsage As swDmDimXpertDistanceFosUsage_e _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol Dim Feature As SwDMDimXpertFeature Dim FosUsage As swDmDimXpertDistanceFosUsage_e Dim value As System.Boolean   value = instance.GetIntraFeature(Feature, FosUsage) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetIntraFeature(     out SwDMDimXpertFeature Feature,    out swDmDimXpertDistanceFosUsage_e FosUsage ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetIntraFeature(  &   [Out] SwDMDimXpertFeature^ Feature, &   [Out] swDmDimXpertDistanceFosUsage_e FosUsage ) ``` | |

#### Parameters

*Feature*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

*FosUsage*
:   How to treat the feature of size when applying this tolerance as defined in [swDmDimXpertDistanceFosUsage\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertDistanceFosUsage_e.md)

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::GetIntraFeature](swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md)
  
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

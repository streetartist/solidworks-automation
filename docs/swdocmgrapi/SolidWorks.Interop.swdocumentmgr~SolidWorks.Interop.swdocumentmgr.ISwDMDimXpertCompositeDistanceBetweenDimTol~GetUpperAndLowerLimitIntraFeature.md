# GetUpperAndLowerLimitIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetUpperAndLowerLimitIntraFeature`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetUpperAndLowerLimitIntraFeature.html) on this topic. |
| GetUpperAndLowerLimitIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md) : GetUpperAndLowerLimitIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Upper*
:   Upper tolerance limit for feature-locating

*Lower*
:   Lower tolerance limit for feature-locating

Gets the upper and lower tolerance limits used by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetUpperAndLowerLimitIntraFeature( _    ByRef Upper As System.Double, _    ByRef Lower As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol Dim Upper As System.Double Dim Lower As System.Double Dim value As System.Boolean   value = instance.GetUpperAndLowerLimitIntraFeature(Upper, Lower) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetUpperAndLowerLimitIntraFeature(     out System.double Upper,    out System.double Lower ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetUpperAndLowerLimitIntraFeature(  &   [Out] System.double Upper, &   [Out] System.double Lower ) ``` | |

#### Parameters

*Upper*
:   Upper tolerance limit for feature-locating

*Lower*
:   Lower tolerance limit for feature-locating

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::GetUpperAndLowerLimitIntraFeature](swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~GetUpperAndLowerLimitIntraFeature.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md)
  
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

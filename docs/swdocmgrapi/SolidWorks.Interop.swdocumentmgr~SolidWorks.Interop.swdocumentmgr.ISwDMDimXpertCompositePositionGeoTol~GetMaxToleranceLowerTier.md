# GetMaxToleranceLowerTier Method (ISwDMDimXpertCompositePositionGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~GetMaxToleranceLowerTier`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~GetMaxToleranceLowerTier.html) on this topic. |
| GetMaxToleranceLowerTier Method (ISwDMDimXpertCompositePositionGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.md) : GetMaxToleranceLowerTier Method (ISwDMDimXpertCompositePositionGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*IsMax*
:   True, if maximum tolerance is set in the lower tier; false, otherwise

*Tolerance*
:   Maximum tolerance in the lower tier

Gets whether the maximum tolerance is set in the lower tier for this DimXpert composite position geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetMaxToleranceLowerTier( _    ByRef IsMax As System.Boolean, _    ByRef Tolerance As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompositePositionGeoTol Dim IsMax As System.Boolean Dim Tolerance As System.Double Dim value As System.Boolean   value = instance.GetMaxToleranceLowerTier(IsMax, Tolerance) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetMaxToleranceLowerTier(     out System.bool IsMax,    out System.double Tolerance ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetMaxToleranceLowerTier(  &   [Out] System.bool IsMax, &   [Out] System.double Tolerance ) ``` | |

#### Parameters

*IsMax*
:   True, if maximum tolerance is set in the lower tier; false, otherwise

*Tolerance*
:   Maximum tolerance in the lower tier

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompositePositionGeoTol::GetMaxToleranceLowerTier](swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~GetMaxToleranceLowerTier.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.md)
  
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

# GetPlanarZoneVector Method (ISwDMDimXpertStraightnessGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol~GetPlanarZoneVector`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol~GetPlanarZoneVector.html) on this topic. |
| GetPlanarZoneVector Method (ISwDMDimXpertStraightnessGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertStraightnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol.md) : GetPlanarZoneVector Method (ISwDMDimXpertStraightnessGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*I*
:   i component of planar zone vector

*J*
:   j component of planar zone vector

*K*
:   k component of planar zone vector

Gets the planar zone vector that is used to compute this DimXpert straightness geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPlanarZoneVector( _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertStraightnessGeoTol Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetPlanarZoneVector(I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetPlanarZoneVector(     out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetPlanarZoneVector(  &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*I*
:   i component of planar zone vector

*J*
:   j component of planar zone vector

*K*
:   k component of planar zone vector

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertStraightnessGeoTol::GetPlanarZoneVector](swdocumentmgr~SwDMDimXpertStraightnessGeoTol~GetPlanarZoneVector.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertStraightnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol.md)
  
[ISwDMDimXpertStraightnessGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

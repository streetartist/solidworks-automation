# GetZoneDirection Method (ISwDMDimXpertSymmetryGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol~GetZoneDirection`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol~GetZoneDirection.html) on this topic. |
| GetZoneDirection Method (ISwDMDimXpertSymmetryGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertSymmetryGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol.md) : GetZoneDirection Method (ISwDMDimXpertSymmetryGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*I*
:   i component of zone direction vector

*J*
:   j component of zone direction vector

*K*
:   k component of zone direction vector

Gets the zone direction of this DimXpert symmetry geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetZoneDirection( _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertSymmetryGeoTol Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetZoneDirection(I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetZoneDirection(     out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetZoneDirection(  &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*I*
:   i component of zone direction vector

*J*
:   j component of zone direction vector

*K*
:   k component of zone direction vector

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertSymmetryGeoTol::GetZoneDirection](swdocumentmgr~SwDMDimXpertSymmetryGeoTol~GetZoneDirection.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertSymmetryGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol.md)
  
[ISwDMDimXpertSymmetryGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

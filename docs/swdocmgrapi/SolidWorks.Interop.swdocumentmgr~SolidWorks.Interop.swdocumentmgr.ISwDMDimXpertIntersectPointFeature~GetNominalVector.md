# GetNominalVector Method (ISwDMDimXpertIntersectPointFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetNominalVector`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetNominalVector.html) on this topic. |
| GetNominalVector Method (ISwDMDimXpertIntersectPointFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.md) : GetNominalVector Method (ISwDMDimXpertIntersectPointFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*I*
:   i component of the direction vector of the intersect point

*J*
:   j component of the direction vector of the intersect point

*K*
:   k component of the direction vector of the intersect point

Gets the direction vector of this DimXpert intersect point.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalVector( _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertIntersectPointFeature Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalVector(I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalVector(     out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalVector(  &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*I*
:   i component of the direction vector of the intersect point

*J*
:   j component of the direction vector of the intersect point

*K*
:   k component of the direction vector of the intersect point

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertIntersectPointFeature::GetNominalVector](swdocumentmgr~SwDMDimXpertIntersectPointFeature~GetNominalVector.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.md)
  
[ISwDMDimXpertIntersectPointFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

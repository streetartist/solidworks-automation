# GetNominalLine Method (ISwDMDimXpertIntersectLineFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature~GetNominalLine`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature~GetNominalLine.html) on this topic. |
| GetNominalLine Method (ISwDMDimXpertIntersectLineFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature.md) : GetNominalLine Method (ISwDMDimXpertIntersectLineFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*X*
:   x coordinate of the intersect line

*Y*
:   y coordinate of the intersect line

*Z*
:   z coordinate of the intersect line

*I*
:   i component of the direction vector of the intersect line

*J*
:   j component of the direction vector of the intersect line

*K*
:   k component of the direction vector of the intersect line

Gets the coordinates and vector for this DimXpert intersect line.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalLine( _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertIntersectLineFeature Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalLine(X, Y, Z, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalLine(     out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalLine(  &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*X*
:   x coordinate of the intersect line

*Y*
:   y coordinate of the intersect line

*Z*
:   z coordinate of the intersect line

*I*
:   i component of the direction vector of the intersect line

*J*
:   j component of the direction vector of the intersect line

*K*
:   k component of the direction vector of the intersect line

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertIntersectLineFeature::GetNominalLine](swdocumentmgr~SwDMDimXpertIntersectLineFeature~GetNominalLine.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature.md)
  
[ISwDMDimXpertIntersectLineFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

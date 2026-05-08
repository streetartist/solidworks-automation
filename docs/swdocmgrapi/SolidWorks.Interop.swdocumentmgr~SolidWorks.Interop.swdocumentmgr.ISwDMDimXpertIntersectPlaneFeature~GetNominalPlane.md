# GetNominalPlane Method (ISwDMDimXpertIntersectPlaneFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature~GetNominalPlane`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature~GetNominalPlane.html) on this topic. |
| GetNominalPlane Method (ISwDMDimXpertIntersectPlaneFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature.md) : GetNominalPlane Method (ISwDMDimXpertIntersectPlaneFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*X*
:   x coordinate of the intersect plane

*Y*
:   y coordinate of the intersect plane

*Z*
:   z coordinate of the intersect plane

*I*
:   i component of the direction vector of the intersect plane

*J*
:   j component of the direction vector of the intersect plane

*K*
:   k component of the direction vector of the intersect plane

Gets the coordinates and vector for this DimXpert intersect plane.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalPlane( _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertIntersectPlaneFeature Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalPlane(X, Y, Z, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalPlane(     out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalPlane(  &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*X*
:   x coordinate of the intersect plane

*Y*
:   y coordinate of the intersect plane

*Z*
:   z coordinate of the intersect plane

*I*
:   i component of the direction vector of the intersect plane

*J*
:   j component of the direction vector of the intersect plane

*K*
:   k component of the direction vector of the intersect plane

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertIntersectPlaneFeature::GetNominalPlane](swdocumentmgr~SwDMDimXpertIntersectPlaneFeature~GetNominalPlane.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature.md)
  
[ISwDMDimXpertIntersectPlaneFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

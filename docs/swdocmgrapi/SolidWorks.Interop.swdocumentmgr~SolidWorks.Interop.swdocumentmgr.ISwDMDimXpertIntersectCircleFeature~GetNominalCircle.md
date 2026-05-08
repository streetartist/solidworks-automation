# GetNominalCircle Method (ISwDMDimXpertIntersectCircleFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature~GetNominalCircle`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature~GetNominalCircle.html) on this topic. |
| GetNominalCircle Method (ISwDMDimXpertIntersectCircleFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature.md) : GetNominalCircle Method (ISwDMDimXpertIntersectCircleFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*R*
:   Radius of the intersect circle

*X*
:   x coordinate of the origin of the intersect circle

*Y*
:   y coordinate of the origin of the intersect circle

*Z*
:   z coordinate of the origin of the intersect circle

*I*
:   i component of the direction vector of the intersect circle

*J*
:   j component of the direction vector of the intersect circle

*K*
:   k component of the direction vector of the intersect circle

Gets the origin coordinates, radius, and vector for this DimXpert intersect circle.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalCircle( _    ByRef R As System.Double, _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertIntersectCircleFeature Dim R As System.Double Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalCircle(R, X, Y, Z, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalCircle(     out System.double R,    out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalCircle(  &   [Out] System.double R, &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*R*
:   Radius of the intersect circle

*X*
:   x coordinate of the origin of the intersect circle

*Y*
:   y coordinate of the origin of the intersect circle

*Z*
:   z coordinate of the origin of the intersect circle

*I*
:   i component of the direction vector of the intersect circle

*J*
:   j component of the direction vector of the intersect circle

*K*
:   k component of the direction vector of the intersect circle

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertIntersectCircleFeature::GetNominalCircle](swdocumentmgr~SwDMDimXpertIntersectCircleFeature~GetNominalCircle.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature.md)
  
[ISwDMDimXpertIntersectCircleFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

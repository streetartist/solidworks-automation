# GetNominalBottomPlane Method (ISwDMDimXpertCylinderFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetNominalBottomPlane`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetNominalBottomPlane.html) on this topic. |
| GetNominalBottomPlane Method (ISwDMDimXpertCylinderFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.md) : GetNominalBottomPlane Method (ISwDMDimXpertCylinderFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*X*
:   x coordinate of the bottom plane

*Y*
:   y coordinate of the bottom plane

*Z*
:   z coordinate of the bottom plane

*I*
:   i component of the direction vector of the bottom plane

*J*
:   j component of the direction vector of the bottom plane

*K*
:   k component of the direction vector of the bottom plane

Gets the coordinates and vector for the plane at the bottom of this DimXpert cylinder.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalBottomPlane( _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCylinderFeature Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalBottomPlane(X, Y, Z, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalBottomPlane(     out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalBottomPlane(  &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*X*
:   x coordinate of the bottom plane

*Y*
:   y coordinate of the bottom plane

*Z*
:   z coordinate of the bottom plane

*I*
:   i component of the direction vector of the bottom plane

*J*
:   j component of the direction vector of the bottom plane

*K*
:   k component of the direction vector of the bottom plane

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCylinderFeature::GetNominalBottomPlane](swdocumentmgr~SwDMDimXpertCylinderFeature~GetNominalBottomPlane.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.md)
  
[ISwDMDimXpertCylinderFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

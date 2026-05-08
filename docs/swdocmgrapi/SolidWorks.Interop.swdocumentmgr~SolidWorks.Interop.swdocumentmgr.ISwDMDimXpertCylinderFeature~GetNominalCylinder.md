# GetNominalCylinder Method (ISwDMDimXpertCylinderFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetNominalCylinder`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetNominalCylinder.html) on this topic. |
| GetNominalCylinder Method (ISwDMDimXpertCylinderFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.md) : GetNominalCylinder Method (ISwDMDimXpertCylinderFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*R*
:   Radius of cylinder

*X*
:   x coordinate of the cylinder

*Y*
:   y coordinate of the cylinder

*Z*
:   z coordinate of the cylinder

*I*
:   i component of the direction vector of the cylinder

*J*
:   j component of the direction vector of the cylinder

*K*
:   k component of the direction vector of the cylinder

Gets various attributes for this DimXpert cylinder.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalCylinder( _    ByRef R As System.Double, _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCylinderFeature Dim R As System.Double Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalCylinder(R, X, Y, Z, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalCylinder(     out System.double R,    out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalCylinder(  &   [Out] System.double R, &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*R*
:   Radius of cylinder

*X*
:   x coordinate of the cylinder

*Y*
:   y coordinate of the cylinder

*Z*
:   z coordinate of the cylinder

*I*
:   i component of the direction vector of the cylinder

*J*
:   j component of the direction vector of the cylinder

*K*
:   k component of the direction vector of the cylinder

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCylinderFeature::GetNominalCylinder](swdocumentmgr~SwDMDimXpertCylinderFeature~GetNominalCylinder.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.md)
  
[ISwDMDimXpertCylinderFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

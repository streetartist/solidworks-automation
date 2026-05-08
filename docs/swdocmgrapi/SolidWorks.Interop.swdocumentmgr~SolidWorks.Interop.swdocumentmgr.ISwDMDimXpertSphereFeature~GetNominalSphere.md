# GetNominalSphere Method (ISwDMDimXpertSphereFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature~GetNominalSphere`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature~GetNominalSphere.html) on this topic. |
| GetNominalSphere Method (ISwDMDimXpertSphereFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertSphereFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature.md) : GetNominalSphere Method (ISwDMDimXpertSphereFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*R*
:   Radius of the sphere

*X*
:   x coordinate of the sphere origin

*Y*
:   y coordinate of the sphere origin

*Z*
:   z coordinate of the sphere origin

Gets the origin coordinates and radius of this DimXpert sphere.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalSphere( _    ByRef R As System.Double, _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertSphereFeature Dim R As System.Double Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim value As System.Boolean   value = instance.GetNominalSphere(R, X, Y, Z) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalSphere(     out System.double R,    out System.double X,    out System.double Y,    out System.double Z ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalSphere(  &   [Out] System.double R, &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z ) ``` | |

#### Parameters

*R*
:   Radius of the sphere

*X*
:   x coordinate of the sphere origin

*Y*
:   y coordinate of the sphere origin

*Z*
:   z coordinate of the sphere origin

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertSphereFeature::GetNominalSphere](swdocumentmgr~SwDMDimXpertSphereFeature~GetNominalSphere.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertSphereFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature.md)
  
[ISwDMDimXpertSphereFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

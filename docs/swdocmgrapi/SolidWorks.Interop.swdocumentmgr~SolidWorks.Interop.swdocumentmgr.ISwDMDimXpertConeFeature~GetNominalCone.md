# GetNominalCone Method (ISwDMDimXpertConeFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature~GetNominalCone`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature~GetNominalCone.html) on this topic. |
| GetNominalCone Method (ISwDMDimXpertConeFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.md) : GetNominalCone Method (ISwDMDimXpertConeFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Angle*
:   Angle in radians of the cone

*X*
:   x coordinate of the cone

*Y*
:   y coordinate of the cone

*Z*
:   z coordinate of the cone

*I*
:   i component of the direction vector of the cone

*J*
:   j component of the direction vector of the cone

*K*
:   k component of the direction vector of the cone

Gets various attributes for this DimXpert cone.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalCone( _    ByRef Angle As System.Double, _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertConeFeature Dim Angle As System.Double Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalCone(Angle, X, Y, Z, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalCone(     out System.double Angle,    out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalCone(  &   [Out] System.double Angle, &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*Angle*
:   Angle in radians of the cone

*X*
:   x coordinate of the cone

*Y*
:   y coordinate of the cone

*Z*
:   z coordinate of the cone

*I*
:   i component of the direction vector of the cone

*J*
:   j component of the direction vector of the cone

*K*
:   k component of the direction vector of the cone

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertConeFeature::GetNominalCone](swdocumentmgr~SwDMDimXpertConeFeature~GetNominalCone.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.md)
  
[ISwDMDimXpertConeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

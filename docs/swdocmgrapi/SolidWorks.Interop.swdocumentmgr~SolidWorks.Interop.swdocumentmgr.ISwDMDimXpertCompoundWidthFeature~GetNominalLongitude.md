# GetNominalLongitude Method (ISwDMDimXpertCompoundWidthFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature~GetNominalLongitude`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature~GetNominalLongitude.html) on this topic. |
| GetNominalLongitude Method (ISwDMDimXpertCompoundWidthFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.md) : GetNominalLongitude Method (ISwDMDimXpertCompoundWidthFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*I*
:   i component of longitudinal unit vector of compound width

*J*
:   j component of longitudinal unit vector of compound width

*K*
:   k component of longitudinal unit vector of compound width

Gets the longitudinal vector for this DimXpert compound width.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalLongitude( _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompoundWidthFeature Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalLongitude(I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalLongitude(     out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalLongitude(  &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*I*
:   i component of longitudinal unit vector of compound width

*J*
:   j component of longitudinal unit vector of compound width

*K*
:   k component of longitudinal unit vector of compound width

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompoundWidthFeature::GetNominalLongitude](swdocumentmgr~SwDMDimXpertCompoundWidthFeature~GetNominalLongitude.md).

# Example

See the examples on the interface page.

# Remarks

The i, j, and k components of the longitudinal vector indicate the direction of a feature's length with respect to its part axes. For example, if the length of a feature goes along the y-axis of the part, its longitudinal vector is (0, 1, 0).

# See Also

#### 

[ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.md)
  
[ISwDMDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

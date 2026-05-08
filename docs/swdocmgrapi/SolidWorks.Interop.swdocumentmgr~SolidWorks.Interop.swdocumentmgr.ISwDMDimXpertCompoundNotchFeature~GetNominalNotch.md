# GetNominalNotch Method (ISwDMDimXpertCompoundNotchFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetNominalNotch`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetNominalNotch.html) on this topic. |
| GetNominalNotch Method (ISwDMDimXpertCompoundNotchFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.md) : GetNominalNotch Method (ISwDMDimXpertCompoundNotchFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*width*
:   Width of the compound notch

*Length*
:   Length of the compound notch

*X*
:   x coordinate of the compound notch

*Y*
:   y coordinate of the compound notch

*Z*
:   z coordinate of the compound notch

*I*
:   i component of the direction vector of the compound notch

*J*
:   j component of the direction vector of the compound notch

*K*
:   k component of the direction vector of the compound notch

*LongitudeI*
:   i component of the longitudinal unit vector of the closed slot

*LongitudeJ*
:   j component of the longitudinal unit vector of the closed slot

*LongitudeK*
:   k component of the longitudinal unit vector of the closed slot

Gets various attributes for this DimXpert compound notch.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalNotch( _    ByRef width As System.Double, _    ByRef Length As System.Double, _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double, _    ByRef LongitudeI As System.Double, _    ByRef LongitudeJ As System.Double, _    ByRef LongitudeK As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompoundNotchFeature Dim width As System.Double Dim Length As System.Double Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim LongitudeI As System.Double Dim LongitudeJ As System.Double Dim LongitudeK As System.Double Dim value As System.Boolean   value = instance.GetNominalNotch(width, Length, X, Y, Z, I, J, K, LongitudeI, LongitudeJ, LongitudeK) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalNotch(     out System.double width,    out System.double Length,    out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K,    out System.double LongitudeI,    out System.double LongitudeJ,    out System.double LongitudeK ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalNotch(  &   [Out] System.double width, &   [Out] System.double Length, &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K, &   [Out] System.double LongitudeI, &   [Out] System.double LongitudeJ, &   [Out] System.double LongitudeK ) ``` | |

#### Parameters

*width*
:   Width of the compound notch

*Length*
:   Length of the compound notch

*X*
:   x coordinate of the compound notch

*Y*
:   y coordinate of the compound notch

*Z*
:   z coordinate of the compound notch

*I*
:   i component of the direction vector of the compound notch

*J*
:   j component of the direction vector of the compound notch

*K*
:   k component of the direction vector of the compound notch

*LongitudeI*
:   i component of the longitudinal unit vector of the closed slot

*LongitudeJ*
:   j component of the longitudinal unit vector of the closed slot

*LongitudeK*
:   k component of the longitudinal unit vector of the closed slot

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompoundNotchFeature::GetNominalNotch](swdocumentmgr~SwDMDimXpertCompoundNotchFeature~GetNominalNotch.md).

# Example

See the examples on the interface page.

# Remarks

The i, j, and k components of the longitudinal vector indicate the direction of a feature's length with respect to its part axes. For example, if the length of a feature goes along the y-axis of the part, its longitudinal vector is (0, 1, 0).

# See Also

#### 

[ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.md)
  
[ISwDMDimXpertCompoundNotchFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

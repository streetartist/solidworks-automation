# GetNominalCompoundWidth Method (ISwDMDimXpertCompoundWidthFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature~GetNominalCompoundWidth`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature~GetNominalCompoundWidth.html) on this topic. |
| GetNominalCompoundWidth Method (ISwDMDimXpertCompoundWidthFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.md) : GetNominalCompoundWidth Method (ISwDMDimXpertCompoundWidthFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*width*
:   Width of compound width

*X*
:   x coordinate of compound width

*Y*
:   y coordinate of compound width

*Z*
:   z coordinate of compound width

*I*
:   i component of the direction vector of compound width

*J*
:   j component of the direction vector of compound width

*K*
:   k component of the direction vector of compound width

Gets the coordinates and vector for this DimXpert compound width.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalCompoundWidth( _    ByRef width As System.Double, _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompoundWidthFeature Dim width As System.Double Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetNominalCompoundWidth(width, X, Y, Z, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalCompoundWidth(     out System.double width,    out System.double X,    out System.double Y,    out System.double Z,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalCompoundWidth(  &   [Out] System.double width, &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*width*
:   Width of compound width

*X*
:   x coordinate of compound width

*Y*
:   y coordinate of compound width

*Z*
:   z coordinate of compound width

*I*
:   i component of the direction vector of compound width

*J*
:   j component of the direction vector of compound width

*K*
:   k component of the direction vector of compound width

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompoundWidthFeature::GetNominalCompoundWidth](swdocumentmgr~SwDMDimXpertCompoundWidthFeature~GetNominalCompoundWidth.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.md)
  
[ISwDMDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

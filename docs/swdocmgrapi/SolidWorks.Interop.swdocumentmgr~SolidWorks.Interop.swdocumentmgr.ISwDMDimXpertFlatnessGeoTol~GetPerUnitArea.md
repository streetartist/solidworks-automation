# GetPerUnitArea Method (ISwDMDimXpertFlatnessGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol~GetPerUnitArea`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol~GetPerUnitArea.html) on this topic. |
| GetPerUnitArea Method (ISwDMDimXpertFlatnessGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertFlatnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol.md) : GetPerUnitArea Method (ISwDMDimXpertFlatnessGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Enabled*
:   True if per unit area flatness tolerance is in effect; false if not

*Length*
:   Length for per unit area

*width*
:   Width for per unit area

*I*
:   i component of length direction vector used to compute flatness per unit area

*J*
:   j component of length direction vector used to compute flatness per unit area

*K*
:   k component of length direction vector used to compute flatness per unit area

Gets the per unit area of this flatness geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPerUnitArea( _    ByRef Enabled As System.Boolean, _    ByRef Length As System.Double, _    ByRef width As System.Double, _    ByRef I As System.Double, _    ByRef J As System.Double, _    ByRef K As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertFlatnessGeoTol Dim Enabled As System.Boolean Dim Length As System.Double Dim width As System.Double Dim I As System.Double Dim J As System.Double Dim K As System.Double Dim value As System.Boolean   value = instance.GetPerUnitArea(Enabled, Length, width, I, J, K) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetPerUnitArea(     out System.bool Enabled,    out System.double Length,    out System.double width,    out System.double I,    out System.double J,    out System.double K ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetPerUnitArea(  &   [Out] System.bool Enabled, &   [Out] System.double Length, &   [Out] System.double width, &   [Out] System.double I, &   [Out] System.double J, &   [Out] System.double K ) ``` | |

#### Parameters

*Enabled*
:   True if per unit area flatness tolerance is in effect; false if not

*Length*
:   Length for per unit area

*width*
:   Width for per unit area

*I*
:   i component of length direction vector used to compute flatness per unit area

*J*
:   j component of length direction vector used to compute flatness per unit area

*K*
:   k component of length direction vector used to compute flatness per unit area

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertFlatnessGeoTol::GetPerUnitArea](swdocumentmgr~SwDMDimXpertFlatnessGeoTol~GetPerUnitArea.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertFlatnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol.md)
  
[ISwDMDimXpertFlatnessGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

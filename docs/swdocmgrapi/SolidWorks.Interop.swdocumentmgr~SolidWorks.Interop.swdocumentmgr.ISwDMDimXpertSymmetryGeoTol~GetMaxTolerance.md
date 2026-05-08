# GetMaxTolerance Method (ISwDMDimXpertSymmetryGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol~GetMaxTolerance`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol~GetMaxTolerance.html) on this topic. |
| GetMaxTolerance Method (ISwDMDimXpertSymmetryGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertSymmetryGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol.md) : GetMaxTolerance Method (ISwDMDimXpertSymmetryGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*IsMax*
:   True, if maximum tolerance is set; false, otherwise

*Tolerance*
:   Maximum tolerance

Gets the maximum tolerance for this DimXpert symmetry geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetMaxTolerance( _    ByRef IsMax As System.Boolean, _    ByRef Tolerance As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertSymmetryGeoTol Dim IsMax As System.Boolean Dim Tolerance As System.Double Dim value As System.Boolean   value = instance.GetMaxTolerance(IsMax, Tolerance) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetMaxTolerance(     out System.bool IsMax,    out System.double Tolerance ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetMaxTolerance(  &   [Out] System.bool IsMax, &   [Out] System.double Tolerance ) ``` | |

#### Parameters

*IsMax*
:   True, if maximum tolerance is set; false, otherwise

*Tolerance*
:   Maximum tolerance

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertSymmetryGeoTol::GetMaxTolerance](swdocumentmgr~SwDMDimXpertSymmetryGeoTol~GetMaxTolerance.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertSymmetryGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol.md)
  
[ISwDMDimXpertSymmetryGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

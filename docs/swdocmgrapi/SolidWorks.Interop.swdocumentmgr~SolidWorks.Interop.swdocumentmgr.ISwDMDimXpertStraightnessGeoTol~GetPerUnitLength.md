# GetPerUnitLength Method (ISwDMDimXpertStraightnessGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol~GetPerUnitLength`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol~GetPerUnitLength.html) on this topic. |
| GetPerUnitLength Method (ISwDMDimXpertStraightnessGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertStraightnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol.md) : GetPerUnitLength Method (ISwDMDimXpertStraightnessGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Enabled*
:   True if per unit length straightness tolerance is in effect; false if not

*Distance*
:   Length for per unit length

Gets the per unit length for this DimXpert straightness geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPerUnitLength( _    ByRef Enabled As System.Boolean, _    ByRef Distance As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertStraightnessGeoTol Dim Enabled As System.Boolean Dim Distance As System.Double Dim value As System.Boolean   value = instance.GetPerUnitLength(Enabled, Distance) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetPerUnitLength(     out System.bool Enabled,    out System.double Distance ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetPerUnitLength(  &   [Out] System.bool Enabled, &   [Out] System.double Distance ) ``` | |

#### Parameters

*Enabled*
:   True if per unit length straightness tolerance is in effect; false if not

*Distance*
:   Length for per unit length

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertStraightnessGeoTol::GetPerUnitLength](swdocumentmgr~SwDMDimXpertStraightnessGeoTol~GetPerUnitLength.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertStraightnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol.md)
  
[ISwDMDimXpertStraightnessGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

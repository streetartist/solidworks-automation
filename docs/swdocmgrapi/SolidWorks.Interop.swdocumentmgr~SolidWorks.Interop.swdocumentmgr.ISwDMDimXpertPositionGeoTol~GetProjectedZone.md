# GetProjectedZone Method (ISwDMDimXpertPositionGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~GetProjectedZone`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~GetProjectedZone.html) on this topic. |
| GetProjectedZone Method (ISwDMDimXpertPositionGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.md) : GetProjectedZone Method (ISwDMDimXpertPositionGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Enabled*
:   True if the projected zone is in effect; false otherwise

*Value*
:   Position projected zone value

Gets the projected zone value of this DimXpert position geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetProjectedZone( _    ByRef Enabled As System.Boolean, _    ByRef Value As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertPositionGeoTol Dim Enabled As System.Boolean Dim Value As System.Double Dim value As System.Boolean   value = instance.GetProjectedZone(Enabled, Value) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetProjectedZone(     out System.bool Enabled,    out System.double Value ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetProjectedZone(  &   [Out] System.bool Enabled, &   [Out] System.double Value ) ``` | |

#### Parameters

*Enabled*
:   True if the projected zone is in effect; false otherwise

*Value*
:   Position projected zone value

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertPositionGeoTol::GetProjectedZone](swdocumentmgr~SwDMDimXpertPositionGeoTol~GetProjectedZone.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.md)
  
[ISwDMDimXpertPositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

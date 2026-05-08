# ZoneType Property (ISwDMDimXpertPositionGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~ZoneType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~ZoneType.html) on this topic. |
| ZoneType Property (ISwDMDimXpertPositionGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.md) : ZoneType Property (ISwDMDimXpertPositionGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the zone type of this DimXpert position geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property ZoneType As swDmDimXpertPositionZoneType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertPositionGeoTol Dim value As swDmDimXpertPositionZoneType_e   value = instance.ZoneType ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertPositionZoneType_e ZoneType {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertPositionZoneType_e ZoneType {    swDmDimXpertPositionZoneType_e get(); } ``` | |

#### Property Value

Zone type for the position geometric tolerance as defined in [swDmDimXpertPositionZoneType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertPositionZoneType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertPositionGeoTol::ZoneType](swdocumentmgr~SwDMDimXpertPositionGeoTol~ZoneType.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.md)
  
[ISwDMDimXpertPositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

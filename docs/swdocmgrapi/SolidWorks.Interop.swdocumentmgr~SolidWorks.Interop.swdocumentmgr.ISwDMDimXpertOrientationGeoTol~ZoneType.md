# ZoneType Property (ISwDMDimXpertOrientationGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~ZoneType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~ZoneType.html) on this topic. |
| ZoneType Property (ISwDMDimXpertOrientationGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.md) : ZoneType Property (ISwDMDimXpertOrientationGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the zone type of this DimXpert orientation geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property ZoneType As swDmDimXpertOrientationZoneType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertOrientationGeoTol Dim value As swDmDimXpertOrientationZoneType_e   value = instance.ZoneType ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertOrientationZoneType_e ZoneType {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertOrientationZoneType_e ZoneType {    swDmDimXpertOrientationZoneType_e get(); } ``` | |

#### Property Value

Zone type for the orientation tolerance as defined in [swDmDimXpertOrientationZoneType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertOrientationZoneType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertOrientationGeoTol::ZoneType](swdocumentmgr~SwDMDimXpertOrientationGeoTol~ZoneType.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.md)
  
[ISwDMDimXpertOrientationGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

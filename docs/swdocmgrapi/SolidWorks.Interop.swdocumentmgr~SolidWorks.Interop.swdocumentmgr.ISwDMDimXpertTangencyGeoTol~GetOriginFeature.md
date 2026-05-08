# GetOriginFeature Method (ISwDMDimXpertTangencyGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol~GetOriginFeature`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol~GetOriginFeature.html) on this topic. |
| GetOriginFeature Method (ISwDMDimXpertTangencyGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertTangencyGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol.md) : GetOriginFeature Method (ISwDMDimXpertTangencyGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Feature*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

Gets the DimXpert feature of origin for this DimXpert tangency geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetOriginFeature( _    ByRef Feature As SwDMDimXpertFeature _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertTangencyGeoTol Dim Feature As SwDMDimXpertFeature Dim value As System.Boolean   value = instance.GetOriginFeature(Feature) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetOriginFeature(     out SwDMDimXpertFeature Feature ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetOriginFeature(  &   [Out] SwDMDimXpertFeature^ Feature ) ``` | |

#### Parameters

*Feature*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertTangencyGeoTol::GetOriginFeature](swdocumentmgr~SwDMDimXpertTangencyGeoTol~GetOriginFeature.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertTangencyGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol.md)
  
[ISwDMDimXpertTangencyGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

# GetPlaneFeatures Method (ISwDMDimXpertIntersectLineFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature~GetPlaneFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature~GetPlaneFeatures.html) on this topic. |
| GetPlaneFeatures Method (ISwDMDimXpertIntersectLineFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature.md) : GetPlaneFeatures Method (ISwDMDimXpertIntersectLineFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Feature1*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

*Feature2*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

Gets the DimXpert plane features that intersect to form this DimXpert intersect line.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPlaneFeatures( _    ByRef Feature1 As SwDMDimXpertFeature, _    ByRef Feature2 As SwDMDimXpertFeature _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertIntersectLineFeature Dim Feature1 As SwDMDimXpertFeature Dim Feature2 As SwDMDimXpertFeature Dim value As System.Boolean   value = instance.GetPlaneFeatures(Feature1, Feature2) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetPlaneFeatures(     out SwDMDimXpertFeature Feature1,    out SwDMDimXpertFeature Feature2 ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetPlaneFeatures(  &   [Out] SwDMDimXpertFeature^ Feature1, &   [Out] SwDMDimXpertFeature^ Feature2 ) ``` | |

#### Parameters

*Feature1*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

*Feature2*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertIntersectLineFeature::GetPlaneFeatures](swdocumentmgr~SwDMDimXpertIntersectLineFeature~GetPlaneFeatures.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature.md)
  
[ISwDMDimXpertIntersectLineFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

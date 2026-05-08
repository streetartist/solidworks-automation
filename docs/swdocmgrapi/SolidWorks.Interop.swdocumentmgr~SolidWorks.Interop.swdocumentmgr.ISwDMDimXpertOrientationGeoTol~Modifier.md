# Modifier Property (ISwDMDimXpertOrientationGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~Modifier`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~Modifier.html) on this topic. |
| Modifier Property (ISwDMDimXpertOrientationGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.md) : Modifier Property (ISwDMDimXpertOrientationGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the material condition modifier for this DimXpert orientation geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property Modifier As swDmDimXpertMaterialConditionModifier_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertOrientationGeoTol Dim value As swDmDimXpertMaterialConditionModifier_e   value = instance.Modifier ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertMaterialConditionModifier_e Modifier {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertMaterialConditionModifier_e Modifier {    swDmDimXpertMaterialConditionModifier_e get(); } ``` | |

#### Property Value

Material condition modifier as defined in [swDmDimXpertMaterialConditionModifier\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertOrientationGeoTol::Modifier](swdocumentmgr~SwDMDimXpertOrientationGeoTol~Modifier.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.md)
  
[ISwDMDimXpertOrientationGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

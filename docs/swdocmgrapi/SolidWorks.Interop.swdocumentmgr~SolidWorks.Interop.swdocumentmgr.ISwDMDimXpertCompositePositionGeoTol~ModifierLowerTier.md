# ModifierLowerTier Property (ISwDMDimXpertCompositePositionGeoTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~ModifierLowerTier`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~ModifierLowerTier.html) on this topic. |
| ModifierLowerTier Property (ISwDMDimXpertCompositePositionGeoTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.md) : ModifierLowerTier Property (ISwDMDimXpertCompositePositionGeoTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the material condition modifer for the tolerance in the lower tier for this DimXpert composite position geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property ModifierLowerTier As swDmDimXpertMaterialConditionModifier_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompositePositionGeoTol Dim value As swDmDimXpertMaterialConditionModifier_e   value = instance.ModifierLowerTier ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertMaterialConditionModifier_e ModifierLowerTier {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertMaterialConditionModifier_e ModifierLowerTier {    swDmDimXpertMaterialConditionModifier_e get(); } ``` | |

#### Property Value

Material condition modifier in the lower tier as defined in [swDmDimXpertMaterialConditionModifier\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompositePositionGeoTol::ModifierLowerTier](swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~ModifierLowerTier.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.md)
  
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

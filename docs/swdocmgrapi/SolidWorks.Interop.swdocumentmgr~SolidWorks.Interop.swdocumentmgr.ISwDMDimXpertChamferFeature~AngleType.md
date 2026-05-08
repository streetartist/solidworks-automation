# AngleType Property (ISwDMDimXpertChamferFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature~AngleType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature~AngleType.html) on this topic. |
| AngleType Property (ISwDMDimXpertChamferFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.md) : AngleType Property (ISwDMDimXpertChamferFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the type of chamfer angle for this DimXpert chamfer.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property AngleType As swDmDimXpertChamferAngleType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertChamferFeature Dim value As swDmDimXpertChamferAngleType_e   value = instance.AngleType ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertChamferAngleType_e AngleType {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertChamferAngleType_e AngleType {    swDmDimXpertChamferAngleType_e get(); } ``` | |

#### Property Value

Type of chamfer angle as defined in [swDmDimXpertChamferAngleType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertChamferAngleType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertChamferFeature::AngleType](swdocumentmgr~SwDMDimXpertChamferFeature~AngleType.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.md)
  
[ISwDMDimXpertChamferFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

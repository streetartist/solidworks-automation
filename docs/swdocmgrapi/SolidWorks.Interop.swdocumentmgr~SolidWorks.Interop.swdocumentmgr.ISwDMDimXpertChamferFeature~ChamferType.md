# ChamferType Property (ISwDMDimXpertChamferFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature~ChamferType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature~ChamferType.html) on this topic. |
| ChamferType Property (ISwDMDimXpertChamferFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.md) : ChamferType Property (ISwDMDimXpertChamferFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the type of this DimXpert chamfer.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property ChamferType As swDmDimXpertChamferType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertChamferFeature Dim value As swDmDimXpertChamferType_e   value = instance.ChamferType ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertChamferType_e ChamferType {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertChamferType_e ChamferType {    swDmDimXpertChamferType_e get(); } ``` | |

#### Property Value

Type of chamfer as defined in [swDmDimXpertChamferType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertChamferType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertChamferFeature::ChamferType](swdocumentmgr~SwDMDimXpertChamferFeature~ChamferType.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.md)
  
[ISwDMDimXpertChamferFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

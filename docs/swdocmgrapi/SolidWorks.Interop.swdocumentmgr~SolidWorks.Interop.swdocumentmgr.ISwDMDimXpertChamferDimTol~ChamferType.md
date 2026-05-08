# ChamferType Property (ISwDMDimXpertChamferDimTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol~ChamferType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol~ChamferType.html) on this topic. |
| ChamferType Property (ISwDMDimXpertChamferDimTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertChamferDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol.md) : ChamferType Property (ISwDMDimXpertChamferDimTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the type of chamfer dimension for this DimXpert chamfer dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property ChamferType As swDmDimXpertChamferDimensionType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertChamferDimTol Dim value As swDmDimXpertChamferDimensionType_e   value = instance.ChamferType ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertChamferDimensionType_e ChamferType {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertChamferDimensionType_e ChamferType {    swDmDimXpertChamferDimensionType_e get(); } ``` | |

#### Property Value

Type of chamfer dimension as defined in [swDmDimXpertChamferDimensionType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertChamferDimensionType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertChamferDimTol::ChamferType](swdocumentmgr~SwDMDimXpertChamferDimTol~ChamferType.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertChamferDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol.md)
  
[ISwDMDimXpertChamferDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

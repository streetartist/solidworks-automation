# PatternTreatment Property (ISwDMDimXpertDistanceBetweenDimTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~PatternTreatment`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~PatternTreatment.html) on this topic. |
| PatternTreatment Property (ISwDMDimXpertDistanceBetweenDimTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol.md) : PatternTreatment Property (ISwDMDimXpertDistanceBetweenDimTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the pattern treatment for this DimXpert distance-between dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property PatternTreatment As swDmDimXpertPatternTreatmentType_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertDistanceBetweenDimTol Dim value As swDmDimXpertPatternTreatmentType_e   value = instance.PatternTreatment ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertPatternTreatmentType_e PatternTreatment {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDmDimXpertPatternTreatmentType_e PatternTreatment {    swDmDimXpertPatternTreatmentType_e get(); } ``` | |

#### Property Value

Pattern treatment for the diameter dimension tolerance as defined in [swDmDimXpertPatternTreatmentType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertPatternTreatmentType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertDistanceBetweenDimTol::PatternTreatment](swdocumentmgr~SwDMDimXpertDistanceBetweenDimTol~PatternTreatment.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol.md)
  
[ISwDMDimXpertDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

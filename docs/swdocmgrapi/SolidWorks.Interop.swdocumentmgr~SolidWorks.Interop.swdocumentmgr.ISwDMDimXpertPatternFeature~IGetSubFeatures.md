# IGetSubFeatures Method (ISwDMDimXpertPatternFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~IGetSubFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~IGetSubFeatures.html) on this topic. |
| IGetSubFeatures Method (ISwDMDimXpertPatternFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertPatternFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature.md) : IGetSubFeatures Method (ISwDMDimXpertPatternFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Count*
:   Number of sub-features in this pattern

Gets all of the sub-features in this DimXpert pattern feature.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function IGetSubFeatures( _    ByVal Count As System.Integer _ ) As SwDMDimXpertFeature ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertPatternFeature Dim Count As System.Integer Dim value As SwDMDimXpertFeature   value = instance.IGetSubFeatures(Count) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDimXpertFeature IGetSubFeatures(     System.int Count ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDimXpertFeature^ IGetSubFeatures(  &   System.int Count ) ``` | |

#### Parameters

*Count*
:   Number of sub-features in this pattern

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

# Remarks

Use [ISwDMDimXpertPatternFeature::GetSubFeatureCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~GetSubFeatureCount.md) to populate the Count argument.

# See Also

#### 

[ISwDMDimXpertPatternFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature.md)
  
[ISwDMDimXpertPatternFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature_members.md)
  
[ISwDMDimXpertPatternFeature::GetSubFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~GetSubFeatures.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

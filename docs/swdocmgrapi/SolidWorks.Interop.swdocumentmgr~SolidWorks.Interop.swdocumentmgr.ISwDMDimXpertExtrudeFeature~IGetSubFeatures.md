# IGetSubFeatures Method (ISwDMDimXpertExtrudeFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~IGetSubFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~IGetSubFeatures.html) on this topic. |
| IGetSubFeatures Method (ISwDMDimXpertExtrudeFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.md) : IGetSubFeatures Method (ISwDMDimXpertExtrudeFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Count*
:   Number of sub-features in the extrude

Gets all of the sub-features of this DimXpert extrude.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function IGetSubFeatures( _    ByVal Count As System.Integer _ ) As SwDMDimXpertFeature ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertExtrudeFeature Dim Count As System.Integer Dim value As SwDMDimXpertFeature   value = instance.IGetSubFeatures(Count) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDimXpertFeature IGetSubFeatures(     System.int Count ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDimXpertFeature^ IGetSubFeatures(  &   System.int Count ) ``` | |

#### Parameters

*Count*
:   Number of sub-features in the extrude

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

# Remarks

Use [ISwDMDimXpertExtrudeFeature::GetSubFeatureCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetSubFeatureCount.md) to populate the Count argument.

# See Also

#### 

[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.md)
  
[ISwDMDimXpertExtrudeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature_members.md)
  
[ISwDMDimXpertExtrudeFeature::GetSubFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetSubFeatures.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

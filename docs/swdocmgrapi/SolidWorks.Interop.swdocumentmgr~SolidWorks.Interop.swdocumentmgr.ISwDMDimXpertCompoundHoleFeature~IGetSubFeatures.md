# IGetSubFeatures Method (ISwDMDimXpertCompoundHoleFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~IGetSubFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~IGetSubFeatures.html) on this topic. |
| IGetSubFeatures Method (ISwDMDimXpertCompoundHoleFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature.md) : IGetSubFeatures Method (ISwDMDimXpertCompoundHoleFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Count*
:   Number of sub-features in this compound hole

Gets all of the sub-features of this DimXpert compound hole.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function IGetSubFeatures( _    ByVal Count As System.Integer _ ) As SwDMDimXpertFeature ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompoundHoleFeature Dim Count As System.Integer Dim value As SwDMDimXpertFeature   value = instance.IGetSubFeatures(Count) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDimXpertFeature IGetSubFeatures(     System.int Count ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDimXpertFeature^ IGetSubFeatures(  &   System.int Count ) ``` | |

#### Parameters

*Count*
:   Number of sub-features in this compound hole

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

# Remarks

Use [ISwDMDimXpertCompoundHoleFeature::GetSubFeatureCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetSubFeatureCount.md) to populate the Count argument.

# See Also

#### 

[ISwDMDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature.md)
  
[ISwDMDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature_members.md)
  
[ISwDMDimXpertCompoundHoleFeature::GetSubFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetSubFeatures.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

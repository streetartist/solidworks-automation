# IGetCadIdentifiers Method (ISwDMDimXpertFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~IGetCadIdentifiers`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~IGetCadIdentifiers.html) on this topic. |
| IGetCadIdentifiers Method (ISwDMDimXpertFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md) : IGetCadIdentifiers Method (ISwDMDimXpertFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Count*
:   Number of CAD identifiers

Gets all of the CAD identifiers of this DimXpert feature.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function IGetCadIdentifiers( _    ByVal Count As System.Integer _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertFeature Dim Count As System.Integer Dim value As System.String   value = instance.IGetCadIdentifiers(Count) ``` | |

| C# |  |
| --- | --- |
| ``` System.string IGetCadIdentifiers(     System.int Count ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ IGetCadIdentifiers(  &   System.int Count ) ``` | |

#### Parameters

*Count*
:   Number of CAD identifiers

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings; the format of each string is bodyid:faceid
- VBA, VB.NET, C#, and C++/CLI: Not supported

# Remarks

Use [ISwDMDimXpertFeature::GetCadIdentifierCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~GetCadIdentifierCount.md) to populate the Count argument.

# See Also

#### 

[ISwDMDimXpertFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)
  
[ISwDMDimXpertFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.md)
  
[ISwDMDimXpertFeature::GetCadIdentifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~GetCadIdentifiers.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

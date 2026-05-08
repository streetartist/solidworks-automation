# GetEndFeatures Method (ISwDMDimXpertCompoundClosedSlot3dFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetEndFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetEndFeatures.html) on this topic. |
| GetEndFeatures Method (ISwDMDimXpertCompoundClosedSlot3dFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompoundClosedSlot3dFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature.md) : GetEndFeatures Method (ISwDMDimXpertCompoundClosedSlot3dFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*End1*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

*End2*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

Gets the DimXpert features at both closed ends of this DimXpert compound closed slot.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetEndFeatures( _    ByRef End1 As SwDMDimXpertFeature, _    ByRef End2 As SwDMDimXpertFeature _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompoundClosedSlot3dFeature Dim End1 As SwDMDimXpertFeature Dim End2 As SwDMDimXpertFeature Dim value As System.Boolean   value = instance.GetEndFeatures(End1, End2) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetEndFeatures(     out SwDMDimXpertFeature End1,    out SwDMDimXpertFeature End2 ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetEndFeatures(  &   [Out] SwDMDimXpertFeature^ End1, &   [Out] SwDMDimXpertFeature^ End2 ) ``` | |

#### Parameters

*End1*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

*End2*
:   [ISwDMDimXpertFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.md)

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompoundClosedSlot3dFeature::GetEndFeatures](swdocumentmgr~SwDMDimXpertCompoundClosedSlot3dFeature~GetEndFeatures.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompoundClosedSlot3dFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature.md)
  
[ISwDMDimXpertCompoundClosedSlot3dFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

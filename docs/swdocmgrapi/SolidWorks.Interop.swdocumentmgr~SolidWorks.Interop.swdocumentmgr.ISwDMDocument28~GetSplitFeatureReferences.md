# GetSplitFeatureReferences Method (ISwDMDocument28)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28~GetSplitFeatureReferences`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28~GetSplitFeatureReferences.html) on this topic. |
| GetSplitFeatureReferences Method (ISwDMDocument28) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.md) : GetSplitFeatureReferences Method (ISwDMDocument28) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*SrcOption*
:   [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)

Gets the split parts in this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetSplitFeatureReferences( _    ByVal SrcOption As SwDMSearchOption _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument28 Dim SrcOption As SwDMSearchOption Dim value As System.Object   value = instance.GetSplitFeatureReferences(SrcOption) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetSplitFeatureReferences(     SwDMSearchOption SrcOption ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetSplitFeatureReferences(  &   SwDMSearchOption^ SrcOption ) ``` | |

#### Parameters

*SrcOption*
:   [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)

#### Return Value

Array of paths of split parts

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument28::GetSplitFeatureReferences](swdocumentmgr~SwDMDocument28~GetSplitFeatureReferences.md).

# Remarks

SOLIDWORKS 2022 allows you to Pack and Go parts created by the Save Bodies and Split features. The split parts created are listed as references of the parent part.

# See Also

#### 

[ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.md)
  
[ISwDMDocument28 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28_members.md)

# Availability

SOLIDWORKS Document Manager API 2022 SP0

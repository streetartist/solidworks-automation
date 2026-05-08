# SetStockFeatureReferences Method (ISwDMDocument28)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28~SetStockFeatureReferences`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28~SetStockFeatureReferences.html) on this topic. |
| SetStockFeatureReferences Method (ISwDMDocument28) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.md) : SetStockFeatureReferences Method (ISwDMDocument28) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*ListOfSplitPartPaths*
:   Array of paths of split parts

*ListOfModifiedSplitPartPaths*
:   Array of renamed paths of split parts

*NewPathName*
:   New path name

Sets the specified split parts in this stock part document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub SetStockFeatureReferences( _    ByVal ListOfSplitPartPaths As System.Object, _    ByVal ListOfModifiedSplitPartPaths As System.Object, _    ByVal NewPathName As System.String _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument28 Dim ListOfSplitPartPaths As System.Object Dim ListOfModifiedSplitPartPaths As System.Object Dim NewPathName As System.String   instance.SetStockFeatureReferences(ListOfSplitPartPaths, ListOfModifiedSplitPartPaths, NewPathName) ``` | |

| C# |  |
| --- | --- |
| ``` void SetStockFeatureReferences(     System.object ListOfSplitPartPaths,    System.object ListOfModifiedSplitPartPaths,    System.string NewPathName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void SetStockFeatureReferences(  &   System.Object^ ListOfSplitPartPaths, &   System.Object^ ListOfModifiedSplitPartPaths, &   System.String^ NewPathName ) ``` | |

#### Parameters

*ListOfSplitPartPaths*
:   Array of paths of split parts

*ListOfModifiedSplitPartPaths*
:   Array of renamed paths of split parts

*NewPathName*
:   New path name

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument28::SetStockFeatureReferences](swdocumentmgr~SwDMDocument28~SetStockFeatureReferences.md).

# Remarks

SOLIDWORKS 2022 allows you to Pack and Go parts created by the Save Bodies and Split features. The split parts created are listed as references of the parent
part.

# See Also

#### 

[ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.md)
  
[ISwDMDocument28 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28_members.md)

# Availability

SOLIDWORKS Document Manager API 2022 SP0

# HasFrozenFeatures Method (ISwDMDocument16)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16~HasFrozenFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16~HasFrozenFeatures.html) on this topic. |
| HasFrozenFeatures Method (ISwDMDocument16) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16.md) : HasFrozenFeatures Method (ISwDMDocument16) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FrozenFeatureNeedsUpdate*
:   True if the document has frozen features that need to be updated, false if not (see **Remarks**)

Gets whether the document has frozen features and whether those features need to be updated.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function HasFrozenFeatures( _    ByRef FrozenFeatureNeedsUpdate As System.Boolean _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument16 Dim FrozenFeatureNeedsUpdate As System.Boolean Dim value As System.Boolean   value = instance.HasFrozenFeatures(FrozenFeatureNeedsUpdate) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool HasFrozenFeatures(     out System.bool FrozenFeatureNeedsUpdate ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool HasFrozenFeatures(  &   [Out] System.bool FrozenFeatureNeedsUpdate ) ``` | |

#### Parameters

*FrozenFeatureNeedsUpdate*
:   True if the document has frozen features that need to be updated, false if not (see **Remarks**)

#### Return Value

True if the document has frozen features, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument16::HasFrozenFeatures](swdocumentmgr~SwDMDocument16~HasFrozenFeatures.md).

# Example

[Get Whether Part Has Frozen Features (C#)](Get_Whether_Part_Has_Frozen_Features_Example_CSharp.htm)
  
[Get Whether Part Has Frozen Features (VB.NET)](Get_Whether_Part_Has_Frozen_Features_Example_vbnet.htm)

# Remarks

The FrozenFeatureNeedsUpdate return value is only valid if the document has frozen features.

# See Also

#### 

[ISwDMDocument16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16.md)
  
[ISwDMDocument16 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16_members.md)

# Availability

SOLIDWORKS Document Manager API 2012 SP0

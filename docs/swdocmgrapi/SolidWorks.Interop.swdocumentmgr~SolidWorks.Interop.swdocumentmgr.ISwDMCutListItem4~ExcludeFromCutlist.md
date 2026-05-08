# ExcludeFromCutlist Property (ISwDMCutListItem4)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4~ExcludeFromCutlist`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4~ExcludeFromCutlist.html) on this topic. |
| ExcludeFromCutlist Property (ISwDMCutListItem4) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4.md) : ExcludeFromCutlist Property (ISwDMCutListItem4) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether this item is excluded from the cut list.

**NOTE: This property is a get-only property. Set is not implemented.**

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property ExcludeFromCutlist As swDMCutListExclusionStatus_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem4 Dim value As swDMCutListExclusionStatus_e   instance.ExcludeFromCutlist = value   value = instance.ExcludeFromCutlist ``` | |

| C# |  |
| --- | --- |
| ``` swDMCutListExclusionStatus_e ExcludeFromCutlist {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property swDMCutListExclusionStatus_e ExcludeFromCutlist {    swDMCutListExclusionStatus_e get();    void set ( &   swDMCutListExclusionStatus_e value); } ``` | |

#### Property Value

As defined by [swDMCutListExclusionStatus \_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDMCutListExclusionStatus_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem4::ExcludeFromCutlist](swdocumentmgr~SwDMCutListItem4~ExcludeFromCutlist.md).

# Remarks

This property is only valid for documents saved in SOLIDWORKS 2021 or later.

# See Also

#### 

[ISwDMCutListItem4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4.md)
  
[ISwDMCutListItem4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4_members.md)

# Availability

SOLIDWORKS Document Manager API 2021 SP0

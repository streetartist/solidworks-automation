# ChildFolderName Property (ISwDMCutListItem2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~ChildFolderName`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~ChildFolderName.html) on this topic. |
| ChildFolderName Property (ISwDMCutListItem2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md) : ChildFolderName Property (ISwDMCutListItem2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the name of the cut list's child folder, if it exists.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property ChildFolderName As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem2 Dim value As System.String   instance.ChildFolderName = value   value = instance.ChildFolderName ``` | |

| C# |  |
| --- | --- |
| ``` System.string ChildFolderName {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ ChildFolderName {    System.String^ get();    void set ( &   System.String^ value); } ``` | |

#### Property Value

Name of cut list's child folder, if it exists

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem2::ChildFolderName](swdocumentmgr~SwDMCutListItem2~ChildFolderName.md).

# Remarks

This property only supports documents saved in SOLIDWORKS 2009 or later.

# See Also

#### 

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md)
  
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0

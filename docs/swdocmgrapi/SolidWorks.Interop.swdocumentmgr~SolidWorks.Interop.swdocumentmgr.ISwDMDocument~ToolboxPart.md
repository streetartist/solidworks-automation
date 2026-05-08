# ToolboxPart Property (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ToolboxPart`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ToolboxPart.html) on this topic. |
| ToolboxPart Property (ISwDMDocument) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : ToolboxPart Property (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets or sets whether this file is a SOLIDWORKS Toolbox file.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property ToolboxPart As SwDmToolboxPartType ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim value As SwDmToolboxPartType   instance.ToolboxPart = value   value = instance.ToolboxPart ``` | |

| C# |  |
| --- | --- |
| ``` SwDmToolboxPartType ToolboxPart {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property SwDmToolboxPartType ToolboxPart {    SwDmToolboxPartType get();    void set ( &   SwDmToolboxPartType value); } ``` | |

#### Property Value

Type of SOLIDWORKS Toolbox part as defined by [SwDmToolboxPartType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmToolboxPartType.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::ToolboxPart](swdocumentmgr~SwDMDocument~ToolboxPart.md).

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS

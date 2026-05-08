# GetDisplayStates Method (ISwDMConfiguration10)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10~GetDisplayStates`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10~GetDisplayStates.html) on this topic. |
| GetDisplayStates Method (ISwDMConfiguration10) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10.md) : GetDisplayStates Method (ISwDMConfiguration10) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the names of the display states for this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetDisplayStates() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration10 Dim value As System.Object   value = instance.GetDisplayStates() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetDisplayStates() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetDisplayStates(); ``` | |

#### Return Value

Array of the names of the display states for this configuration

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration10::GetDisplayStates](swdocumentmgr~SwDMConfiguration10~GetDisplayStates.md).

# Remarks

The first name in the list is the active display state.

# See Also

#### 

[ISwDMConfiguration10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10.md)
  
[ISwDMConfiguration10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10_members.md)

# Availability

SOLIDWORKS Document Manager API 2008 SP5

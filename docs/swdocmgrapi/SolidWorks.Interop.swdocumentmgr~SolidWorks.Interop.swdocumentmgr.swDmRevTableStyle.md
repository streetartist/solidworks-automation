# swDmRevTableStyle Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmRevTableStyle`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmRevTableStyle.html) on this topic. |
| swDmRevTableStyle Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : swDmRevTableStyle Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Multiple drawing sheet styles for revision tables.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum swDmRevTableStyle     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As swDmRevTableStyle ``` | |

| C# |  |
| --- | --- |
| ``` public enum swDmRevTableStyle : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class swDmRevTableStyle : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swDmRevCopyOfSheet1** | 1 = Linked; copies the revision table on sheet 1 to all sheets, updating all revision tables when revisions are made |
| **swDmRevIndependent** | 2 = Independent; makes the revision table on each sheet independent of the other revision tables in the drawing; updates to one revision table do not affect other revision tables |
| **swDmRevSeeSheet1** | 0 = See Sheet 1; makes the revision table on the first sheet the active table, labeling the revision tables on all other drawing sheets, **See Sheet 1** |
| **swDmRevStyleUnknown** | -1 |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

# swDmShowChildComponentsInBOMResult Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmShowChildComponentsInBOMResult`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmShowChildComponentsInBOMResult.html) on this topic. |
| swDmShowChildComponentsInBOMResult Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : swDmShowChildComponentsInBOMResult Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

How components are displayed in the bill of materials (BOM).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum swDmShowChildComponentsInBOMResult     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As swDmShowChildComponentsInBOMResult ``` | |

| C# |  |
| --- | --- |
| ``` public enum swDmShowChildComponentsInBOMResult : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class swDmShowChildComponentsInBOMResult : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swDmShowChildComponentsInBOM\_FALSE** | 0 = Do not display child components in the BOM; the subassembly appears as a single item |
| **swDmShowChildComponentsInBOM\_NotDefined** | -1 = Document was saved in an older version of SOLIDWORKS; you must save document in SOLIDWORKS 2009 or later |
| **swDmShowChildComponentsInBOM\_Promote** | 2 = All of the child components are promoted one level; the configuration dissolves when it appears in a BOM |
| **swDmShowChildComponentsInBOM\_TRUE** | 1 = List child components individually in the BOM |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

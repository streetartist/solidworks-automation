# swDmExcludeFromBOMResult Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmExcludeFromBOMResult`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmExcludeFromBOMResult.html) on this topic. |
| swDmExcludeFromBOMResult Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : swDmExcludeFromBOMResult Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Bill of materials (BOM) components exclusion options.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum swDmExcludeFromBOMResult     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As swDmExcludeFromBOMResult ``` | |

| C# |  |
| --- | --- |
| ``` public enum swDmExcludeFromBOMResult : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class swDmExcludeFromBOMResult : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swDmExcludeFromBOM\_FALSE** | 0 = Do not exclude components from BOM. |
| **swDmExcludeFromBOM\_NotDefined** | - 1 = Indicates that the document was created or saved in SOLIDWORKS 2008 SP01 or earlier. Open and save the document in SOLIDWORKS 2008 SP02 or later. |
| **swDmExcludeFromBOM\_TRUE** | 1 = Exclude components from BOM. |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)
